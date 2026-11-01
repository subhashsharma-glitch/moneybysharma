#!/usr/bin/env python3
"""Build static postcode shards for the Broadband & phones postcode checker from Ofcom Connected Nations open data
(Open Government Licence). Not run by build.py: run by hand when Ofcom publishes a new release.

  python3 scripts/build_broadband_data.py /path/to/unzipped/ofcom/fixed /path/to/unzipped/ofcom/mobile

Writes data/broadband/pc/<DISTRICT>.json (one per postcode district, e.g. YO1.json) and data/broadband/meta.json
(release date, laua mobile coverage). Values are Ofcom's own percentages, unchanged (rounded to 1 dp)."""
import csv, glob, json, os, sys, re, shutil
FIX, MOB = sys.argv[1], sys.argv[2]
OUT = "data/broadband"
RELEASE = {"name": "Connected Nations update: Spring 2026", "dataDate": "January 2026",
           "url": "https://www.ofcom.org.uk/phones-and-broadband/coverage-and-speeds/connected-nations-update-spring-2026",
           "checked": "2026-11-01"}
# Fields kept, in order (short keys used by the page script)
COLS = [("b0", "% of premises with 0<2Mbit/s download speed"), ("b2", "% of premises with 2<5Mbit/s download speed"),
        ("b5", "% of premises with 5<10Mbit/s download speed"), ("b10", "% of premises with 10<30Mbit/s download speed"),
        ("b30", "% of premises with 30<300Mbit/s download speed"), ("b300", "% of premises with >=300Mbit/s download speed"),
        ("sf", "SFBB availability (% premises)"), ("uf100", "UFBB (100Mbit/s) availability (% premises)"),
        ("uf", "UFBB availability (% premises)"), ("gig", "Gigabit availability (% premises)"),
        ("nodec", "% of premises unable to receive decent broadband from fixed or FWA"),
        ("nga", "% of premises with NGA"), ("fwa", "% of premises able to receive decent broadband from FWA")]
def num(x):
    x = (x or "").strip()
    if x == "": return None
    v = round(float(x), 1); return int(v) if v == int(v) else v
files = sorted(glob.glob(os.path.join(FIX, "**", "*_pc_coverage_r2_*.csv"), recursive=True))
assert len(files) == 121, f"expected 121 all-premises postcode files, found {len(files)}"
shards = {}
for f in files:
    with open(f, newline="", encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            pc = r["postcode_space"].strip().upper()
            if " " not in pc: continue
            dist, inward = pc.split(" ", 1)
            sh = shards.setdefault(dist, {"vals": {}, "p": {}})
            vals = tuple(num(r[c]) for _, c in COLS)
            idx = sh["vals"].setdefault(vals, len(sh["vals"]))
            sh["p"][inward] = idx
if os.path.isdir(OUT + "/pc"): shutil.rmtree(OUT + "/pc")
os.makedirs(OUT + "/pc")
for dist, sh in shards.items():
    assert re.fullmatch(r"[A-Z0-9]{2,4}", dist), dist
    v = [list(t) for t, _ in sorted(sh["vals"].items(), key=lambda kv: kv[1])]
    json.dump({"v": v, "p": sh["p"]}, open(f"{OUT}/pc/{dist}.json", "w"), separators=(",", ":"))
# Mobile: Ofcom publishes mobile coverage down to local authority only (not postcode, not per operator below UK/nation level).
mf = glob.glob(os.path.join(MOB, "**", "*_mobile_coverage_laua_r01.csv"), recursive=True)[0]
mob = {}
for r in csv.DictReader(open(mf, newline="", encoding="utf-8-sig")):
    g = lambda k: num(r.get(k))
    mob[r["laua"]] = {"n": r["laua_name"],
        "in4g_any": None if g("4G_prem_in_0") is None and g("4G_prem_in_4") is None else round(100 - (g("4G_prem_in_0") or 0), 1),
        "in4g_all": g("4G_prem_in_4") or 0,
        "out4g_any": round(100 - (g("4G_prem_out_0") or 0), 1), "out4g_all": g("4G_prem_out_4") or 0,
        "out5g_any": round(100 - (g("5G_high_confidence_prem_out_0") or 0), 1)}
json.dump({"release": RELEASE, "cols": [k for k, _ in COLS], "mobileLaua": mob}, open(f"{OUT}/meta.json", "w"), separators=(",", ":"))
tot = sum(os.path.getsize(f"{OUT}/pc/{d}.json") for d in shards)
print(f"{len(shards)} district shards, {sum(len(s['p']) for s in shards.values())} postcodes, {tot/1e6:.1f} MB; "
      f"largest {max(os.path.getsize(f'{OUT}/pc/{d}.json') for d in shards)/1e3:.0f} KB; meta {os.path.getsize(OUT+'/meta.json')/1e3:.0f} KB")
