#!/usr/bin/env python3
"""Weekly refresh of data/annuity-rates.json from Hargreaves Lansdown's published annuity rate table.

Usage (from the repo root):
  python3 scripts/update_annuity_rates.py            # fetch, validate, update JSON, rebuild
  python3 scripts/update_annuity_rates.py --dry-run  # fetch and validate only; print what would change
  python3 scripts/update_annuity_rates.py --no-build # update JSON but don't rebuild

Never invents values. If the page can't be fetched, the table/date can't be found, any of the six rows is missing,
the age columns differ, or any figure is outside a sane range, it prints why, exits 1 and changes NOTHING.
It does not commit or push; review `git diff` and commit as usual.
"""
import html, json, re, subprocess, sys, datetime, urllib.request, os
URL = "https://www.hl.co.uk/retirement/annuities/best-buy-rates"
DATA = "data/annuity-rates.json"
ROWS = {  # label on HL's page -> key used by the calculator
 "Single life, level, no guarantee": "single|level|0",
 "Single life, level, 5 year guarantee": "single|level|5",
 "Single life, RPI, 5 year guarantee": "single|rpi|5",
 "Single life, 3% escalation, 5 year guarantee": "single|3pc|5",
 "Joint life 50%, level, no guarantee": "joint|level|0",
 "Joint life 50%, 3% escalation, no guarantee": "joint|3pc|0",
}
HEADER = "Annuity type Age 55 Age 60 Age 65 Age 65 (smoker*) Age 70 Age 75"
def fail(msg): print("NO CHANGE:", msg); sys.exit(1)
def main():
    dry = "--dry-run" in sys.argv; nobuild = "--no-build" in sys.argv
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    try:
        req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/130 Safari/537.36"})
        raw = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
    except Exception as e: fail(f"could not fetch {URL}: {e}")
    raw = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", raw, flags=re.S)
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", raw)))
    m = re.search(r"This week's best annuity rates \((\d{1,2} [A-Z][a-z]+ \d{4})\)", t)
    if not m: fail("quote date heading not found")
    try: qdate = datetime.datetime.strptime(m.group(1), "%d %B %Y").date()
    except ValueError: fail(f"unreadable quote date {m.group(1)!r}")
    seg = t[m.end(): m.end() + 3000]
    if HEADER not in seg: fail("age column header changed: " + seg[:200])
    rates, smoker = {}, None
    for label, key in ROWS.items():
        r = re.search(re.escape(label) + r"((?: £[\d,]+){6})", seg)
        if not r: fail(f"row not found or not 6 figures: {label}")
        v = [int(x.replace(",", "")) for x in re.findall(r"£([\d,]+)", r.group(1))]
        if any(not 1000 <= x <= 30000 for x in v): fail(f"figure out of range in {label}: {v}")
        rates[key] = [v[0], v[1], v[2], v[4], v[5]]  # drop the age-65 smoker column
        if key == "single|level|0": smoker = v[3]
    d = json.load(open(DATA))
    old = (d.get("quotes_dated"), d.get("rates"))
    if qdate.isoformat() < (d.get("quotes_dated") or ""): fail(f"page date {qdate} is older than stored {d['quotes_dated']}")
    d["rates"] = rates; d["quotes_dated"] = qdate.isoformat(); d["checked"] = datetime.date.today().isoformat()
    d["smoker_example"]["standard"] = rates["single|level|0"][2]; d["smoker_example"]["smoker"] = smoker
    print("quotes dated", qdate, "| changed figures:", old[1] != rates, "| previous date:", old[0])
    for k, v in rates.items(): print(f"  {k:15} {v}")
    if dry: print("dry run: nothing written"); return
    tmp = DATA + ".tmp"; json.dump(d, open(tmp, "w"), indent=1, ensure_ascii=False); os.replace(tmp, DATA)
    print("wrote", DATA)
    if not nobuild:
        subprocess.run([sys.executable, "scripts/build.py"], check=True)
        subprocess.run([sys.executable, "scripts/garmin_chrome.py"], check=True)
main()
