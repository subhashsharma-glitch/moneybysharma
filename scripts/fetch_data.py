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
