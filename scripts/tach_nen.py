# -*- coding: utf-8 -*-
"""Tách nền ảnh bằng rembg (offline sau lần tải model đầu). Dùng:
  python tach_nen.py VAO.jpg RA.png [--model u2net|isnet-general-use|u2net_human_seg] [--alpha-matting]
"""
import argparse
from PIL import Image
from rembg import remove, new_session

ap = argparse.ArgumentParser()
ap.add_argument("inp"); ap.add_argument("out")
ap.add_argument("--model", default="u2net_human_seg")
ap.add_argument("--alpha-matting", action="store_true")
a = ap.parse_args()
img = Image.open(a.inp).convert("RGB")
res = remove(img, session=new_session(a.model), alpha_matting=a.alpha_matting)
res.convert("RGBA").save(a.out)
print("OK ->", a.out)
