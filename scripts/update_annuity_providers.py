#!/usr/bin/env python3
"""Refresh data/annuity-providers.json (per-provider £100,000 annuity figures) from the Which? annuity rates article.

Usage (from the repo root):
  python3 scripts/update_annuity_providers.py --dry-run   # fetch, parse, validate, print; writes nothing
  python3 scripts/update_annuity_providers.py             # update JSON (figures, quote date, checked date) and rebuild
  python3 scripts/update_annuity_providers.py --no-build  # update JSON only

Never invents values. Exits 1 and changes NOTHING if the page can't be fetched, the "correct at <date>" line or either
age table (65, 70) is missing, any of the three columns doesn't name the same providers, a figure is out of range, or the
date is older than the stored one. Which?'s ordering (highest first) is ignored: providers are stored and shown A to Z.
Does not commit or push.
"""
import html, json, re, subprocess, sys, datetime, urllib.request, os
URL = "https://www.which.co.uk/money/pensions-and-retirement/accessing-your-pensions/annuities/annuity-rates-aQGfH6W5n2rm"
DATA = "data/annuity-providers.json"
COLS = ["Single life, level", "Joint life (50%), level", "Joint life (50%), rising 3% a year"]
HEAD = "Single-life annuity Income Joint-life annuity (50%) Income Joint-life annuity plus 3% Income"
def fail(m): print("NO CHANGE:", m); sys.exit(1)
def main():
    dry = "--dry-run" in sys.argv; nobuild = "--no-build" in sys.argv
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    d = json.load(open(DATA)); known = set(d["scenarios"]["65"]["Single life, level"])
    try:
        raw = urllib.request.urlopen(urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/130 Safari/537.36"}), timeout=30).read().decode("utf-8", "ignore")
    except Exception as e: fail(f"could not fetch {URL}: {e}")
    raw = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", raw, flags=re.S)
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", raw)))
    names = "|".join(re.escape(n) for n in sorted(known, key=len, reverse=True))
    out, dates = {}, set()
    for age in ("65", "70"):
        i = t.find(f"Annuity rates for a {age}-year-old")
        if i < 0: fail(f"age {age} table heading not found")
        j = t.find(HEAD, i)
        if j < 0 or j - i > 300: fail(f"age {age} column headings changed")
        k = t.find("Source:", j)
        if k < 0: fail(f"age {age} source line not found")
        m = re.match(r"Source: Money ?Helper annuity calculator ?, correct at (\d{1,2} [A-Z][a-z]+ \d{4})", t[k:k+120])
        if not m: fail(f"age {age} source/date line changed: {t[k:k+120]!r}")
        dates.add(m.group(1))
        cells = re.findall(rf"({names}) £([\d,]+)", t[j+len(HEAD):k])
        if len(cells) != 3 * len(known): fail(f"age {age}: expected {3*len(known)} provider figures, found {len(cells)}")
        cols = [dict() for _ in COLS]
        for n, (prov, v) in enumerate(cells):
            col = cols[n % 3]
            if prov in col: fail(f"age {age}: {prov} appears twice in one column")
            v = int(v.replace(",", ""))
            if not 2000 <= v <= 20000: fail(f"age {age}: figure out of range {prov} £{v}")
            col[prov] = v
        for c, col in zip(COLS, cols):
            if set(col) != known: fail(f"age {age} '{c}': providers {sorted(col)} differ from {sorted(known)}")
        out[age] = {c: dict(sorted(col.items())) for c, col in zip(COLS, cols)}  # A to Z, Which? order ignored
    if len(dates) != 1: fail(f"tables carry different dates {dates}")
    try: qd = datetime.datetime.strptime(dates.pop(), "%d %B %Y").date().isoformat()
    except ValueError: fail("unreadable date")
    if qd < d["quotes_dated"]: fail(f"page date {qd} older than stored {d['quotes_dated']}")
    print("quotes dated", qd, "| previous", d["quotes_dated"], "| figures changed:", out != d["scenarios"])
    for a, sc in out.items():
        for c, col in sc.items(): print(f"  {a} {c}: {col}")
    if dry: print("dry run: nothing written"); return
    d["scenarios"] = out; d["quotes_dated"] = qd; d["checked"] = datetime.date.today().isoformat()
    tmp = DATA + ".tmp"; json.dump(d, open(tmp, "w"), indent=1, ensure_ascii=False); os.replace(tmp, DATA); print("wrote", DATA)
    if not nobuild:
        subprocess.run([sys.executable, "scripts/build.py"], check=True)
        subprocess.run([sys.executable, "scripts/garmin_chrome.py"], check=True)
main()
