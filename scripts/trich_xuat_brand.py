# -*- coding: utf-8 -*-
"""Trích xuất visual thương hiệu từ tư liệu có sẵn (logo, ảnh bài đăng cũ, ảnh chụp website…).

Dùng:
    python scripts/trich_xuat_brand.py <thư mục hoặc ảnh...> [--logo logo.png] [--out brands/<ten-brand>] [--k 8]

Tạo trong --out:
    brand-audit.md     bảng màu chung + theo từng ảnh, vai trò gợi ý, tương phản, nhận xét
    tokens-goi-y.css   tokens.css điền sẵn màu gợi ý (font giữ mặc định)
Chỉ là GỢI Ý: luôn nhìn lại bằng mắt, ưu tiên mã màu trong logo gốc / guideline.
Cần: pip install pillow
"""
import argparse, colorsys, datetime, os, sys
from PIL import Image

EXT = (".png", ".jpg", ".jpeg", ".webp")


def files_from(paths):
    out = []
    for p in paths:
        if os.path.isdir(p):
            for root, _, fs in os.walk(p):
                out += [os.path.join(root, f) for f in sorted(fs) if f.lower().endswith(EXT)]
        elif p.lower().endswith(EXT) and os.path.isfile(p):
            out.append(p)
    return out


def palette(path, k):
    im = Image.open(path)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGBA", im.size, (0, 0, 0, 0))
        alpha = im.split()[-1]
    else:
        alpha = None
    im = im.convert("RGB")
    im.thumbnail((320, 320))
    if alpha is not None:
        alpha = alpha.resize(im.size)
    q = im.quantize(colors=k, method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette()[: k * 3]
    counts = [0] * k
    px = q.load(); ap = alpha.load() if alpha is not None else None
    w, h = q.size
    for y in range(h):
        for x in range(w):
            if ap is not None and ap[x, y] < 128:
                continue
            counts[px[x, y]] += 1
    tot = sum(counts) or 1
    res = [((pal[i * 3], pal[i * 3 + 1], pal[i * 3 + 2]), counts[i] / tot) for i in range(k) if counts[i]]
    return sorted(res, key=lambda t: -t[1])


def hexc(c):
    return "#%02X%02X%02X" % c


def lum(c):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = c
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def contrast(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)


def hls(c):
    h, l, s = colorsys.rgb_to_hls(*(v / 255 for v in c))
    return h * 360, l, s


def dist(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5


def hue_accent(files, bg):
    """Tìm màu nhấn theo điểm ảnh: gom các điểm ảnh bão hòa (s>0.35, 0.25<l<0.88) theo dải màu 10°,
    ưu tiên dải lặp lại ở nhiều ảnh. Trả về (màu trung bình, số ảnh có, xếp hạng các dải)."""
    bins = {}
    for i, f in enumerate(files):
        im = Image.open(f).convert("RGB"); im.thumbnail((220, 220))
        px = list(im.get_flattened_data() if hasattr(im, 'get_flattened_data') else im.getdata()); n = len(px) or 1; loc = {}
        for c in px:
            h, l, sat = hls(c)
            if sat > 0.35 and 0.25 < l < 0.88 and dist(c, bg) > 70:
                b = int(h // 10)
                e = loc.setdefault(b, [0, 0, 0, 0]); e[0] += c[0]; e[1] += c[1]; e[2] += c[2]; e[3] += 1
        for b, e in loc.items():
            if e[3] / n < 0.002:
                continue
            g = bins.setdefault(b, [0, 0, 0, 0, 0.0, 0])
            for k in range(4): g[k] += e[k]
            g[4] += (e[3] / n) ** 0.5; g[5] += 1
    if not bins:
        return None, 0, []
    rank = sorted(bins.items(), key=lambda kv: kv[1][4] * kv[1][5], reverse=True)
    b, g = rank[0]
    return (round(g[0] / g[3]), round(g[1] / g[3]), round(g[2] / g[3])), g[5], rank


def merge(all_cols, thr=38):
    """Gộp các màu gần nhau giữa nhiều ảnh, cộng tỉ lệ diện tích; đếm số ảnh chứa màu."""
    groups = []
    for c, w, idx in all_cols:
        for g in groups:
            if dist(g[0], c) < thr:
                tw = g[1] + w
                g[0] = tuple(round((g[0][i] * g[1] + c[i] * w) / tw) for i in range(3))
                g[1] = tw
                g[2].add(idx)
                break
        else:
            groups.append([c, w, {idx}])
    tot = sum(g[1] for g in groups) or 1
    return sorted([(tuple(g[0]), g[1] / tot, len(g[2])) for g in groups], key=lambda t: -t[1])


def name_tone(c):
    h, l, s = hls(c)
    if s < 0.12 or l < 0.08 or l > 0.95:
        return "trung tính " + ("tối" if l < 0.3 else "sáng" if l > 0.8 else "xám")
    names = [(15, "đỏ"), (40, "cam"), (65, "vàng"), (160, "xanh lá"), (200, "xanh ngọc"), (255, "xanh dương"), (290, "tím"), (330, "hồng"), (361, "đỏ")]
    n = next(nm for lim, nm in names if h < lim)
    return n + (" đậm" if l < 0.3 else " nhạt" if l > 0.75 else "")


def main():
    ap = argparse.ArgumentParser(description="Trích xuất bảng màu & gợi ý token từ tư liệu thương hiệu")
    ap.add_argument("nguon", nargs="+")
    ap.add_argument("--logo")
    ap.add_argument("--out", default=".")
    ap.add_argument("--k", type=int, default=10)
    a = ap.parse_args()
    fs = files_from(a.nguon)
    if a.logo and a.logo not in fs:
        fs = [a.logo] + fs
    if not fs:
        sys.exit("Không thấy ảnh nào (png/jpg/webp).")
    os.makedirs(a.out, exist_ok=True)

    per, allc = [], []
    for f in fs:
        try:
            p = palette(f, a.k)
        except Exception as e:
            print("Bỏ qua", f, e); continue
        wgt = 2.0 if a.logo and os.path.samefile(f, a.logo) else 1.0
        per.append((f, p))
        allc += [(c, w * wgt, len(per)) for c, w in p]
    G = merge(allc)

    # vai trò gợi ý
    bg = G[0][0]
    dark_bg = lum(bg) < 0.18
    # chữ: màu gần trung tính, tương phản ≥ 7:1 với nền, diện tích lớn nhất; không có thì trắng / gần đen
    tc = [g[0] for g in G if contrast(g[0], bg) >= 7 and hls(g[0])[2] < 0.12]
    text = tc[0] if tc else ((250, 250, 252) if dark_bg else (17, 19, 26))
    chroma = [g for g in G[1:] if hls(g[0])[2] > 0.25 and 0.18 < hls(g[0])[1] < 0.85]
    logo_cols = []
    if a.logo:
        logo_cols = [c for c, w in palette(a.logo, 6) if hls(c)[2] > 0.25 and w > 0.03]
    # nhấn = màu "đắt" nhất: bão hòa, độ sáng vừa, khác hẳn nền, xuất hiện ở nhiều ảnh (diện tích nhỏ vẫn được)
    def score(g):
        c, w, n = g
        h, l, sat = hls(c)
        if dist(c, bg) < 70 or l < 0.15 or l > 0.9:
            return -1
        return sat * (1 - abs(l - 0.55)) * (w ** 0.35) * (n ** 0.5)
    hacc, hn, hrank = hue_accent([f for f, _ in per], bg)
    ranked = sorted(G, key=score, reverse=True)
    accent = hacc or (ranked[0][0] if ranked and score(ranked[0]) > 0 else (logo_cols[0] if logo_cols else (47, 91, 234)))
    acc_alts = [(round(g[0] / g[3]), round(g[1] / g[3]), round(g[2] / g[3])) for _, g in hrank[1:4]]
    # màu phụ: ưu tiên cùng họ màu với nền (thẻ/khối), sau đó mới tới màu khác
    def hd(x, y):
        d = abs(hls(x)[0] - hls(y)[0]); return min(d, 360 - d)
    fam = [g[0] for g in G[1:] if dist(g[0], bg) > 25 and dist(g[0], accent) > 60 and dist(g[0], text) > 60 and hls(g[0])[2] > 0.12 and hd(g[0], bg) < 30]
    second = (fam or [g[0] for g in G[1:] if g[0] not in (accent, text) and dist(g[0], bg) > 40] or [bg])[0]
    on_accent = (255, 255, 255) if contrast((255, 255, 255), accent) >= contrast((17, 17, 17), accent) else (17, 17, 17)
    muted = tuple(round(t * 0.62 + b * 0.38) for t, b in zip(text, bg))

    # độ đồng nhất: bao nhiêu ảnh chứa màu nhấn
    has = sum(1 for _, p in per if any(dist(c, accent) < 45 and w > 0.01 for c, w in p))
    avg_l = sum(hls(g[0])[1] * g[1] for g in G)
    avg_s = sum(hls(g[0])[2] * g[1] for g in G)

    L = [f"# Brand audit — trích xuất tự động ({datetime.date.today():%d.%m.%Y})", "",
         f"Nguồn: {len(per)} ảnh" + (f" · logo: `{os.path.basename(a.logo)}` (tính trọng số ×2)" if a.logo else ""), "",
         "> Gợi ý từ máy. Màu ảnh chụp lẫn màu người, ánh sáng, nén JPG → xem lại bằng mắt, ưu tiên mã màu gốc trong logo/guideline.", "",
         "## 1. Bảng màu chung (gộp các ảnh)", "", "| Màu | HEX | Tông | Diện tích | Xuất hiện ở | Sáng | Bão hòa |", "|---|---|---|---|---|---|---|"]
    for c, w, n in G[:12]:
        h, l, s = hls(c)
        L.append(f"| <span style=\"display:inline-block;width:28px;height:16px;background:{hexc(c)};border:1px solid #888\"></span> | `{hexc(c)}` | {name_tone(c)} | {w*100:.1f}% | {n} ảnh | {l:.2f} | {s:.2f} |")
    L += ["", "## 2. Vai trò gợi ý", "", "| Vai trò | HEX | Ghi chú |", "|---|---|---|",
          f"| Nền chính (60%) | `{hexc(bg)}` | {'nền tối' if dark_bg else 'nền sáng'} |",
          f"| Màu phụ (30%) | `{hexc(second)}` | thẻ, khối, nền phụ |",
          f"| Nhấn (10%) | `{hexc(accent)}` | màu bão hòa lặp lại nhiều nhất — CTA, từ khóa |",
          f"| Nhấn thay thế | {' '.join('`'+hexc(c)+'`' for c in acc_alts) or '—'} | các dải màu bão hòa lặp lại kế tiếp (có thể là màu da/ảnh — kiểm tra) |",
          f"| Màu trong logo | {' '.join('`'+hexc(c)+'`' for c in logo_cols) or '—'} | đối chiếu: nếu logo là màu nhận diện chính thì cân nhắc dùng làm nhấn |",
          f"| Chữ chính | `{hexc(text)}` | tương phản với nền {contrast(text, bg):.1f}:1 |",
          f"| Chữ phụ | `{hexc(muted)}` | tương phản {contrast(muted, bg):.1f}:1 {'(đạt)' if contrast(muted, bg) >= 4.5 else '(CHƯA ĐẠT 4.5 — chỉnh lại)'} |",
          f"| Chữ trên nút nhấn | `{hexc(on_accent)}` | tương phản {contrast(on_accent, accent):.1f}:1 |", "",
          "## 3. Tương phản các cặp chính", "", "| Cặp | Tỉ lệ | Thân chữ ≥4.5 | Chữ lớn ≥3 |", "|---|---|---|---|"]
    for nm, x, y in [("Chữ / nền", text, bg), ("Chữ phụ / nền", muted, bg), ("Nhấn / nền", accent, bg), ("Chữ nút / nhấn", on_accent, accent), ("Chữ / màu phụ", text, second)]:
        r = contrast(x, y)
        L.append(f"| {nm} | {r:.2f}:1 | {'✔' if r >= 4.5 else '✘'} | {'✔' if r >= 3 else '✘'} |")
    L += ["", "## 4. Nhận xét nhanh", "",
          f"- Tổng thể {'tối' if avg_l < 0.4 else 'sáng' if avg_l > 0.65 else 'trung bình'} (độ sáng TB {avg_l:.2f}), {'trầm' if avg_s < 0.25 else 'rực' if avg_s > 0.5 else 'vừa'} (bão hòa TB {avg_s:.2f}).",
          f"- Màu nhấn xuất hiện ở {has}/{len(per)} ảnh → {'nhận diện màu khá đồng nhất' if has >= 0.6 * len(per) else 'nhận diện màu CHƯA đồng nhất — cần chuẩn hóa'}.",
          f"- Số màu nổi (≥3% diện tích): {sum(1 for g in G if g[1] >= .03)} → {'gọn' if sum(1 for g in G if g[1] >= .03) <= 5 else 'nhiều màu, nên rút về 60–30–10'}.", "",
          "## 5. Màu theo từng ảnh", ""]
    for f, p in per:
        L.append(f"- `{os.path.basename(f)}`: " + " ".join(f"`{hexc(c)}` {w*100:.0f}%" for c, w in p[:6]))
    L += ["", "## 6. Nhận định (điền bằng mắt — xem references/xay-dung-brand-dna.md mục A3–A4)", "",
          "- Chữ (nhóm kiểu chữ, font gần nhất có tiếng Việt, số cỡ chữ đang dùng): [ ]",
          "- Logo (biến thể, vùng an toàn): [ ]", "- Bố cục lặp lại: [ ]", "- Hình ảnh: [ ]", "- Bất nhất cần xử lý: [ ]", "",
          "| Nhóm | Giữ | Chuẩn hóa | Bỏ |", "|---|---|---|---|", "| Màu | | | |", "| Chữ | | | |", "| Bố cục | | | |", "| Ảnh | | | |", ""]
    open(os.path.join(a.out, "brand-audit.md"), "w", encoding="utf8").write("\n".join(L))

    bg2 = tuple(min(255, round(v * 1.18 + 6)) for v in bg) if dark_bg else tuple(round(v * 0.96) for v in bg)
    surf = "rgba(255,255,255,.06)" if dark_bg else "#FFFFFF"
    T = f"""/* tokens GỢI Ý — sinh bởi scripts/trich_xuat_brand.py ({datetime.date.today():%d.%m.%Y}).
   Xem brand-audit.md, chỉnh bằng mắt, chọn font (references/xay-dung-brand-dna.md mục 3.3) rồi đổi tên thành tokens.css. */
@import url("https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,500;0,600;0,700;1,500&family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap");
:root{{
  --font-display:"Noto Serif",Georgia,serif;
  --font-body:"Be Vietnam Pro",system-ui,sans-serif;
  --bg:linear-gradient(170deg,{hexc(bg)} 0%,{hexc(bg2)} 100%);
  --bg-solid:{hexc(bg)};
  --bg-glow:radial-gradient(ellipse 900px 600px at 85% 0%,rgba({accent[0]},{accent[1]},{accent[2]},.14),rgba({accent[0]},{accent[1]},{accent[2]},0) 70%);
  --text:{hexc(text)}; --text-strong:{"#FFFFFF" if dark_bg else "#0B0D12"}; --text-muted:{hexc(muted)}; --tagline:{hexc(accent)};
  --accent:{hexc(accent)}; --accent-soft:{hexc(accent)};
  --accent-text:linear-gradient(90deg,{hexc(accent)},{hexc(accent)});
  --accent-fill:{hexc(accent)};
  --on-accent:{hexc(on_accent)};
  --hairline:rgba({text[0]},{text[1]},{text[2]},.14);
  --surface:{surf}; --surface-strong:{surf}; --surface-border:rgba({text[0]},{text[1]},{text[2]},.12);
  --shadow:0 14px 34px rgba(0,0,0,{'.35' if dark_bg else '.10'});
  --overlay-rgb:{bg[0]},{bg[1]},{bg[2]};
  --radius:16px; --margin:64px;
  --c-phu:{hexc(second)}; /* màu phụ 30% */
}}
"""
    open(os.path.join(a.out, "tokens-goi-y.css"), "w", encoding="utf8").write(T)
    print(f"Đã phân tích {len(per)} ảnh → {os.path.join(a.out, 'brand-audit.md')} + tokens-goi-y.css")
    print(f"Nền {hexc(bg)} · chữ {hexc(text)} ({contrast(text, bg):.1f}:1) · nhấn {hexc(accent)} · phụ {hexc(second)}")


if __name__ == "__main__":
    main()
