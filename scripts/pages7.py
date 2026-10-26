# Money Matters cheat sheet (exec'd from build.py) – reuses figures and sources already on the site
TY = "2026/27 (6 Apr 2026 – 5 Apr 2027)"
def _s(k, asat):
    return f'<a href="{S[k][1]}">{html.escape(S[k][0].split(" – ")[0])}</a>, as at {asat}'
CSD = []
def _sec(title, rows):
    CSD.append({"title": title, "rows": [list(x) for x in rows]})
    r = "".join(f'<tr><th scope="row">{a}</th><td>{b}</td><td class="cs-src">{c}</td></tr>' for a,b,c in rows)
    return f'<section class="cs-sec"><h2>{title}</h2><table class="cs"><thead><tr><th scope="col">Item</th><th scope="col">Figure</th><th scope="col">Source</th></tr></thead><tbody>{r}</tbody></table></section>'
lm = CPI["latestMonth"]; CPI_BULLETIN = CPI.get("bulletinUrl", CPI["sourceUrl"]); CPI_PUB = datetime.datetime.strptime(CPI["released"],"%d-%m-%Y").strftime("%-d %b %Y"); CPI_CHK = datetime.date.fromisoformat(CPI["fetched"]).strftime("%-d %b %Y"); CPI_NEXT = datetime.datetime.strptime(CPI["nextRelease"],"%d %B %Y").strftime("%-d %b %Y"); cpim = lm["period"].split()[1].title() + " " + lm["period"].split()[0]
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
  ("CPI inflation",f'{lm["rate"]}% in the year to {cpim}',f'<a href="{CPI_BULLETIN}">ONS</a>, published {CPI_PUB}, checked {CPI_CHK}; next release {CPI_NEXT}')]) +
 _sec("ISAs", [
  ("ISA allowance","£20,000 a year across all ISAs",_s("isa",TY)),
  ("Cash ISA change","From 6 April 2027, under-65s can put at most £12,000 of the £20,000 in cash ISAs",_s("cashisa","Nov 2025 announcement")),
  ("Lifetime ISA","Open aged 18–39; up to £4,000 a year (within the £20,000) with a 25% government bonus",_s("lisa",TY)),
  ("Lifetime ISA withdrawals","First home costing £450,000 or less, bought 12+ months after your first payment, or from age 60; other withdrawals face a 25% charge",_s("lisa2","17 Oct 2026")),
  ("Junior ISA","£9,000 a year for under-18s",_s("isa",TY))]) +
 _sec("Pensions", [
  ("Annual allowance","£60,000 for most people (all contributions, including employer)",_s("aa",TY)),
  ("Tax relief","At your marginal rate, on contributions up to 100% of UK earnings (or £3,600 gross if little or no earnings)",_s("pentax",TY)),
  ("Access age","55, rising to 57 on 6 April 2028",_s("nmpa","12 Oct 2026")),
  ("Full new State Pension","£241.30 a week (about £12,548 a year)",_s("sp",TY)),
  ("Pension Tracing Service","Free GOV.UK service to find a lost pension's contact details (0800 731 0175). It won't say whether you have one or its value",_s("pts","17 Oct 2026"))]) +
 _sec("Work and pay", [
  ("National Insurance (employees)","8% on pay of £242.01–£967 a week (£1,048.01–£4,189 a month); 2% above that",_s("ni",TY)),
  ("Employer National Insurance","15% on pay above £96 a week (£417 a month) for most employees",_s("nirates",TY)),
  ("Self-employed (Class 4)","6% on profits of £12,570–£50,270; 2% above that",_s("nise",TY)),
  ("Minimum wage (from 1 Apr 2026)","£12.71 aged 21+ · £10.85 aged 18–20 · £8.00 under 18 and apprentices",_s("nmw","1 Apr 2026")),
  ("Trading allowance","£1,000 a year of gross side income, one allowance across all of it; above that, register for Self Assessment",_s("trading",TY)),
  ("Student loan thresholds","Plan 1 £26,900 · Plan 2 £29,385 · Plan 4 £33,795 · Plan 5 £25,000 · Postgraduate £21,000 a year. 9% of income above (6% Postgraduate)",_s("slrepay",TY)),
  ("Plan 2 student loan","Started 2012–2023 (England). Interest 4.1% to 6% by income (the 6% limit is described as 'currently' in place); written off after 30 years",_s("slwo","17 Oct 2026")),
  ("Workplace pension minimum","8% of qualifying earnings (£6,240–£50,270) in total, with at least 3% from the employer",_s("aemin",TY))]) +
 _sec("Borrowing and debt", [
  ("Payday loan cap","0.8% a day of the amount borrowed (interest and fees); £15 maximum default charges; total charges capped at 100% of the amount borrowed",_s("hcstc","17 Oct 2026")),
  ("Loan sharks (report)","England 0300 555 2222 · Wales 0300 123 3311 · Scotland 0800 074 0878 · Northern Ireland (Consumerline) 0300 123 6262",_s("loansh","17 Oct 2026")),
  ("Buy now, pay later","FCA-regulated since 15 July 2026 (interest-free deferred payment credit where lender and seller are different businesses); Section 75 applies to those agreements",_s("bnpl","17 Oct 2026")),
  ("Representative APR","The rate must be available to at least 51% of people accepted; up to 49% can be offered a higher rate",_s("apr","17 Oct 2026")),
  ("Overdrafts","One annual interest rate, no daily or monthly fees (since 6 April 2020)",_s("od","17 Oct 2026")),
  ("Breathing Space (England and Wales)","Up to 60 days' legal protection from creditors, with most interest and charges frozen",_s("bs","17 Oct 2026"))]) +
 _sec("Scams and fraud", [
  ("Call your bank safely","Hang up and dial 159, or use the number on your card",_s("s159","17 Oct 2026")),
  ("Report scam texts and emails","Texts to 7726 (free); emails to report@phishing.gov.uk",_s("phish","17 Oct 2026")),
  ("Report fraud","Report Fraud 0300 123 2040 (Scotland: 101)",_s("reportfraud","17 Oct 2026")),
  ("Bank transfer scam refunds","Up to £85,000 a claim; report within 13 months. Under review",_s("psrapp","17 Oct 2026"))]) +
 _sec("Investing", [
  ("Capital Gains Tax","Annual exempt amount £3,000; rates 18% (basic-rate) and 24% (higher/additional-rate)",_s("rates",TY)),
  ("Dividends","£500 allowance; rates 10.75% basic · 35.75% higher · 39.35% additional",_s("rates",TY)),
  ("FSCS investment protection","Up to £85,000 per person, per firm if an authorised investment firm fails (after 1 April 2019). It does not cover falls in value",_s("fscsinv","17 Oct 2026"))]) +
 _sec("Money habits and insurance", [
  ("Emergency fund","Rule of thumb: three to six months' essential outgoings in an instant-access account",_s("mhem","17 Oct 2026")),
  ("Motor insurance","Third party is the legal minimum to drive on UK roads",_s("vehins","17 Oct 2026")),
  ("FSCS insurance protection","100% for compulsory cover such as third-party motor; 90% for home, travel, first-party motor and others",_s("fscsins","17 Oct 2026"))]) +
 _sec("Bills and consumer rights", [
  ("Energy price cap","£1,723 a year for a typical dual-fuel household on Direct Debit",_s("cap","1 Oct – 31 Dec 2026")),
  ("Faulty goods","Short-term right to reject within 30 days, for a refund",_s("cra22","17 Oct 2026")),
  ("Online, phone and mail orders","Cancel within 14 days of receiving the item, no reason needed; a further 14 days to return it",_s("govret","17 Oct 2026")),
  ("Direct Debit Guarantee","Full and immediate refund if the organisation or your bank makes an error",_s("ddg","17 Oct 2026")),
  ("Chargeback (debit cards)","A voluntary card-scheme process, not a legal right: claim within 120 days",_s("mh75","17 Oct 2026")),
  ("Section 75","Card provider jointly liable for purchases over £100 and up to £30,000 paid at least partly by credit card",_s("s75","12 Oct 2026")),
  ("Current Account Switch Service","Switch in 7 working days; payments redirected; refunds if the switch goes wrong",_s("cass","12 Oct 2026"))])
)
BASICS = '''<section class="cs-sec cs-basics"><h2>Money basics checklist</h2><ul class="cs-check">
<li><strong>Emergency fund</strong> – easy-access cash for unexpected bills, built up before investing.</li>
<li><strong>Pay off expensive debt</strong> – credit card and overdraft interest usually costs more than savings earn.</li>
<li><strong>Get your employer's pension match</strong> – contributing enough to get the full employer contribution adds money you'd otherwise miss out on.</li>
<li><strong>Use your ISAs</strong> – interest, dividends and gains inside an ISA are tax-free.</li>
<li><strong>Give it time</strong> – investing is for five years or more; staying invested through ups and downs matters more than timing the market.</li></ul></section>'''
CSFOOT = f'<p class="cs-foot"><strong>Information only – not financial advice.</strong> MoneyBySharma isn\'t authorised or regulated by the FCA. Figures were checked between 12 and 26 October 2026 against the sources shown and can change; rules differ in Scotland. Investments can fall as well as rise. moneybysharma.co.uk</p>'
pages["money-matters-cheat-sheet.html"] = page("money-matters-cheat-sheet.html","Money Matters cheat sheet 2026/27 – MoneyBySharma",
 "The key UK personal finance figures for 2026/27 in one place: tax bands, National Insurance, minimum wage, savings and ISA allowances, pensions, FSCS, scam reporting numbers, Bank Rate, CPI and more, each with its source.",
 ph('<a href="resources.html">Resources</a> › Money Matters cheat sheet',"Money Matters cheat sheet 2026/27","UK personal finance at a glance. Every figure links to its official source, with an \"as at\" date."), W(f'''
<p class="cs-actions"><a class="btn" href="assets/money-matters-cheat-sheet-2026-27.pdf" download>Download the PDF (635 KB, 8 pages)</a> <a href="resources.html">Back to Resources</a></p>
<div class="cs-grid">{CS}{BASICS}</div>{CSFOOT}'''))

import re as _re
json.dump({"sections": CSD, "basics": _re.findall(r"<li>(.*?)</li>", BASICS), "foot": CSFOOT, "lead": "UK personal finance at a glance. Every figure links to its official source, with an \"as at\" date.", "checked": "12–26 October 2026"},
          open("data/cheat-sheet.json","w"), ensure_ascii=False, indent=1)
