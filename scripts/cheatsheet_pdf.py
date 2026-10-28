"""Build assets/money-matters-cheat-sheet-2026-27.pdf in the Explained Simply house style
(MoneyBySharma logo on the cover, icon header tiles, header-band cards).
Content comes only from data/cheat-sheet.json (written by pages7.py during build.py).
Style, fonts and icons are reused from the Explained Simply source on the box:
/workspace/mbs-explained-src (base.py + the ICONS/CSS additions in build.py). Override with ES_SRC.
Usage: python3 scripts/cheatsheet_pdf.py [out.pdf]"""
import html as _h, json, os, re, sys, asyncio
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ES = os.environ.get("ES_SRC", "/workspace/mbs-explained-src")
D = json.load(open(f"{R}/data/cheat-sheet.json"))
sys.path.insert(0, ES)
from base import S, ICONS, CSS as BASECSS
_src = open(f"{ES}/build.py").read()
exec(re.search(r"ICONS\.update\(\{.*?\n\}\)", _src, re.S).group(0))            # extra icons (percent, jar, lock, ...)
ESCSS = re.search(r"CSS = BASECSS \+ r'''(.*?)'''", _src, re.S).group(1)        # logo, header-band cards, cover title

TITLE = "Money Matters cheat sheet"
SEC = {s["title"]: s for s in D["sections"]}
SICON = {"Income tax (England, Wales &amp; NI)": "percent", "Savings": "jar", "ISAs": "lock", "Investing": "growth",
         "Pensions": "hourglass", "Money habits and insurance": "umbrella", "Work and pay": "payslip",
         "Borrowing and debt": "scale", "Bills and consumer rights": "home", "Scams and fraud": "shield", "BASICS": "check",
         "Announced for 2027/28": "calendar"}
PAGES = [  # (kicker, title, subtitle, header icon, [section titles])
 ("Tax &amp; savings", "Income tax and savings", "Bands, allowances and protection", "percent", ["Income tax (England, Wales &amp; NI)", "Savings"]),
 ("ISAs &amp; investing", "ISAs and investing", "Allowances, tax and protection", "lock", ["ISAs", "Investing"]),
 ("Pensions &amp; insurance", "Pensions and insurance", "Key ages, rules of thumb and protection", "hourglass", ["Pensions", "Money habits and insurance"]),
 ("Work &amp; pay", "Work and pay", "National Insurance, minimum wage and deductions", "payslip", ["Work and pay"]),
 ("Borrowing &amp; debt", "Borrowing and debt", "Caps, protections and who to call", "scale", ["Borrowing and debt"]),
 ("Bills &amp; rights", "Bills and your rights", "Prices, refunds and protections", "home", ["Bills and consumer rights"]),
 ("Budget 2026", "Announced for 2027/28", "From the Budget on 28 Oct 2026; some not law yet", "calendar", ["Announced for 2027/28"]),
 ("Scams &amp; basics", "Scams and money basics", "Where to report, and a simple checklist", "shield", ["Scams and fraud", "BASICS"]),
]
TOTAL = 1 + len(PAGES)
NOTE = f'Figures checked {D["checked"]}. General information, not financial advice.'
LOGO = ('<div class="mbs-logo" role="img" aria-label="MoneyBySharma"><svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="8" fill="#0f4c45"/>'
        '<path d="M8 22V11l8 7 8-7v11" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
        '<circle cx="24" cy="8" r="2.6" fill="#d9822b"/></svg><span class="wm">Money<i>By</i>Sharma</span></div>')
