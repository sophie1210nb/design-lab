# -*- coding: utf-8 -*-
"""Cài brand pack riêng hoặc gói ảnh của một thương hiệu vào brands/<tên>/.

Brand pack riêng (logo, ảnh, quy tắc nội bộ) KHÔNG nằm trong repo công khai: mỗi đội giữ pack
ở kho nội bộ dưới dạng file .zip (hoặc một thư mục) và cài bằng script này.

Dùng:
    python scripts/nap_tu_lieu.py --brand <tên> "<file .zip hoặc thư mục>"
    vd: python scripts/nap_tu_lieu.py --brand cafe-may "~/Downloads/cafe-may-brand-pack.zip"

Script tự nhận dạng nguồn:
  * BRAND PACK — có brand.md ở gốc, trong <x>/brand.md hoặc brands/<x>/brand.md:
      cài TOÀN BỘ pack (brand.md, tokens.css, assets/, templates/, …) vào brands/<tên>/,
      gộp vào pack đang có và ghi đè file trùng tên.
  * GÓI ẢNH — không có brand.md:
      chép ảnh (jpg/jpeg/png/webp, giữ thư mục con như clean/) vào brands/<tên>/assets/anh-that/.
Sau khi cài: dò mọi mẫu trong brands/<tên>/templates/ và báo ảnh/tệp còn thiếu.

brands/* (trừ brands/_mau/) đã được .gitignore — pack riêng không bao giờ bị commit lên repo.
"""
import argparse, os, re, shutil, sys, tempfile, zipfile
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_EXT = (".jpg", ".jpeg", ".png", ".webp")
BO_QUA = {"__MACOSX", ".git", "output", "__pycache__", ".DS_Store", "Thumbs.db"}


def giai_nen(path):
    tmp = tempfile.mkdtemp(prefix="nap-tu-lieu-")
    with zipfile.ZipFile(path) as z:
        for info in z.infolist():
            # tên file tiếng Việt trong zip tạo trên Windows có thể không bật cờ UTF-8
            name = info.filename
            if not (info.flag_bits & 0x800):
                try:
                    name = name.encode("cp437").decode("utf8")
                except (UnicodeEncodeError, UnicodeDecodeError):
                    pass
            name = name.replace("\\", "/")
            if name.startswith("/") or ".." in name.split("/"):
                continue  # chặn đường dẫn thoát ra ngoài
            out = os.path.join(tmp, *name.split("/"))
            if name.endswith("/"):
                os.makedirs(out, exist_ok=True)
                continue
            os.makedirs(os.path.dirname(out), exist_ok=True)
            with z.open(info) as fi, open(out, "wb") as fo:
                shutil.copyfileobj(fi, fo)
    return tmp


def tim_brand_pack(src):
    """Trả về thư mục chứa brand.md (gốc, <x>/, brands/<x>/) hoặc None."""
    if os.path.isfile(os.path.join(src, "brand.md")):
        return src
    cands = []
    for d in sorted(os.listdir(src)):
        p = os.path.join(src, d)
        if d in BO_QUA or not os.path.isdir(p):
            continue
        if os.path.isfile(os.path.join(p, "brand.md")):
            cands.append(p)
        elif d == "brands":
            for x in sorted(os.listdir(p)):
                if os.path.isfile(os.path.join(p, x, "brand.md")) and x != "_mau":
                    cands.append(os.path.join(p, x))
    if len(cands) > 1:
        print("Cảnh báo: nguồn có nhiều brand pack, chỉ cài pack đầu tiên: " + os.path.basename(cands[0]))
    return cands[0] if cands else None


def chep_cay(src, dst, chi_anh=False):
    n = 0
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in BO_QUA]
        for f in files:
            if f in BO_QUA or (chi_anh and not f.lower().endswith(IMG_EXT)):
                continue
            rel = os.path.relpath(os.path.join(root, f), src)
            out = os.path.join(dst, rel)
            os.makedirs(os.path.dirname(out), exist_ok=True)
            shutil.copy2(os.path.join(root, f), out)
            n += 1
    return n


