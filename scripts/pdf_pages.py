#!/usr/bin/env python3
"""Render assets/explained-simply-money-matters.pdf to assets/explained-simply/page-NN.webp (the in-page View).
Re-run this whenever the PDF changes:  python3 scripts/pdf_pages.py   (needs poppler-utils and Pillow)."""
import glob, os, subprocess, tempfile
from PIL import Image
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = f"{R}/assets/explained-simply-money-matters.pdf"; OUT = f"{R}/assets/explained-simply"
os.makedirs(OUT, exist_ok=True)
for f in glob.glob(f"{OUT}/page-*.webp"): os.remove(f)
with tempfile.TemporaryDirectory() as t:
    subprocess.run(["pdftoppm", "-r", "100", "-png", PDF, f"{t}/p"], check=True)
    for i, f in enumerate(sorted(glob.glob(f"{t}/p-*.png")), 1):
        im = Image.open(f).convert("RGB"); im.save(f"{OUT}/page-{i:02d}.webp", "WEBP", quality=80, method=6)
        print(i, im.size)
