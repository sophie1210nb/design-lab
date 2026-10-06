# -*- coding: utf-8 -*-
"""Xoá chữ/vật thừa trong ảnh bằng LaMa (ONNX, chạy offline trên CPU).

Dùng:
  python xoa_chu_anh.py VAO.jpg RA.jpg 100,50,600,180 [x0,y0,x1,y1 ...]
  python xoa_chu_anh.py VAO.jpg RA.jpg --mask mat-na.png      (trắng = vùng cần xoá)
  python xoa_chu_anh.py VAO.jpg RA.jpg 100,50,600,180 590,40,700,200:sang
      (hậu tố :sang / :toi = chỉ xoá pixel giống chữ sáng/tối trong hình đó — dùng khi chữ sát người)
Tuỳ chọn: --pad-ratio 0.4 (vùng xoá chiếm tối đa ~40% cửa sổ), --feather 6 (px làm mềm mép),
          --quality 92, --model đường-dẫn-lama.onnx
Pixel ngoài vùng mask giữ NGUYÊN (giữ độ phân giải / độ nét gốc).
"""
import argparse, os, sys
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
import onnxruntime as ort

_HOME = os.path.expanduser("~")
# Mặc định ~/.thiet-ke-models/lama_fp32.onnx (đổi bằng --model).
MODEL = os.path.join(_HOME, ".thiet-ke-models", "lama_fp32.onnx")
S = 512


def parse_rect(s):
    x0, y0, x1, y1 = [int(round(float(v))) for v in s.split(",")]
    return min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)


def components(mask):
    """Tách mask (bool HxW) thành các vùng liên thông -> (nhãn HxW, [(id, bbox)...])."""
    import cv2
    n, lab, st, _ = cv2.connectedComponentsWithStats(mask.astype(np.uint8), 8)
    return lab, [(i, (st[i, 0], st[i, 1], st[i, 0] + st[i, 2], st[i, 1] + st[i, 3])) for i in range(1, n)]


def window_for(b, W, H, pad_ratio, area=None):
    x0, y0, x1, y1 = b
    bw, bh = x1 - x0, y1 - y0
    # cửa sổ vuông, cạnh sao cho diện tích lỗ <= pad_ratio * diện tích cửa sổ, và mỗi phía có lề
    side = max(bw, bh) + 2 * max(32, int(0.15 * max(bw, bh)))
    area = bw * bh if area is None else area
    side = max(side, int(np.ceil(np.sqrt(area / pad_ratio))), 256)
    side = min(side, max(W, H))
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    ww, wh = min(side, W), min(side, H)
    wx0 = int(np.clip(cx - ww / 2, 0, W - ww)); wy0 = int(np.clip(cy - wh / 2, 0, H - wh))
    return wx0, wy0, wx0 + ww, wy0 + wh


def run_lama(sess, img, msk):
    """img: HxWx3 uint8, msk: HxW float 0/1 -> HxWx3 float 0..255 (cùng kích thước)."""
    h, w = msk.shape
    im = np.asarray(Image.fromarray(img).resize((S, S), Image.LANCZOS), np.float32) / 255.0
    mk = np.asarray(Image.fromarray((msk * 255).astype(np.uint8)).resize((S, S), Image.BILINEAR), np.float32) / 255.0
    mk = (mk > 0.1).astype(np.float32)
    out = sess.run(None, {"image": im.transpose(2, 0, 1)[None], "mask": mk[None, None]})[0][0]
    out = out.transpose(1, 2, 0)
    if out.max() <= 1.5:
        out = out * 255.0
    out = np.clip(out, 0, 255).astype(np.uint8)
    return np.asarray(Image.fromarray(out).resize((w, h), Image.LANCZOS), np.float32)


def match_border(orig, fill, m, ring=6, valid=None):
    """Khớp tông: lấy chênh lệch (gốc - vá) trên vành ngay ngoài mask, khuếch tán mượt vào trong mask."""
    import cv2
    mk = (m > 0).astype(np.uint8)
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * ring + 1, 2 * ring + 1))
    rg = (cv2.dilate(mk, k) - mk).astype(np.float32)
    diff = np.abs(orig - fill).max(axis=2)
    rg = rg * (diff < 40)
    if valid is not None:
        rg = rg * valid  # bỏ điểm vành lệch quá nhiều (biên người/vật) để không kéo màu lạ vào
    if rg.sum() < 10:
        return fill
    sig = max(8.0, 0.04 * max(m.shape))
    wsum = cv2.GaussianBlur(rg, (0, 0), sig) + 1e-4
    out = fill.copy()
    for c in range(3):
        d = (orig[..., c] - fill[..., c]) * rg
        corr = cv2.GaussianBlur(d, (0, 0), sig) / wsum
        # chỗ xa vành (trọng số rất nhỏ) dùng chênh lệch trung bình
        mean = (d.sum() / rg.sum())
        wn = np.clip(wsum / (wsum.max() + 1e-6) * 4, 0, 1)
        out[..., c] = fill[..., c] + corr * wn + mean * (1 - wn)
    return np.clip(out, 0, 255)