def kiem_tra_mau(brand_dir, ten):
    """Dò tham chiếu ảnh/tệp tương đối trong templates/*.html và *.css, báo tệp còn thiếu."""
    tdir = os.path.join(brand_dir, "templates")
    if not os.path.isdir(tdir):
        print("Pack chưa có thư mục templates/ — bỏ qua bước kiểm tra mẫu.")
        return
    pat = re.compile(r"""(?:src|href)\s*=\s*["']([^"']+)["']|url\(\s*["']?([^"')]+)["']?\s*\)""", re.I)
    need = {}
    for f in sorted(os.listdir(tdir)):
        if not f.lower().endswith((".html", ".css")):
            continue
        s = open(os.path.join(tdir, f), encoding="utf8", errors="replace").read()
        s = re.sub(r"<!--.*?-->", "", s, flags=re.S)  # bỏ chú thích (thường chứa ví dụ <ảnh>)
        for m in pat.finditer(s):
            ref = unquote((m.group(1) or m.group(2) or "").strip())
            if not ref or re.match(r"^(https?:|data:|#|mailto:|//)", ref, re.I) or "<" in ref or "{" in ref:
                continue
            ref = ref.split("#")[0].split("?")[0]
            if not ref:
                continue
            need.setdefault(ref, set()).add(f)
    miss = {}
    for ref, users in need.items():
        if not os.path.exists(os.path.normpath(os.path.join(tdir, ref))):
            miss[ref] = users
    anh = [r for r in need if "anh-that/" in r]
    if miss:
        print(f"Mẫu của {ten} còn thiếu {len(miss)} tệp (bổ sung vào gói rồi chạy lại):")
        for k, v in sorted(miss.items()):
            print(f"  - {k}  ← dùng trong {', '.join(sorted(v))}")
    else:
        print(f"Đủ tệp cho {len(need)} tham chiếu trong các mẫu {ten} "
              f"(gồm {len(anh)} ảnh thật). Có thể thiết kế ngay.")


def main():
    ap = argparse.ArgumentParser(description="Cài brand pack riêng hoặc gói ảnh vào brands/<tên>/")
    ap.add_argument("--brand", required=True, help="tên thư mục trong brands/ (chữ thường, không dấu, gạch ngang)")
    ap.add_argument("nguon", help="file .zip hoặc thư mục: brand pack (có brand.md) hoặc gói ảnh")
    a = ap.parse_args()

    if a.brand in ("", ".", "..", "_mau") or re.search(r"[\\/]", a.brand):
        sys.exit("Tên brand không hợp lệ (không dùng _mau, không chứa / hoặc \\).")
    brand_dir = os.path.join(ROOT, "brands", a.brand)

    src = os.path.expanduser(a.nguon)
    tmp = None
    if os.path.isfile(src) and src.lower().endswith(".zip"):
        tmp = giai_nen(src)
        src = tmp
    if not os.path.isdir(src):
        sys.exit(f"Không đọc được nguồn: {a.nguon}")

    try:
        pack = tim_brand_pack(src)
        if pack:
            moi = not os.path.isdir(brand_dir)
            n = chep_cay(pack, brand_dir)
            os.makedirs(os.path.join(brand_dir, "assets", "anh-that"), exist_ok=True)
            print(f"Đã {'cài' if moi else 'cập nhật'} brand pack vào brands/{a.brand}/ ({n} tệp, ghi đè tệp trùng tên).")
            for p in ("brand.md", "tokens.css", "assets", "templates"):
                print(f"  {'có ' if os.path.exists(os.path.join(brand_dir, p)) else 'THIẾU'}  {p}")
        else:
            if not os.path.isdir(brand_dir):
                print(f"Chưa có brands/{a.brand}/ — tạo mới (chỉ có ảnh; nên tạo brand.md theo references/tao-brand-moi.md).")
            dst = os.path.join(brand_dir, "assets", "anh-that")
            os.makedirs(dst, exist_ok=True)
            img_src = src
            for cand in ("anh-that", os.path.join("assets", "anh-that")):
                if os.path.isdir(os.path.join(src, cand)):
                    img_src = os.path.join(src, cand)
                    break
            n = chep_cay(img_src, dst, chi_anh=True)
            print(f"Gói ảnh: đã nạp {n} ảnh vào brands/{a.brand}/assets/anh-that/")
    finally:
        if tmp:
            shutil.rmtree(tmp, ignore_errors=True)

    kiem_tra_mau(brand_dir, a.brand)


if __name__ == "__main__":
    main()
