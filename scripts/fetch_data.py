#!/usr/bin/env python3
"""Build-time data fetch: Bank of England Bank Rate + UK DMO gilts in issue. Writes data/*.json."""
import json, re, urllib.request, datetime, xml.etree.ElementTree as ET
UA = {"User-Agent": "Mozilla/5.0 (MoneyBySharma build)"}
def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30).read().decode("utf-8", "replace")
today = datetime.date.today().isoformat()
# Bank Rate (series IUDBEDR)
boe_url = ("https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp?csv.x=yes&SeriesCodes=IUDBEDR"
           "&UsingCodes=Y&CSVF=TN&Datefrom=01/Jan/2024&Dateto=now")
rows = [l.split(",") for l in get(boe_url).strip().splitlines()[1:] if "," in l]
rate = float(rows[-1][1]); changed = rows[-1][0]
for d, v in reversed(rows):
    if float(v) != rate: break
    changed = d
br = {"rate": rate, "asAt": datetime.datetime.strptime(rows[-1][0], "%d %b %Y").date().isoformat(),
      "since": datetime.datetime.strptime(changed, "%d %b %Y").date().isoformat(),
      "source": "Bank of England Database, series IUDBEDR (Official Bank Rate)",
      "sourceUrl": "https://www.bankofengland.co.uk/monetary-policy/the-interest-rate-bank-rate", "fetched": today}
json.dump(br, open("data/bank-rate.json", "w"), indent=2)
# DMO gilts in issue (report D1A)
xml = get("https://www.dmo.gov.uk/data/XmlDataReport?reportCode=D1A").strip()
root = ET.fromstring(xml)
FR = {"¼": .25, "½": .5, "¾": .75, "⅛": .125, "⅜": .375, "⅝": .625, "⅞": .875}
def coupon(name):
    m = re.match(r"\s*([\d]*)\s*([¼½¾⅛⅜⅝⅞])?\s*(\d+/\d+)?\s*%", name)
    if not m: return None
    c = float(m.group(1) or 0) + FR.get(m.group(2) or "", 0)
    if m.group(3): a, b = m.group(3).split("/"); c += int(a) / int(b)
    return round(c, 4)
gilts, cob = [], None
for e in root:
    a = e.attrib
    if a.get("INSTRUMENT_TYPE", "").strip() != "Conventional": continue
    cob = a["CLOSE_OF_BUSINESS_DATE"][:10]
    gilts.append({"name": a["INSTRUMENT_NAME"].strip(), "isin": a["ISIN_CODE"], "coupon": coupon(a["INSTRUMENT_NAME"]),
                  "maturity": a["REDEMPTION_DATE"][:10], "dividendDates": a.get("DIVIDEND_DATES", "")})
gilts.sort(key=lambda g: g["maturity"])
json.dump({"source": "UK Debt Management Office – Gilts in Issue (report D1A)",
           "sourceUrl": "https://www.dmo.gov.uk/data/gilt-market/gilts-in-issue/",
           "closeOfBusiness": cob, "fetched": today,
           "note": "Reference data only (name, coupon, maturity). Prices are not included – enter a current price from your broker or the DMO.",
           "gilts": gilts}, open("data/gilts.json", "w"), indent=2, ensure_ascii=False)
print("bank rate", br, "gilts", len(gilts), "cob", cob)
# Total gilts in issue (all types, nominal incl. index-linked uplift), £ million, from the same D1A report
tot = sum(float(e.attrib.get("TOTAL_AMOUNT_INCLUDING_IL_UPLIFT", 0) or 0) for e in root)
conv = sum(float(e.attrib.get("TOTAL_AMOUNT_IN_ISSUE", 0) or 0) for e in root if e.attrib.get("INSTRUMENT_TYPE","").strip()=="Conventional")
g = json.load(open("data/gilts.json")); g["totalInIssueInclUpliftMillions"] = round(tot, 1); g["conventionalInIssueMillions"] = round(conv, 1)
json.dump(g, open("data/gilts.json", "w"), indent=2, ensure_ascii=False)
# ONS CPI annual rate (D7G7)
import csv, io
rows = list(csv.reader(io.StringIO(get("https://www.ons.gov.uk/generator?format=csv&uri=/economy/inflationandpriceindices/timeseries/d7g7/mm23"))))
meta = {r[0]: r[1] for r in rows[:8] if len(r) > 1}
annual = [{"year": int(r[0]), "rate": float(r[1])} for r in rows if len(r) > 1 and re.fullmatch(r"\d{4}", r[0])]
monthly = [{"period": r[0], "rate": float(r[1])} for r in rows if len(r) > 1 and re.fullmatch(r"\d{4} [A-Z]{3}", r[0])]
# Link to the ONS consumer price inflation bulletin for the latest month, e.g. .../consumerpriceinflation/september2026.
# Checked with a request; if it can't be confirmed, keep the existing bulletinUrl only when it is for the same month.
_y, _m = monthly[-1]["period"].split()
_mn = datetime.datetime.strptime(_m.title(), "%b").strftime("%B").lower()
_bul = f"https://www.ons.gov.uk/economy/inflationandpriceindices/bulletins/consumerpriceinflation/{_mn}{_y}"
try:
    get(_bul)
except Exception:
    try:
        _old = json.load(open("data/cpi.json")).get("bulletinUrl")
    except Exception:
        _old = None
    _bul = _old if _old and _old.endswith(f"/{_mn}{_y}") else None
json.dump({"source": "ONS – CPI annual rate 00: all items (series D7G7, dataset MM23)",
           "sourceUrl": "https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/d7g7/mm23",
           "released": meta.get("Release date"), "nextRelease": meta.get("Next release"), "fetched": today,
           "annual": annual, "latestMonth": monthly[-1], "peakMonth": max(monthly, key=lambda m: m["rate"]),
           **({"bulletinUrl": _bul} if _bul else {})},
          open("data/cpi.json", "w"), indent=2)
print("gilts total £m", tot, "cpi annual", annual[0], annual[-1], monthly[-1])
