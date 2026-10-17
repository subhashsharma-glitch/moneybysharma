#!/usr/bin/env python3
"""Re-check data/deals.json against the retailers' own pages (used by the twice-weekly deals refresh).

What it does
  --check (default)  Fetch each entry's primary official URL. For entries with check.mode == "auto" it confirms the page still
                     contains every string in check.expect (the exact phrases/prices the entry is based on). Prints a report;
                     changes nothing. Exit code 1 if any auto entry failed.
  --apply            Also write data/deals.json: entries that pass get checked = today; entries that fail get status = "review"
                     (the page then shows only a link, no figures) with a reviewNote saying what to look at. Never edits prices.
  --prune            Remove entries / points / offers whose 'until'/'expires' date has passed (the page build also hides these).
  --json             Print the report as JSON (for an agent to read).
Entries with check.mode == "manual" (sites that block automated fetches: Tesco, Aldi, Asda, Odeon, Vue, Boots, Superdrug, Argos,
Too Good To Go ...) are listed under "needs agent/manual check": open the official page in a real browser or via web search, update the
figures in data/deals.json by hand from what the page says, set checked to the date you looked, then run build.py.
Rules: only retailer-owned pages; no promo codes; no third-party price sites; if a figure can't be confirmed, delete it or set status to
"link-only". After editing run `python3 scripts/build.py` and the site checks before publishing.
"""
import argparse, datetime, html, json, os, re, sys, time, urllib.request, urllib.error
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "data", "deals.json")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36 MoneyBySharma-deals-check"
BLOCK = re.compile(r"access denied|just a moment|pardon our interruption|security checkpoint|verifying your browser|are you a robot|captcha", re.I)
def norm(s):
    s = html.unescape(re.sub(r"(?s)<(script|style|svg|noscript).*?</\1>", " ", s)); s = re.sub(r"<[^>]+>", " ", s)
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"').replace("\u00a0", " ")
    return re.sub(r"\s+", " ", s).strip()
def fetch(url, tries=2):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-GB,en;q=0.9", "Accept": "text/html,*/*"})
            with urllib.request.urlopen(req, timeout=25) as r: return r.status, r.read().decode("utf-8", "ignore"), r.geturl()
        except urllib.error.HTTPError as e: last = (e.code, "", url)
        except Exception as e: last = (0, "", url); time.sleep(1)
    return last
def entries(d):
    for g in d["groups"]:
        for e in g["entries"]: yield g, e
def check_one(e):
    c = e.get("check", {}); url = c.get("url") or e["links"][0][1]
    st, body, final = fetch(url); t = norm(body)
    res = {"id": e["id"], "name": e["name"], "url": url, "status": st, "mode": c.get("mode", "manual")}
    if st != 200 or BLOCK.search(t[:600]) or len(t) < 200:
        res["result"] = "blocked-or-unreachable"; return res
    if c.get("mode") != "auto": res["result"] = "reachable (manual content check)"; return res
    missing = [s for s in c.get("expect", []) if norm(s) not in t]
    res["result"] = "ok" if not missing and c.get("expect") else ("no expectations set" if not c.get("expect") else "CHANGED"); res["missing"] = missing
    return res
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); ap.add_argument("--prune", action="store_true"); ap.add_argument("--json", action="store_true")
    ap.add_argument("--only", help="entry id"); a = ap.parse_args()
    d = json.load(open(PATH)); today = datetime.date.today().isoformat(); out = []
    for g, e in entries(d):
        if a.only and e["id"] != a.only: continue
        if e.get("expires") and e["expires"] < today: out.append({"id": e["id"], "name": e["name"], "result": "expired"}); continue
        r = check_one(e); out.append(r); time.sleep(0.7)
        if a.apply:
            if r["result"] == "ok": e["checked"] = today; e["status"] = "ok" if e.get("status") != "link-only" else "link-only"; e.pop("reviewNote", None)
            elif r["result"] == "CHANGED": e["status"] = "review"; e["reviewNote"] = "Page no longer contains: " + "; ".join(r["missing"])
    if a.prune:
        for g in d["groups"]:
            g["entries"] = [e for e in g["entries"] if not (e.get("expires") and e["expires"] < today)]
            for e in g["entries"]:
                for k in ("points", "offers"):
                    if k in e: e[k] = [p for p in e[k] if not (isinstance(p, dict) and p.get("until") and p["until"] < today)]
    if a.apply or a.prune:
        d["updated"] = today
        json.dump(d, open(PATH + ".tmp", "w"), indent=1, ensure_ascii=False); os.replace(PATH + ".tmp", PATH)
    if a.json: print(json.dumps(out, indent=1)); 
    else:
        for r in out: print(f'{r["result"]:34} {r["id"]:22} {r.get("status","")} {r.get("url","")}' + (f'  MISSING: {r["missing"]}' if r.get("missing") else ""))
        manual = [r["id"] for r in out if r["mode"] != "auto" and r["result"] != "expired"] if out and "mode" in out[0] else []
        print(f'\n{len(out)} entries checked. Needs agent/manual check ({len(manual)}): ' + ", ".join(manual))
    sys.exit(1 if any(r["result"] == "CHANGED" for r in out) else 0)
if __name__ == "__main__": main()
