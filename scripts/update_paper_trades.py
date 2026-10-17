#!/usr/bin/env python3
"""Update the Paper trading experiment page from Chase's cleaned export.

Refresh command (weekdays):  python3 scripts/update_paper_trades.py --push

SAFE BY DESIGN (rewritten 17 Oct 2026): the site is NOT built from your working tree.
  1. fetch origin, check out a throwaway worktree of origin/main (the published site)
  2. validate the export and copy it into that worktree's data/paper-trades.json
  3. rebuild the site INSIDE the worktree, so unpublished previews and uncommitted edits are never built
  4. refuse unless every changed file is in STAGE, no new files appear, and every internal link and anchor
     in the changed files resolves to a page that already exists on origin/main
  5. commit in the worktree; with --push push that commit to origin main (never forced)
Your working tree, branches and uncommitted work are never touched. Without --push the commit is kept on a
local branch (refresh/<as_of>) instead of main. Nothing is pushed on any failure.
Exit codes: 0 updated or skipped, 1 failed/refused. Never touches Pages settings or CNAME.
"""
import argparse, datetime, json, os, re, shutil, subprocess, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
# Files the refresh may commit: the data-driven outputs, plus the guides added in October 2026 so that
# they are covered once they are live. A file is only ever committed if the build changed it AND it is
# listed here; a build that changes anything else is refused (see check_changes).
STAGE = ["data/paper-trades.json", "assets/search-index.json", "paper-trading.html", "sitemap.xml", "tools.html", "tools/garmin-insights/index.html",
         # go-live additions (only matter once these exist on origin/main; harmless before)
         "pay-tax-payslip.html", "scams-fraud.html", "budgeting-emergency-fund.html", "insurance-basics.html",
         "assets/calc-ui6.js", "assets/calc-ui7.js", "assets/money-matters-cheat-sheet-2026-27.pdf", "assets/explained-simply-money-matters.pdf",
         "scripts/gap_common.py", "scripts/gap_sections.py", "scripts/pages14.py", "scripts/pages15.py",
         # deals & savings (preview until approved; only matters once these exist on origin/main)
         "deals.html", "data/deals.json", "scripts/pages16.py", "scripts/update_deals.py",
         "feedback.html", "assets/feedback.js", "scripts/pages17.py"]
def placeholder(d):
    if d.get("placeholder"): return True
    txt = " ".join(str(d.get(k, "")) for k in ("disclaimer", "note", "notes")) + " " + " ".join(str(d[b].get(k, "")) for b in BOOKS if isinstance(d.get(b), dict) for k in ("name", "notes", "description"))
    return bool(re.search(r"placeholder|dummy|lorem|sample data|example data|mock", txt, re.I))
GH = shutil.which("gh") or "/usr/local/bin/gh"
# the repo's configured credential helper points at /usr/bin/gh, which is not where gh lives on the box: name the real path
CRED = ["-c", "credential.helper=", "-c", f"credential.helper=!{GH} auth git-credential"]
AUTHOR = ["-c", "user.name=Subhash Sharma", "-c", "user.email=334298032+subhashsharma-glitch@users.noreply.github.com"]
def git(*a, cwd=ROOT, check=False): return subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True, check=check)
def net(*a, cwd=ROOT): return subprocess.run(["timeout", "90", "git", *CRED, *a], cwd=cwd).returncode == 0

HREF = re.compile(r"""(?:href|src)=["']([^"']+)["']""", re.I)
IDS = re.compile(r"""\bid=["']([^"']+)["']""")
def internal_target(ref, page):
    """Map an href to (path, fragment) for site-internal links; None for external/non-page references."""
    if re.match(r"^(?:[a-z][a-z0-9+.-]*:|//)", ref, re.I): return None
    path, _, frag = ref.partition("#"); path = path.partition("?")[0]
    if not path: path = page
    elif not path.startswith("/"): path = os.path.normpath(os.path.join(os.path.dirname(page), path))
    else: path = path.lstrip("/")
    if path in ("", "."): path = "index.html"
    if path.endswith("/"): path += "index.html"
    return path, frag
def search_urls(t):
    """URLs in assets/search-index.json: {"e": [[url, title, page, type, text], ...]}; '#x' entries belong to the preceding page."""
    out, page = [], ""
    for e in json.loads(t).get("e", []):
        u = e[0]
        if u.startswith("#"): out.append(page + u)
        else: page = u.partition("#")[0]; out.append(u)
    return out
