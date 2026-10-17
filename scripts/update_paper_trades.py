#!/usr/bin/env python3
"""Update the Paper trading experiment page from Chase's cleaned export.

  copy /workspace/paper-trading/public/paper-trades.json -> data/paper-trades.json
  validate -> rebuild the site -> commit locally.

Refresh command (weekdays):  python3 scripts/update_paper_trades.py --push

Order: check export -> skip if older/unchanged -> refuse placeholder data -> validate ->
copy -> rebuild -> commit -> (with --push) push. Nothing is pushed on any failure.
Without --push it only commits locally. Exit codes: 0 updated or skipped, 1 failed/refused.
Never touches Pages settings or CNAME (it only stages the files listed in STAGE).
"""
import argparse, datetime, json, os, re, shutil, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(ROOT, "data", "paper-trades.json")
SRC = "/workspace/paper-trading/public/paper-trades.json"
BOOKS = ("atr", "x_buzz")
BAD_KEYS = re.compile(r"account|acct|iban|sort.?code|password|token|secret|ibkr|broker", re.I)
BAD_VAL = re.compile(r"\b[A-Z]{1,2}\d{6,9}\b|\b\d{8,}\b")   # account-number-like strings
def fail(m): sys.exit("VALIDATION FAILED: " + m)
def walk(x, path=""):
    if isinstance(x, dict):
        for k, v in x.items():
            if BAD_KEYS.search(k): fail(f"suspicious key {path}/{k}")
            walk(v, f"{path}/{k}")
    elif isinstance(x, list):
        for i, v in enumerate(x): walk(v, f"{path}[{i}]")
    elif isinstance(x, str) and BAD_VAL.search(x): fail(f"account-number-like value at {path}: {x[:40]}")
def validate(d):
    for k in ("as_of", "disclaimer") + BOOKS:
        if k not in d: fail("missing " + k)
    datetime.datetime.fromisoformat(d["as_of"])
    for k in BOOKS:
        b = d[k]
        for f in ("start_date", "start_cash", "cash", "open_positions", "closed_trades", "totals"):
            if f not in b: fail(f"{k}: missing {f}")
        datetime.date.fromisoformat(b["start_date"])
        t = b["totals"]
        if t["closed_count"] != len(b["closed_trades"]): fail(f"{k}: closed_count mismatch")
        if t["open_count"] != len(b["open_positions"]): fail(f"{k}: open_count mismatch")
        for c in b["closed_trades"]:
            for f in ("ticker", "entry_date", "entry_price", "exit_date", "exit_price", "units", "pnl_usd", "pnl_pct"):
                if f not in c: fail(f"{k}: closed trade missing {f}")
            if abs((c["exit_price"] - c["entry_price"]) * c["units"] - c["pnl_usd"]) > 0.05: fail(f"{k} {c['ticker']}: pnl does not match prices")
        for o in b["open_positions"]:
            for f in ("ticker", "entry_date", "entry_price", "units", "cost_basis"):
                if f not in o: fail(f"{k}: open position missing {f}")
        if abs(sum(c["pnl_usd"] for c in b["closed_trades"]) - t["realised_pnl_usd"]) > 0.05: fail(f"{k}: realised P&L does not match trades")
        if abs(t["realised_pnl_usd"] / b["start_cash"] * 100 - t["realised_pnl_pct"]) > 0.02: fail(f"{k}: realised % mismatch")
        if t["win_count"] != sum(c["pnl_usd"] > 0 for c in b["closed_trades"]): fail(f"{k}: win_count mismatch")
        if any(o.get("unrealised_pnl_usd") is not None for o in b["open_positions"]): print(f"note: {k} has unrealised P&L values; the page still does not show them")
    walk(d)
STAGE = ["data/paper-trades.json", "assets/search-index.json", "paper-trading.html", "sitemap.xml", "tools.html", "tools/garmin-insights/index.html"]
def placeholder(d):
    if d.get("placeholder"): return True
    txt = " ".join(str(d.get(k, "")) for k in ("disclaimer", "note", "notes")) + " " + " ".join(str(d[b].get(k, "")) for b in BOOKS if isinstance(d.get(b), dict) for k in ("name", "notes", "description"))
    return bool(re.search(r"placeholder|dummy|lorem|sample data|example data|mock", txt, re.I))
GH = shutil.which("gh") or "/usr/local/bin/gh"
# the repo's configured credential helper points at /usr/bin/gh, which is not where gh lives on the box: name the real path
CRED = ["-c", "credential.helper=", "-c", f"credential.helper=!{GH} auth git-credential"]
def run(*a): return subprocess.run(a, cwd=ROOT, check=True)
def git(*a): return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--src", default=SRC)
    ap.add_argument("--no-commit", action="store_true"); ap.add_argument("--push", action="store_true"); a = ap.parse_args()
    if not os.path.exists(a.src): fail("export not found: " + a.src)
    try: d = json.load(open(a.src))
    except Exception as e: fail(f"export is not valid JSON: {e}")
    if placeholder(d): fail("export looks like placeholder data; refusing to publish")
    validate(d)
    old = open(DEST).read() if os.path.exists(DEST) else None
    if old is not None:
        o = json.loads(old)
        if datetime.datetime.fromisoformat(d["as_of"]) < datetime.datetime.fromisoformat(o["as_of"]):
            print(f"skip: export ({d['as_of']}) is older than the published data ({o['as_of']})"); return
        if o == d: print("skip: export is unchanged"); return
    shutil.copyfile(a.src, DEST)
    def restore():
        if old is not None: open(DEST, "w").write(old)
        else: os.remove(DEST)
    try:
        run(sys.executable, "scripts/build.py"); run(sys.executable, "scripts/garmin_chrome.py")
    except Exception:
        restore(); raise
    if a.no_commit: print("built; not committed"); return
    run("git", "add", *[f for f in STAGE if os.path.exists(os.path.join(ROOT, f))])
    if git("diff", "--cached", "--quiet").returncode == 0: print("no changes to commit"); return
    run("git", "-c", "user.name=Subhash Sharma", "-c", "user.email=334298032+subhashsharma-glitch@users.noreply.github.com",
        "commit", "-m", f"Paper trading: update export as of {d['as_of']}")
    print("committed locally.")
    if not a.push: print("not pushed (use --push)."); return
    if subprocess.run(["timeout", "90", "git", *CRED, "pull", "--rebase", "--autostash", "-q"], cwd=ROOT).returncode != 0: fail("could not sync with remote; commit kept locally, NOT pushed")
    if subprocess.run(["timeout", "90", "git", *CRED, "push", "-q"], cwd=ROOT).returncode != 0: fail("push failed; commit kept locally")
    print("pushed:", git("log", "--oneline", "-1").stdout.strip())
if __name__ == "__main__": main()
