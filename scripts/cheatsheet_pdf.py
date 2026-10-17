"""Build assets/money-matters-cheat-sheet-2026-27.pdf in the Explained Simply template.
Content comes only from data/cheat-sheet.json (written by pages7.py during build.py)."""
import json, os, subprocess, sys, tempfile
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = json.load(open(f"{R}/data/cheat-sheet.json"))
INTER = "/usr/share/fonts/truetype/sand-box/google/Inter/Inter-VariableFont_opsz,wght.ttf"
FD = os.environ.get("CS_FONTS", "/tmp/csfonts")
def _fonts():
    # Static instances of Inter (variable fonts print as Type 3 glyphs otherwise)
    from fontTools.ttLib import TTFont
    from fontTools.varLib import instancer
    os.makedirs(FD, exist_ok=True)
    for w in (400, 600, 700, 800):
        f = f"{FD}/Inter-{w}.ttf"
        if not os.path.exists(f):
            instancer.instantiateVariableFont(TTFont(INTER), {"wght": w, "opsz": 14 if w < 700 else 28}).save(f)
    return "".join(f'@font-face{{font-family:Inter;src:url("file://{FD}/Inter-{w}.ttf");font-weight:{w}}}' for w in (400, 600, 700, 800))
FONTFACES = _fonts()
SEC = {s["title"]: s for s in D["sections"]}
PAGES = [  # (kicker, title, subtitle, [section titles])
 ("TAX &amp; SAVINGS", "Income tax and savings", "Bands, allowances and protection", ["Income tax (England, Wales &amp; NI)", "Savings"]),
 ("ISAs &amp; INVESTING", "ISAs and investing", "Allowances, tax and protection", ["ISAs", "Investing"]),
 ("PENSIONS &amp; INSURANCE", "Pensions and insurance", "Key ages, rules of thumb and protection", ["Pensions", "Money habits and insurance"]),
 ("WORK &amp; PAY", "Work and pay", "National Insurance, minimum wage and deductions", ["Work and pay"]),
 ("BORROWING &amp; DEBT", "Borrowing and debt", "Caps, protections and who to call", ["Borrowing and debt"]),
 ("BILLS &amp; RIGHTS", "Bills and your rights", "Prices, refunds and protections", ["Bills and consumer rights"]),
 ("SCAMS &amp; BASICS", "Scams and money basics", "Where to report, and a simple checklist", ["Scams and fraud", "BASICS"]),
]
TOTAL = 1 + len(PAGES)
def foot(n): return f'<div class="small">Figures checked {D["checked"]}. General information, not financial advice.</div><div class="foot"><span></span><span class="ft">Money Matters cheat sheet</span><span class="pn">{n:02d} / {TOTAL:02d}</span></div>'
def card(t):
    if t == "BASICS":
        lis = "".join(f'<li><span class="tick">✓</span><span>{x}</span></li>' for x in D["basics"])
        return f'<section class="card"><h2>Money basics checklist</h2><ul class="chk">{lis}</ul></section>'
    rows = "".join(f'<div class="row"><div class="lab">{a}</div><div class="fig">{b}</div><div class="src">{c}</div></div>' for a, b, c in SEC[t]["rows"])
    return f'<section class="card"><h2>{t}</h2><div class="rows">{rows}</div></section>'