def main():
    ap = argparse.ArgumentParser(description="Xoá chữ trong ảnh bằng LaMa")
    ap.add_argument("inp"); ap.add_argument("out")
    ap.add_argument("rects", nargs="*", help="x0,y0,x1,y1 theo pixel ảnh gốc")
    ap.add_argument("--mask", help="PNG mask: trắng = xoá")
    ap.add_argument("--pad-ratio", type=float, default=0.4)
    ap.add_argument("--feather", type=int, default=6)
    ap.add_argument("--dilate", type=int, default=8, help="nới mask thêm N px trước khi inpaint")
    ap.add_argument("--chi-chu", choices=["sang", "toi"],
                    help="trong mỗi hình chữ nhật chỉ xoá pixel giống CHỮ: 'sang' = chữ sáng trên nền tối, "
                         "'toi' = chữ tối trên nền sáng (so với trung vị độ sáng của hình chữ nhật). "
                         "Giúp không đụng tóc/da/áo người đứng sát chữ.")
    ap.add_argument("--nguong", type=float, default=35, help="độ chênh sáng để coi là chữ (mặc định 35)")
    ap.add_argument("--nguong-max", type=float, default=110,
                    help="với chế độ 'toi': pixel tối hơn nền quá mức này coi là người/vật (áo, tóc) và giữ nguyên")
    ap.add_argument("--bo-mau-dam", type=float, default=90,
                    help="với --chi-chu: bỏ qua pixel màu rực (max-min kênh > giá trị này), mặc định 90; <0 để tắt")
    ap.add_argument("--bo-mau-am", type=float, default=22,
                    help="với --chi-chu: bỏ qua pixel tông ấm (R-B > giá trị này) như da, tóc (mặc định 22; <0 để tắt)")
    ap.add_argument("--poly", action="append", default=[],
                    help='đa giác xoá CHÍNH XÁC (không nới), vd "10,10 200,15 190,90 12,80" — dùng sát mép người; lặp lại được')
    ap.add_argument("--giu", action="append", default=[],
                    help="x0,y0,x1,y1 vùng BẢO VỆ (mặt, tóc, tay...) — không bao giờ bị sửa; lặp lại được")
    ap.add_argument("--khong-chinh-mau", action="store_true",
                    help="tắt bước khớp màu vùng vá với viền xung quanh")
    ap.add_argument("--xem-mask", help="chỉ xuất ảnh xem trước mask (đỏ = vùng sẽ xoá) ra file này rồi dừng, không chạy LaMa")
    ap.add_argument("--luu-mask", help="lưu mask (trước khi nới) ra PNG để kiểm tra")
    ap.add_argument("--quality", type=int, default=92)
    ap.add_argument("--model", default=MODEL)
    a = ap.parse_args()

    src = Image.open(a.inp).convert("RGB")
    W, H = src.size
    mimg = Image.new("L", (W, H), 0)
    if a.mask:
        mimg = Image.open(a.mask).convert("L").resize((W, H))
        mimg = mimg.point(lambda v: 255 if v > 127 else 0)
    d = ImageDraw.Draw(mimg)
    arr = np.asarray(src, np.float32)
    lum = arr @ np.array([0.299, 0.587, 0.114], np.float32)
    chu_rects = []
    for r in a.rects:
        mode = a.chi_chu
        if ":" in r:  # "x0,y0,x1,y1:sang" / ":toi" / ":full" = chế độ riêng cho hình chữ nhật này
            r, mode = r.split(":", 1)
            mode = None if mode == "full" else mode
        x0, y0, x1, y1 = parse_rect(r)
        if not mode:
            d.rectangle((x0, y0, x1, y1), fill=255)
            continue
        L = lum[y0:y1, x0:x1]
        # độ sáng nền: chữ tối trên nền sáng -> lấy phân vị 85 (không bị kéo bởi áo/tóc tối trong khung)
        med = np.percentile(L, 85) if mode == "toi" else np.median(L)
        chu_rects.append((x0, y0, x1, y1, mode, med))
        if mode == "sang":
            sel = L > med + a.nguong
        else:  # chữ tối: tối hơn nền nhưng không quá tối (áo vest, tóc đen bị loại)
            sel = (L < med - a.nguong) & (L > med - a.nguong_max)
        sub = arr[y0:y1, x0:x1]
        if a.bo_mau_am >= 0:
            sel &= (sub[..., 0] - sub[..., 2]) <= a.bo_mau_am
        if a.bo_mau_dam >= 0:  # bỏ pixel màu rực (viền đèn tím/xanh trên áo...) — chữ thường ít bão hoà
            sel &= (sub.max(axis=2) - sub.min(axis=2)) <= a.bo_mau_dam
        cur = np.asarray(mimg).copy()
        cur[y0:y1, x0:x1][sel] = 255
        mimg = Image.fromarray(cur); d = ImageDraw.Draw(mimg)
    if a.luu_mask:
        mimg.save(a.luu_mask)
    if a.dilate > 0:
        mimg = mimg.filter(ImageFilter.MaxFilter(2 * a.dilate + 1))
    mask = np.asarray(mimg) > 127
    mask = mask.copy()
    # sau khi nới: trong các hình chế độ chữ, bỏ lại pixel KHÔNG phải nền/chữ (da, tóc ấm; áo/tóc tối hoặc sáng ngược)
    for x0, y0, x1, y1, mode, med in chu_rects:
        dd = a.dilate + 1
        x0, y0, x1, y1 = max(0, x0 - dd), max(0, y0 - dd), min(W, x1 + dd), min(H, y1 + dd)
        sub = arr[y0:y1, x0:x1]; L = lum[y0:y1, x0:x1]
        bad = (L < med - a.nguong) if mode == "sang" else ((L > med + a.nguong) | (L < med - a.nguong_max))
        if a.bo_mau_am >= 0:
            bad |= (sub[..., 0] - sub[..., 2]) > a.bo_mau_am
        if a.bo_mau_dam >= 0:
            bad |= (sub.max(axis=2) - sub.min(axis=2)) > a.bo_mau_dam
        mask[y0:y1, x0:x1] &= ~bad
    polym = np.zeros((H, W), bool)
    if a.poly:
        pm = Image.new("L", (W, H), 0); pd = ImageDraw.Draw(pm)
        for pl in a.poly:
            pts = [tuple(float(v) for v in q.split(",")) for q in pl.split()]
            pd.polygon(pts, fill=255)
        polym = np.asarray(pm) > 127
        mask |= polym
    for g in a.giu:
        x0, y0, x1, y1 = parse_rect(g)
        mask[y0:y1, x0:x1] = False
    if not mask.any():
        sys.exit("Không có vùng mask nào.")
    if a.xem_mask:
        pv = np.asarray(src).copy()
        pv[mask] = (0.45 * pv[mask] + 0.55 * np.array([255, 0, 0])).astype(np.uint8)
        Image.fromarray(pv).save(a.xem_mask, quality=90)
        print("Đã lưu xem trước mask ->", a.xem_mask)
        return

    sess = ort.InferenceSession(a.model, providers=["CPUExecutionProvider"])
    base = np.asarray(src).copy()
    result = base.astype(np.float32)
    # gom các mảnh mask gần nhau (từng chữ cái) thành một vùng để chạy LaMa một lần
    grp = np.asarray(Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(41))) > 127
    lab, comps = components(grp)
    todo = mask.copy()  # vùng chưa vá (còn chữ) — luôn che khi đưa vào LaMa để mô hình không "chép" lại chữ
    for cid, b in comps:
        mine = mask & (lab == cid)
        wx0, wy0, wx1, wy1 = window_for(b, W, H, a.pad_ratio, int(mine.sum()))
        m = mine[wy0:wy1, wx0:wx1].astype(np.float32)
        hole = todo[wy0:wy1, wx0:wx1].astype(np.float32)
        cur = np.clip(result[wy0:wy1, wx0:wx1] + 0.5, 0, 255).astype(np.uint8)
        fill = run_lama(sess, cur, hole)
        if not a.khong_chinh_mau:
            fill = match_border(cur.astype(np.float32), fill, m, valid=1 - hole)
        # alpha mềm: 0 ở mép mask -> 1 khi vào sâu `feather` px (vành nới --dilate không chứa chữ nên ramp an toàn)
        if a.feather > 0:
            import cv2
            dist = cv2.distanceTransform((m > 0).astype(np.uint8), cv2.DIST_L2, 5)
            al = np.clip(dist / a.feather, 0, 1)
            al = np.maximum(al, polym[wy0:wy1, wx0:wx1] & (m > 0))  # đa giác: mép cứng (sát mép người)
        else:
            al = m
        al = al[..., None]
        reg = result[wy0:wy1, wx0:wx1]
        result[wy0:wy1, wx0:wx1] = reg * (1 - al) + fill * al
        todo &= ~mine
        print(f"  vùng {tuple(int(v) for v in b)} -> cửa sổ {(wx0, wy0, wx1, wy1)}")
    out = np.clip(result + 0.5, 0, 255).astype(np.uint8)
    out[~mask] = base[~mask]  # đảm bảo pixel ngoài mask y hệt gốc
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    kw = {"quality": a.quality, "subsampling": 0} if a.out.lower().endswith((".jpg", ".jpeg")) else {}
    exif = src.info.get("icc_profile")
    if exif:
        kw["icc_profile"] = exif
    Image.fromarray(out).save(a.out, **kw)
    print("OK ->", a.out)


if __name__ == "__main__":
    main()