CSS = BASECSS + ESCSS + r'''
.cover h1 .w { font-size:92px; } .cover h1 .o { font-size:122px; }
.cover .subt { font-size:30px; }
.cover .hook { margin-top:34px; } .cover .chips { margin-top:44px; }
.cover .byline { bottom:132px; }
.cover .fnote { bottom:84px; }
.body { justify-content:flex-start; gap:14px; top:222px; }
.hc .hb .t { font-size:28px; }
.cs { padding:2px 22px 4px 24px; }
.cs .r { display:grid; grid-template-columns:212px 1fr 204px; gap:18px; padding:11px 0; border-top:2px solid #EEF1F6; align-items:start; }
.cs .r:first-child { border-top:none; }
.cs .l { padding-right:12px; font-size:22px; font-weight:800; color:var(--navy); line-height:1.32; }
.cs .f { margin-left:4px; padding-right:12.5px; font-size:22.42px; font-weight:500; color:var(--navy); line-height:1.29; }
.cs .s { font-size:17px; color:var(--muted); line-height:1.35; }
.cs .s a { color:var(--orange-d); font-weight:800; text-decoration:none; }
.hc .ticks { padding:4px 22px 20px; } .hc .ticks li { font-size:23px; margin-top:12px; } .hc .ticks li b, .hc .ticks li strong { color:var(--navy); font-weight:800; }
.csdisc { background:#FFF2E0; border-radius:16px; padding:14px 16px 14px 24px; font-size:21px; line-height:1.38; color:#4A3610; }
.csdisc strong { color:var(--orange-d); font-weight:800; }
'''
e = _h.escape
def footer(n): return f'<div class="fnote">{e(NOTE)}</div><div class="footer"><span></span><span>{TITLE}</span><span class="num">{n:02d} / {TOTAL:02d}</span></div>'
def card(t):
    if t == "BASICS":
        body = '<ul class="ticks">' + "".join(f"<li>{x}</li>" for x in D["basics"]) + "</ul>"; name = "Money basics checklist"
    else:
        body = '<div class="cs">' + "".join(f'<div class="r"><div class="l">{a}</div><div class="f">{b}</div><div class="s">{c}</div></div>' for a, b, c in SEC[t]["rows"]) + "</div>"; name = t
    return f'<div class="hc"><div class="hb">{ICONS[SICON[t]]}<div class="t">{name}</div></div>{body}</div>'
chips = "".join(f'<div class="chip">{ICONS[SICON[s["title"]]]}{s["title"].split(" (")[0]}</div>' for s in D["sections"]) + f'<div class="chip">{ICONS["check"]}Money basics</div>'
pages = [f'''<section class="page cover dark"><div class="grid"></div><div class="inner">
<div class="pillc">UK personal finance · 2026/27</div>
<h1><span class="w">Money Matters</span><span class="o">cheat sheet</span></h1>
<div class="hook"><span>UK personal finance</span><br>at a glance.</div>
<div class="subt">{D["lead"].replace("UK personal finance at a glance. ", "")}</div><div class="chips">{chips}</div></div>
<div class="byline">{LOGO}</div>{footer(1)}</section>''']
for i, (k, t, s, ic, secs) in enumerate(PAGES, start=2):
    extra = f'<div class="csdisc">{D["foot"].replace("<p class=\"cs-foot\">", "").replace("</p>", "")}</div>' if i == TOTAL else ""
    pages.append(f'<section class="page"><div class="head"><div class="kicker">{k}</div><h1>{t}</h1><div class="sub">{s}</div><div class="ico">{ICONS[ic]}</div></div>'
                 f'<div class="body">{"".join(card(x) for x in secs)}{extra}</div>{footer(i)}</section>')
OUT = sys.argv[1] if len(sys.argv) > 1 else f"{R}/assets/money-matters-cheat-sheet-2026-27.pdf"
HTML = os.path.splitext(OUT)[0] + ".build.html" if len(sys.argv) > 2 else "/tmp/cheatsheet-build.html"
open(HTML, "w").write(f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>Money Matters cheat sheet 2026/27</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>')

CHECK = r'''() => [...document.querySelectorAll('.page')].map((p, i) => {
  const lim = (p.querySelector('.fnote') || p.querySelector('.footer')).getBoundingClientRect().top;
  let mx = 0; p.querySelectorAll('.body *, .inner *').forEach(c => { mx = Math.max(mx, c.getBoundingClientRect().bottom); });
  const pr = p.getBoundingClientRect(); const over = [...p.querySelectorAll('*')].some(c => { const r = c.getBoundingClientRect(); return r.width && r.right > pr.right + .5; });
  return {page: i + 1, slack: Math.round(lim - mx), overflowX: over};
})'''
async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        await pg.goto("file://" + HTML); await pg.evaluate("document.fonts.ready"); await pg.emulate_media(media="print")
        bad = [r for r in await pg.evaluate(CHECK) if r["slack"] < 8 or r["overflowX"]]
        if bad: print("LAYOUT PROBLEMS", bad)
        await pg.pdf(path=OUT, width="1080px", height="1350px", print_background=True, prefer_css_page_size=True)
        await b.close()
    print("wrote", OUT)
asyncio.run(main())
