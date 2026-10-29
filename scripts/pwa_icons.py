#!/usr/bin/env python3
"""Generate the PWA / home-screen icons from the brand logo (white M, orange dot, dark teal #0f4c45).
Run once (or after a logo change): python3 scripts/pwa_icons.py. Writes assets/icons/*.png. Not run by build.py."""
from PIL import Image, ImageDraw
TEAL, ORANGE, WHITE = (15, 76, 69, 255), (217, 130, 43, 255), (255, 255, 255, 255)
def draw_mark(d, ox, oy, s):  # logo drawn in a 32-unit box at (ox, oy), scale s px/unit
    P = lambda x, y: (ox + x * s, oy + y * s)
    pts = [P(8, 22), P(8, 11), P(16, 18), P(24, 11), P(24, 22)]
    w = 2.6 * s
    d.line(pts, fill=WHITE, width=round(w), joint="curve")
    for p in pts: d.ellipse([p[0] - w / 2, p[1] - w / 2, p[0] + w / 2, p[1] + w / 2], fill=WHITE)
    c, r = P(24, 8), 2.6 * s
    d.ellipse([c[0] - r, c[1] - r, c[0] + r, c[1] + r], fill=ORANGE)
def icon(size, kind):
    k = 4; S = size * k
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    if kind == "any":        # rounded tile like the favicon
        d.rounded_rectangle([0, 0, S - 1, S - 1], radius=S * 8 / 32, fill=TEAL); draw_mark(d, 0, 0, S / 32)
    elif kind == "maskable": # full-bleed teal; mark inside the central 60% so it survives any mask (safe zone = 80% circle)
        d.rectangle([0, 0, S, S], fill=TEAL); m = S * 0.6; draw_mark(d, (S - m) / 2, (S - m) / 2 + S * 0.02, m / 32)
    else:                    # apple: full square (iOS rounds the corners), mark at 80%
        d.rectangle([0, 0, S, S], fill=TEAL); m = S * 0.8; draw_mark(d, (S - m) / 2, (S - m) / 2, m / 32)
    return im.resize((size, size), Image.LANCZOS)
if __name__ == "__main__":
    for name, size, kind in [("icon-192.png", 192, "any"), ("icon-512.png", 512, "any"), ("icon-maskable-512.png", 512, "maskable"),
                             ("apple-touch-icon.png", 180, "apple")]:
        im = icon(size, kind)
        if kind != "any": im = im.convert("RGB")
        im.save("assets/icons/" + name, optimize=True); print("wrote assets/icons/" + name)
