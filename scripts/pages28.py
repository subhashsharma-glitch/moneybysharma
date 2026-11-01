# Home page: move the "Today's key numbers" section so it sits before the Budget 2026 banner (Subhash, 1 Nov 2026).
import re as _re28
_h = pages["index.html"]
_m = _re28.search(r'<section class="numbers" aria-labelledby="kn">.*?</section>', _h, flags=_re28.S)
assert _m and _h.count('<section class="numbers"') == 1, "key numbers section not found"
_sec = _m.group(0); _h = _h[:_m.start()] + _h[_m.end():]
_b = '<style>\n.b26-banner{'
assert _h.count(_b) == 1, "Budget 2026 banner not found"
pages["index.html"] = _h.replace(_b, _sec + _b)