def check_links(wt, changed, base_files):
    """Every internal link/anchor in the changed files must point at a file that is on origin/main (or is itself being committed)."""
    ok_files = set(base_files) | set(changed); bad = []
    def have(p): return p in ok_files or (p.rstrip("/") + "/index.html") in ok_files
    targets = []
    for f in changed:
        p = os.path.join(wt, f)
        if not os.path.exists(p): continue
        if f.endswith(".html"): targets += [(f, r) for r in HREF.findall(open(p, encoding="utf-8", errors="replace").read())]
        elif f == "sitemap.xml": targets += [(f, re.sub(r"^https://moneybysharma\.co\.uk/?", "", u)) for u in re.findall(r"<loc>([^<]+)</loc>", open(p).read())]
        elif f == "assets/search-index.json": targets += [(f, u) for u in search_urls(open(p).read())]
    ids_cache = {}
    for f, ref in targets:
        r = internal_target(ref, f if f.endswith(".html") else "index.html")
        if r is None: continue
        path, frag = r
        if not have(path): bad.append(f"{f} -> {ref} (page not on origin/main)"); continue
        fp = os.path.join(wt, path)
        if frag and path.endswith(".html") and os.path.exists(fp):
            ids = ids_cache.get(path)
            if ids is None: ids = ids_cache[path] = set(IDS.findall(open(fp, encoding="utf-8", errors="replace").read()))
            if frag not in ids: bad.append(f"{f} -> {ref} (no such anchor)")
    return sorted(set(bad))
def check_changes(wt, base_files):
    st = git("status", "--porcelain", "--untracked-files=all", cwd=wt).stdout.splitlines()
    changed = [l[3:].strip().strip('"') for l in st]
    outside = [c for c in changed if c not in STAGE]
    if outside: fail("the rebuild changed files outside the allowed list (nothing committed): " + ", ".join(outside[:12]))
    new = [c for c in changed if c not in base_files]
    if new: fail("the rebuild created files that are not on origin/main (nothing committed): " + ", ".join(new[:12]))
    bad = check_links(wt, changed, base_files)
    if bad: fail("links to unpublished pages or missing anchors (nothing committed):\n  " + "\n  ".join(bad[:25]))
    return changed
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--src", default=SRC); ap.add_argument("--base", default="origin/main")
    ap.add_argument("--no-commit", action="store_true"); ap.add_argument("--push", action="store_true"); a = ap.parse_args()
    if not os.path.exists(a.src): fail("export not found: " + a.src)
    try: d = json.load(open(a.src))
    except Exception as e: fail(f"export is not valid JSON: {e}")
    if placeholder(d): fail("export looks like placeholder data; refusing to publish")
    validate(d)
    remote, _, branch = a.base.partition("/")
    if not net("fetch", "-q", remote, branch): fail(f"could not fetch {a.base}; nothing built")
    if git("rev-parse", "--verify", "-q", a.base).returncode != 0: fail("unknown base " + a.base)
    base_files = set(git("ls-tree", "-r", "--name-only", a.base, check=True).stdout.splitlines())
    tmp = tempfile.mkdtemp(prefix="mbs-refresh-"); wt = os.path.join(tmp, "site")
    git("worktree", "add", "-q", "--detach", wt, a.base, check=True)
    try:
        dest = os.path.join(wt, "data", "paper-trades.json")
        if os.path.exists(dest):
            o = json.load(open(dest))
            if datetime.datetime.fromisoformat(d["as_of"]) < datetime.datetime.fromisoformat(o["as_of"]):
                print(f"skip: export ({d['as_of']}) is older than the published data ({o['as_of']})"); return
            if o == d: print("skip: export is unchanged"); return
        shutil.copyfile(a.src, dest)
        for cmd in ("build.py", "garmin_chrome.py"):
            if subprocess.run([sys.executable, f"scripts/{cmd}"], cwd=wt).returncode != 0: fail(f"scripts/{cmd} failed in the clean checkout; nothing committed")
        changed = check_changes(wt, base_files)
        print("checks passed. files changed:", ", ".join(changed) or "none")
        if a.no_commit: print("built and checked in a clean checkout; not committed"); return
        git("add", "--", *changed, cwd=wt, check=True)
        if git("diff", "--cached", "--quiet", cwd=wt).returncode == 0: print("no changes to commit"); return
        c = git(*AUTHOR, "commit", "-q", "-m", f"Paper trading: update export as of {d['as_of']}", cwd=wt)
        if c.returncode != 0: fail("commit failed: " + c.stderr.strip())
        sha = git("rev-parse", "HEAD", cwd=wt).stdout.strip()
        if not a.push:
            br = "refresh/" + re.sub(r"[^0-9A-Za-z]+", "-", d["as_of"]).strip("-")
            git("branch", "-f", br, sha, check=True); print(f"committed {sha[:7]} on local branch {br} (not pushed; use --push)."); return
        if not net("push", "-q", remote, f"{sha}:refs/heads/{branch}", cwd=wt): fail("push failed or was rejected (remote moved?); commit kept only on the throwaway checkout, NOT pushed - rerun to retry")
        print("pushed:", git("log", "--oneline", "-1", sha).stdout.strip())
    finally:
        git("worktree", "remove", "--force", wt); git("worktree", "prune"); shutil.rmtree(tmp, ignore_errors=True)
if __name__ == "__main__": main()
