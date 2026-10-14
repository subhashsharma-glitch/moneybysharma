# Money Matters cheat sheet (exec'd from build.py) – reuses figures and sources already on the site
TY = "2026/27 (6 Apr 2026 – 5 Apr 2027)"
def _s(k, asat):
    return f'<a href="{S[k][1]}">{html.escape(S[k][0].split(" – ")[0])}</a>, as at {asat}'
CSD = []
def _sec(title, rows):
    CSD.append({"title": title, "rows": [list(x) for x in rows]})
    r = "".join(f'<tr><th scope="row">{a}</th><td>{b}</td><td class="cs-src">{c}</td></tr>' for a,b,c in rows)
    return f'<section class="cs-sec"><h2>{title}</h2><table class="cs"><thead><tr><th scope="col">Item</th><th scope="col">Figure</th><th scope="col">Source</th></tr></thead><tbody>{r}</tbody></table></section>'
lm = CPI["latestMonth"]; cpim = lm["period"].split()[1].title() + " " + lm["period"].split()[0]
CS = (
 _sec("Income tax (England, Wales &amp; NI)", [
  ("Personal Allowance","£12,570 (reduced by £1 for every £2 of income over £100,000)",_s("rates",TY)),
  ("Basic rate 20%","£12,571 – £50,270",_s("rates",TY)),
  ("Higher rate 40%","£50,271 – £125,140",_s("rates",TY)),
  ("Additional rate 45%","Over £125,140 (Scotland has its own bands)",_s("rates",TY))]) +
 _sec("Savings", [
  ("Personal Savings Allowance","£1,000 basic rate · £500 higher rate · £0 additional rate",_s("savtax",TY)),
  ("Starting rate for savings","0% on up to £5,000, reduced £1 for £1 by other income above the Personal Allowance",_s("savtax",TY)),
  ("FSCS deposit protection","£120,000 per person, per banking licence (was £85,000 until 30 Nov 2025)",_s("fscsbb","1 Dec 2025")),
  ("Bank Rate",f'{BR["rate"]:.2f}% (since {d(BR["since"])})',_s("boe",d(BR["asAt"]))),
  ("CPI inflation",f'{lm["rate"]}% in the year to {cpim}',_s("cpi","ONS release of " + datetime.datetime.strptime(CPI["released"],"%d-%m-%Y").strftime("%-d %B %Y")))]) +
 _sec("ISAs", [
  ("ISA allowance","£20,000 a year across all ISAs",_s("isa",TY)),
  ("Cash ISA change","From 6 April 2027, under-65s can put at most £12,000 of the £20,000 in cash ISAs",_s("cashisa","Nov 2025 announcement")),
  ("Lifetime ISA","Open aged 18–39; up to £4,000 a year (within the £20,000) with a 25% government bonus",_s("lisa",TY)),
  ("Junior ISA","£9,000 a year for under-18s",_s("isa",TY))]) +
 _sec("Pensions", [
  ("Annual allowance","£60,000 for most people (all contributions, including employer)",_s("aa",TY)),
  ("Tax relief","At your marginal rate, on contributions up to 100% of UK earnings (or £3,600 gross if little or no earnings)",_s("pentax",TY)),
  ("Access age","55, rising to 57 on 6 April 2028",_s("nmpa","12 Oct 2026")),
  ("Full new State Pension","£241.30 a week (about £12,548 a year)",_s("sp",TY))]) +
 _sec("Investing", [
  ("Capital Gains Tax","Annual exempt amount £3,000; rates 18% (basic-rate) and 24% (higher/additional-rate)",_s("rates",TY)),
  ("Dividends","£500 allowance; rates 10.75% basic · 35.75% higher · 39.35% additional",_s("rates",TY))]) +
 _sec("Bills and consumer rights", [
  ("Energy price cap","£1,723 a year for a typical dual-fuel household on Direct Debit",_s("cap","1 Oct – 31 Dec 2026")),
  ("Section 75","Card provider jointly liable for purchases over £100 and up to £30,000 paid at least partly by credit card",_s("s75","12 Oct 2026")),
  ("Current Account Switch Service","Switch in 7 working days; payments redirected; refunds if the switch goes wrong",_s("cass","12 Oct 2026"))])
)
BASICS = '''<section class="cs-sec cs-basics"><h2>Money basics checklist</h2><ul class="cs-check">
<li><strong>Emergency fund</strong> – easy-access cash for unexpected bills, built up before investing.</li>
<li><strong>Pay off expensive debt</strong> – credit card and overdraft interest usually costs more than savings earn.</li>
<li><strong>Get your employer's pension match</strong> – contributing enough to get the full employer contribution adds money you'd otherwise miss out on.</li>
<li><strong>Use your ISAs</strong> – interest, dividends and gains inside an ISA are tax-free.</li>
<li><strong>Give it time</strong> – investing is for five years or more; staying invested through ups and downs matters more than timing the market.</li></ul></section>'''
CSFOOT = f'<p class="cs-foot"><strong>Information only – not financial advice.</strong> MoneyBySharma isn\'t authorised or regulated by the FCA. Figures were checked on {CHECKED} against the sources shown and can change; rules differ in Scotland. Investments can fall as well as rise. moneybysharma.co.uk</p>'
pages["money-matters-cheat-sheet.html"] = page("money-matters-cheat-sheet.html","Money Matters cheat sheet 2026/27 – MoneyBySharma",
 "The key UK personal finance figures for 2026/27 on one page: tax bands, savings and ISA allowances, pensions, FSCS, Bank Rate, CPI, the price cap and more, each with its source.",
 ph('<a href="resources.html">Resources</a> › Money Matters cheat sheet',"Money Matters cheat sheet 2026/27","UK personal finance at a glance. Every figure links to its official source, with an \"as at\" date."), W(f'''
<p class="cs-actions"><a class="btn" href="assets/money-matters-cheat-sheet-2026-27.pdf" download>Download the printable PDF (A4)</a> <a href="resources.html">Back to Resources</a></p>
<div class="cs-grid">{CS}{BASICS}</div>{CSFOOT}'''))

import re as _re
json.dump({"sections": CSD, "basics": _re.findall(r"<li>(.*?)</li>", BASICS), "foot": CSFOOT, "lead": "UK personal finance at a glance. Every figure links to its official source, with an \"as at\" date.", "checked": CHECKED},
          open("data/cheat-sheet.json","w"), ensure_ascii=False, indent=1)