chips = "".join(f'<span class="chip">{s["title"].split(" (")[0]}</span>' for s in D["sections"]) + '<span class="chip">Money basics</span>'
html = [f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>Money Matters cheat sheet 2026/27</title><style>
{FONTFACES}
@page{{size:810pt 1013.04pt;margin:0}}
*{{box-sizing:border-box}}body{{margin:0;font-family:Inter,sans-serif;color:#0b1b33}}
.page{{width:810pt;height:1013.04pt;position:relative;overflow:hidden;page-break-after:always;background:#f3f5fa}}
.dots{{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.13) 1.2pt,transparent 1.3pt);background-size:30pt 30pt}}
.cover{{background:radial-gradient(500pt 360pt at 92% 4%,rgba(255,154,31,.22),transparent 70%),radial-gradient(520pt 420pt at 0% 100%,rgba(47,96,170,.45),transparent 70%),linear-gradient(170deg,#0d1c35 0%,#0b1b33 60%,#0a1730 100%);color:#fff}}
.cv{{position:absolute;left:60pt;right:60pt;top:66pt}}
.pill{{display:inline-block;background:#ff9a1f;color:#0b1b33;font-weight:800;letter-spacing:.06em;font-size:17pt;padding:8pt 16pt;border-radius:30pt}}
.t1{{font-size:66pt;font-weight:800;letter-spacing:-.035em;line-height:1.02;margin:24pt 0 0}}.t2{{font-size:84pt;font-weight:800;letter-spacing:-.04em;line-height:1;color:#ff9a1f;margin:0}}
.sub{{font-size:30pt;font-weight:800;letter-spacing:-.02em;line-height:1.15;margin:34pt 0 14pt}}.sub u{{text-decoration:none;box-shadow:inset 0 -10pt 0 rgba(255,154,31,.55)}}
.lead{{font-size:21pt;line-height:1.5;color:#c9d4e5;margin:0 0 26pt}}
.chips{{display:flex;flex-wrap:wrap;gap:10pt}}.chip{{border:1.2pt solid rgba(201,212,229,.4);background:rgba(255,255,255,.05);border-radius:10pt;padding:8pt 14pt;font-size:16pt;font-weight:600}}
.by{{position:absolute;left:60pt;top:840pt;font-size:21pt;color:#c9d4e5}}.byn{{position:absolute;left:60pt;top:868pt;font-size:36pt;font-weight:800;letter-spacing:-.01em}}
.small{{position:absolute;left:48pt;right:48pt;bottom:62pt;text-align:center;font-size:12.5pt;color:#7d8899}}
.foot{{position:absolute;left:48pt;right:48pt;bottom:20pt;border-top:1pt solid #d5dbe5;padding-top:14pt;display:grid;grid-template-columns:1fr auto 1fr;font-size:16pt;color:#5a6678}}
.foot .pn{{text-align:right;font-weight:700}}
.cover .foot{{border-color:rgba(255,255,255,.18);color:#c9d4e5}}.cover .small{{color:#8a97ad}}
.hd{{background:#0b1b33;color:#fff;padding:36pt 48pt 22pt;border-bottom:6pt solid #ff9a1f}}
.kick{{color:#ff9a1f;font-weight:800;letter-spacing:.08em;font-size:18pt}}.hd h1{{font-size:44pt;font-weight:800;letter-spacing:-.03em;margin:4pt 0 2pt;line-height:1.1}}.hd p{{margin:0;font-size:21pt;color:#c9d4e5}}
.body{{padding:24pt 42pt 0}}
.card{{background:#fff;border-radius:16pt;box-shadow:0 2pt 10pt rgba(11,27,51,.08);margin:0 0 18pt;overflow:hidden}}
.card h2{{margin:0;background:#0b1b33;color:#fff;font-size:21pt;font-weight:800;padding:12pt 22pt;border-bottom:4pt solid #ff9a1f;letter-spacing:-.01em}}
.rows{{padding:4pt 22pt}}.row{{display:grid;grid-template-columns:150pt 1fr 165pt;gap:16pt;padding:11pt 0;border-bottom:1pt solid #e6eaf1;align-items:start}}.row:last-child{{border-bottom:0}}
.lab{{font-weight:700;font-size:15.5pt;line-height:1.3}}.fig{{font-size:15.5pt;line-height:1.35;color:#0b1b33;font-weight:600}}
.src{{font-size:11.5pt;line-height:1.35;color:#5a6678}}.src a{{color:#e07c00;text-decoration:none;font-weight:700}}
.chk{{list-style:none;margin:0;padding:10pt 22pt}}.chk li{{display:flex;gap:12pt;padding:7pt 0;font-size:15pt;line-height:1.4;color:#2f3b50}}.tick{{flex:none;width:22pt;height:22pt;border-radius:6pt;background:#ff9a1f;color:#0b1b33;font-weight:800;display:grid;place-items:center;font-size:13pt}}
.chk strong{{color:#0b1b33}}
.disc{{background:#fff4e2;border-radius:14pt;padding:14pt 20pt;font-size:13.5pt;line-height:1.45;color:#4a3610}}.disc strong{{color:#e07c00}}
</style></head><body>
<div class="page cover"><div class="dots"></div><div class="cv"><span class="pill">UK PERSONAL FINANCE · 2026/27</span>
<div class="t1">Money Matters</div><div class="t2">cheat sheet</div>
<div class="sub"><u>UK personal finance</u><br>at a glance.</div>
<p class="lead">Every figure links to its official source, with an "as at" date.</p><div class="chips">{chips}</div></div>
<div class="by">by</div><div class="byn">MoneyBySharma</div>{foot(1)}</div>''']
for i, (k, t, s, secs) in enumerate(PAGES, start=2):
    extra = f'<div class="disc">{D["foot"].replace("<p class=\"cs-foot\">","").replace("</p>","")}</div>' if i == TOTAL else ""
    html.append(f'<div class="page"><div class="hd"><div class="kick">{k}</div><h1>{t}</h1><p>{s}</p></div><div class="body">{"".join(card(x) for x in secs)}{extra}</div>{foot(i)}</div>')
html.append("</body></html>")
tmp = tempfile.mkdtemp(); src = f"{tmp}/cs.html"; open(src, "w").write("".join(html))
out = sys.argv[1] if len(sys.argv) > 1 else f"{R}/assets/money-matters-cheat-sheet-2026-27.pdf"
subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", "--allow-file-access-from-files", f"--print-to-pdf={out}", f"file://{src}"], check=True, capture_output=True)
print("wrote", out)
