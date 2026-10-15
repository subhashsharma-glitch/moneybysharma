#!/usr/bin/env python3
"""Static page generator for MoneyBySharma. Run scripts/fetch_data.py first, then this."""
import json, datetime, html
from seo import seo_meta
BR = json.load(open("data/bank-rate.json")); GI = json.load(open("data/gilts.json"))
CHECKED = "12 October 2026"
CHECKED_ISO = "2026-10-12"
def d(iso): return datetime.date.fromisoformat(iso).strftime("%-d %B %Y")
S = {  # sources (checked 12 Oct 2026)
 "rates": ("GOV.UK – Budget 2025 OOTLAR Annex A: rates and allowances (2026 to 2027)", "https://www.gov.uk/government/publications/budget-2025-overview-of-tax-legislation-and-rates-ootlar/annex-a-rates-and-allowances"),
 "savtax": ("GOV.UK – Tax on savings interest", "https://www.gov.uk/apply-tax-free-interest-on-savings"),
 "sav27": ("GOV.UK/HMRC – Changes to tax rates for property, savings and dividend income (27 Nov 2025)", "https://www.gov.uk/government/publications/income-tax-changes-to-tax-rates-for-property-savings-and-dividend-income/income-tax-changes-to-tax-rates-for-property-savings-and-dividend-income"),
 "fscs": ("FSCS – Deposit protection limit", "https://www.fscs.org.uk/what-we-cover/banks-building-societies-credit-unions/deposit-limit/"),
 "isa": ("GOV.UK – Individual Savings Accounts (ISAs)", "https://www.gov.uk/individual-savings-accounts"),
 "cashisa": ("GOV.UK/HMRC – Cash ISA limit reduction (from 6 April 2027)", "https://www.gov.uk/government/publications/reduction-in-the-cash-individual-savings-account-isa-limit/cash-individual-savings-account-isa-limit-reduction"),
 "isasi": ("legislation.gov.uk – The Individual Savings Account (Amendment) (No. 2) Regulations 2026 (SI 2026/1018)", "https://www.legislation.gov.uk/uksi/2026/1018/pdfs/uksi_20261018_en.pdf"),
 "tfs": ("GOV.UK/HMRC – Tax-free savings newsletter 19 (Nov 2025)", "https://www.gov.uk/government/publications/tax-free-savings-newsletter-19/tax-free-savings-newsletter-19-november-2025"),
 "lisa": ("GOV.UK – Lifetime ISA", "https://www.gov.uk/lifetime-isa"),
 "pentax": ("GOV.UK – Tax on your private pension contributions", "https://www.gov.uk/tax-on-your-private-pension/pension-tax-relief"),
 "aa": ("GOV.UK – Annual allowance", "https://www.gov.uk/tax-on-your-private-pension/annual-allowance"),
 "nmpa": ("HMRC Pensions Tax Manual PTM062100 – pension age", "https://www.gov.uk/hmrc-internal-manuals/pensions-tax-manual/ptm062100"),
 "boe": ("Bank of England – Bank Rate", BR["sourceUrl"]),
 "dmo": (GI["source"], GI["sourceUrl"]),
 "giltcgt": ("GOV.UK – Capital Gains Tax: what you don't pay it on (gilts)", "https://www.gov.uk/capital-gains-tax/what-you-dont-pay-it-on"),
 "aischeme": ("HMRC Savings and Investment Manual – Accrued Income Scheme", "https://www.gov.uk/hmrc-internal-manuals/savings-and-investment-manual/saim4000"),
 "scot": ("GOV.UK – Scottish Income Tax", "https://www.gov.uk/scottish-income-tax"),
 "mas": ("MoneyHelper – Mortgages (free, government-backed guidance)", "https://www.moneyhelper.org.uk/en/homes/buying-a-home"),
 "sp": ("GOV.UK – The new State Pension: what you'll get", "https://www.gov.uk/new-state-pension/what-youll-get"),
 "spni": ("GOV.UK – The new State Pension: your National Insurance record", "https://www.gov.uk/new-state-pension/your-national-insurance-record"),
 "ae": ("GOV.UK/DWP – Automatic enrolment earnings trigger and qualifying earnings band review 2026/27 (18 Dec 2025)", "https://www.gov.uk/government/publications/review-of-the-automatic-enrolment-earnings-trigger-and-qualifying-earnings-band-for-202627/review-of-the-automatic-enrolment-earnings-trigger-and-qualifying-earnings-band-for-202627"),
 "aemin": ("GOV.UK – Workplace pensions: what you, your employer and the government pay", "https://www.gov.uk/workplace-pensions/what-you-your-employer-and-the-government-pay"),
 "spa": ("GOV.UK – Check your State Pension age", "https://www.gov.uk/state-pension-age"),
 "jpm": ("J.P. Morgan Asset Management – Guide to Retirement 2026 (US edition), 'Impact of being out of the market', data as of 31 Dec 2025", "https://am.jpmorgan.com/us/en/asset-management/adv/insights/retirement-insights/guide-to-retirement/"),
 "cap": ("Ofgem – Energy price cap unit rates and standing charges (1 Oct – 31 Dec 2026)", "https://www.ofgem.gov.uk/information-consumers/energy-advice-households/energy-price-cap-unit-rates-and-standing-charges"),
 "capnews": ("Ofgem – Energy price cap will rise by 4% from October 2026 (26 Aug 2026)", "https://www.ofgem.gov.uk/press-release/energy-price-cap-will-rise-4-october-2026"),
 "est": ("Energy Saving Trust – Solar panels: costs, savings and benefits", "https://energysavingtrust.org.uk/advice/solar-panels/"),
 "seg": ("Ofgem – Smart Export Guarantee (SEG)", "https://www.ofgem.gov.uk/environmental-and-social-schemes/smart-export-guarantee-seg"),
 "vat": ("GOV.UK/HMRC – VAT Notice 708/6: energy-saving materials and heating equipment", "https://www.gov.uk/guidance/vat-on-energy-saving-materials-and-heating-equipment-notice-7086"),
 "ved": ("GOV.UK – Vehicle tax rate tables", "https://www.gov.uk/vehicle-tax-rate-tables"),
 "eved": ("GOV.UK/HMRC – Electric Vehicle Excise Duty (eVED), draft legislation (13 Jul 2026)", "https://www.gov.uk/government/publications/electric-vehicle-excise-duty-eved/electric-vehicle-excise-duty-eved"),
 "evedcr": ("GOV.UK – eVED consultation response (13 Jul 2026)", "https://www.gov.uk/government/consultations/consultation-on-the-introduction-of-electric-vehicle-excise-duty-eved/outcome/the-introduction-of-electric-vehicle-excise-duty-eved-consultation-response"),
 "zev": ("GOV.UK – Phasing out sales of new petrol and diesel cars from 2030: government response (April 2025)", "https://www.gov.uk/government/consultations/phasing-out-sales-of-new-petrol-and-diesel-cars-from-2030-and-supporting-the-zev-transition/outcome/phasing-out-sales-of-new-petrol-and-diesel-cars-from-2030-and-supporting-the-zev-transition-summary-of-responses-and-joint-government-response"),
 "bik": ("GOV.UK – Company car tax appropriate percentages (Budget 2025 Annex A)", "https://www.gov.uk/government/publications/budget-2025-overview-of-tax-legislation-and-rates-ootlar/annex-a-rates-and-allowances"),
 "ss": ("GOV.UK – Salary sacrifice for employers (optional remuneration arrangements)", "https://www.gov.uk/guidance/salary-sacrifice-and-the-effects-on-paye"),
 "fcareg": ("FCA Financial Services Register", "https://register.fca.org.uk/"),
}
def src(*keys):
    return '<p class="src">Sources (checked ' + CHECKED + '): ' + "; ".join(f'<a href="{S[k][1]}" rel="noopener">{S[k][0]}</a>' for k in keys) + ".</p>"
NAV = [("index.html","Home"),("savings.html","Savings"),("investments.html","Investments"),("pensions.html","Pensions"),("mortgages.html","Mortgages"),("gilts.html","Gilts"),("energy.html","Energy"),("energy-providers.html","Energy providers"),("electric-cars.html","Electric cars"),("jargon.html","Jargon buster"),("resources.html","Resources"),("about.html","About")]
NAVG = [("index.html","Home"),
 ("Guides",[("savings.html","Savings"),("bank-accounts.html","Bank accounts"),("credit-cards.html","Credit cards"),("credit-scores-debt-help.html","Credit scores &amp; debt help"),("investments.html","Investments"),("pensions.html","Pensions"),("mortgages.html","Mortgages"),("gilts.html","Gilts"),("energy.html","Energy"),("energy-providers.html","Energy providers"),("broadband-phones.html","Broadband &amp; phones"),("students.html","Students"),("electric-cars.html","Electric cars")]),
 ("Learn",[("how-money-works.html","How money works"),("jargon.html","Jargon buster")]),
 ("Tools",[("tools.html","All tools"),("tools/garmin-insights/",'Garmin Fitness Insights<small class="dd-desc">Your Garmin activity trends, processed in your browser</small>'),("paper-trading.html",'Paper trading experiment<small class="dd-desc">Fake-money trades and totals. Experiment only</small>')],"tools.html"),
 ("resources.html","Resources"),("about.html","About")]
LOGO = '<svg width="30" height="30" viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="8" fill="#0f4c45"/><path d="M8 22V11l8 7 8-7v11" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="24" cy="8" r="2.6" fill="#d9822b"/></svg>'
DISC = ("<strong>Information only – not financial advice.</strong> MoneyBySharma gives general information, not regulated financial advice, "
 "and is not authorised or regulated by the Financial Conduct Authority (FCA). Do your own research or speak to an FCA-authorised adviser before making decisions. "
 "With investments your capital is at risk and you may get back less than you put in. Tax treatment depends on your individual circumstances and may change in future.")
def page(fn, title, desc, body, head="", scripts=()):
    def _li(h,t): return f'<li><a href="{h}"{" aria-current=page" if h==fn else ""}>{t}</a></li>'
    nav = ""
    for item in NAVG:
        if isinstance(item[1], list):
            cur = any(h==fn for h,_ in item[1])
            lab = f'<a class="dd-link" href="{item[2]}">{item[0]}</a>' if len(item) > 2 else item[0]
            cur = cur or (len(item) > 2 and item[2] == fn)
            nav += f'<li class="dd"><details><summary{" class=cur" if cur else ""}>{lab}</summary><ul>' + "".join(_li(h,t) for h,t in item[1]) + '</ul></details></li>'
        else: nav += _li(*item)
    sc = "".join(f'<script src="assets/{s}" defer></script>' for s in ("main.js",)+tuple(scripts))
    return f'''<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{html.escape(desc)}"><meta name="theme-color" content="#0f4c45">
<link rel="canonical" href="https://moneybysharma.co.uk/{'' if fn=='index.html' else fn}">
{seo_meta(fn, title, desc)}<link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="assets/style.css">{sc}</head>
<body><a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap nav"><a class="logo" href="index.html" aria-label="MoneyBySharma home">{LOGO}<span>Money<span class="by">By</span>Sharma</span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
<nav class="main" id="nav" aria-label="Main"><ul>{nav}</ul></nav></div></header>
<main id="main">{body}{head}</main>
<footer class="site"><div class="wrap"><div class="disc"><p style="margin:0">{DISC}</p></div>
<ul><li><a href="about.html">About</a></li><li><a href="disclaimer.html">Disclaimer</a></li><li><a href="privacy.html">Privacy (no cookies)</a></li><li><a href="jargon.html">Jargon buster</a></li><li><a href="resources.html">Resources</a></li><li>Contact: <a href="mailto:hello@moneybysharma.co.uk">hello@moneybysharma.co.uk</a></li></ul>
<p style="margin:1rem 0 0">© 2026 MoneyBySharma · Plain-English UK money information · Figures checked {CHECKED} for tax year 2026/27.</p></div></footer>
</body></html>'''
def ph(crumb, h1, lead): return f'<div class="page-head"><div class="wrap"><div class="crumb"><a href="index.html">Home</a> › {crumb}</div><h1>{h1}</h1><p>{lead}</p></div></div>'
def W(x): return f'<div class="wrap">{x}</div>'
pages = {}
# ---------- HOME ----------
now = datetime.date.today().isoformat()
lowc = sorted([g for g in GI["gilts"] if g["maturity"] > (datetime.date.today()+datetime.timedelta(days=365)).isoformat()], key=lambda g: (g["coupon"], g["maturity"]))[0]
pages["index.html"] = page("index.html", "MoneyBySharma – plain-English UK money information", "Clear, neutral UK personal-finance information: savings, ISAs, pensions, mortgages and gilts, with free calculators.", f'''
<section class="hero"><div class="wrap"><span class="tag" style="background:rgba(255,255,255,.15);color:#fff">UK · Tax year 2026/27</span>
<h1>Money, explained in plain English.</h1>
<p>MoneyBySharma is a free UK personal-finance information site. Clear guides to savings, ISAs, pensions, mortgages and gilts – with simple calculators and every figure linked to its official source.</p>
<div class="cta"><a class="btn" href="savings.html">Start with savings</a><a class="btn ghost" href="#calculators">Try the calculators</a></div></div></section>
<section class="numbers" aria-labelledby="kn"><div class="wrap"><h2 id="kn">Today's key numbers</h2>
<div class="kn"><b>{BR["rate"]:.2f}%</b><small>Bank of England Bank Rate, since {d(BR["since"])}. <a href="{BR["sourceUrl"]}" rel="noopener">BoE</a> data as at {d(BR["asAt"])}.</small></div>
<div class="kn"><b>£20,000</b><small>ISA allowance 2026/27. <a href="{S["rates"][1]}" rel="noopener">GOV.UK</a></small></div>
<div class="kn"><b>£12,570</b><small>Personal Allowance 2026/27: income you can earn tax-free. Frozen to April 2031; tapers away above £100,000. <a href="https://www.gov.uk/income-tax-rates" rel="noopener">GOV.UK</a>, 14 Oct 2026 · <a href="money-matters-cheat-sheet.html">Cheat sheet</a></small></div>
</div></section>
<div class="wrap"><a class="card feature" href="how-money-works.html"><span class="tag">New · Illustrated guide</span><h2 style="margin:.4rem 0">How money works, in pictures</h2><p>Where money comes from, what the Bank of England does, why prices rise – and what it all means for your savings, mortgage and investments. Ten simple steps.</p><span class="btn">Start the guide →</span></a>
<h2>Guides</h2><div class="grid g3">
<a class="card" href="savings.html"><span class="tag">Guide</span><h3>Savings</h3><p>Easy access, fixed bonds, cash ISAs, regular savers, FSCS protection and how savings interest is taxed.</p></a>
<a class="card" href="investments.html"><span class="tag">Guide</span><h3>Investments</h3><p>Stocks and shares ISAs, SIPPs, index funds and how platform fees work.</p></a>
<a class="card" href="mortgages.html"><span class="tag">Guide</span><h3>Mortgages</h3><p>Fixed vs tracker, when to look at remortgaging, and how repayments are worked out.</p></a>
<a class="card" href="gilts.html"><span class="tag">Guide</span><h3>Gilts</h3><p>What UK government bonds are and why low-coupon gilts can be tax-efficient.</p></a>
<a class="card" href="pensions.html"><span class="tag">Guide</span><h3>Pensions</h3><p>The State Pension, workplace pensions, SIPPs and why starting young matters so much.</p></a>
<a class="card" href="energy.html"><span class="tag">Guide</span><h3>Energy</h3><p>The Ofgem price cap, fixed vs variable deals, solar panels and home batteries.</p></a>
<a class="card" href="electric-cars.html"><span class="tag">Guide</span><h3>Electric cars</h3><p>Running costs, vehicle tax, company-car tax and the road to 2035.</p></a>
<a class="card" href="jargon.html"><span class="tag">Reference</span><h3>Jargon buster</h3><p>A searchable A–Z of around 60 money terms.</p></a>
<a class="card" href="resources.html"><span class="tag">Resources</span><h3>Downloads &amp; tools</h3><p>The free Money Matters cheat sheet: 2026/27 figures on one page, with a printable PDF.</p></a></div>
<h2 id="calculators">Calculators</h2><div class="grid g3">
<a class="card" href="gilts.html#calc"><h3>Gilt vs savings after tax</h3><p>Gross redemption yield, net yield for your tax band and the equivalent savings rate.</p></a>
<a class="card" href="mortgages.html#calc"><h3>Mortgage repayments</h3><p>Repayment or interest-only, optional overpayments and a balance chart.</p></a>
<a class="card" href="investments.html#calc"><h3>Platform fee impact</h3><p>Compare a percentage fee with a flat fee over the years.</p></a>
<a class="card" href="pensions.html#calc"><h3>Start age vs pot at 67</h3><p>See how the age you start saving changes your pension pot, after fees and inflation.</p></a>
<a class="card" href="energy.html#calc"><h3>Home battery payback</h3><p>Charge cheap overnight, use at peak: annual saving and payback.</p></a>
<a class="card" href="electric-cars.html#calc"><h3>EV charging cost</h3><p>Home vs public charging cost per mile and per year.</p></a></div>
<h2>Weekly best 3 rates – by email</h2><div class="card"><p>A short weekly email listing the three highest AERs we've checked. <strong>Coming soon</strong> – the form below is switched off and collects nothing.</p>
<form class="signup" aria-describedby="su-note" onsubmit="return false"><label class="sr" for="su">Email address</label><input id="su" type="email" placeholder="you@example.com" disabled><button class="btn" disabled>Coming soon</button></form><p id="su-note" class="hint">No data is collected. See our <a href="privacy.html">privacy page</a>.</p></div>
</div>''')
# ---------- SAVINGS ----------
pages["savings.html"] = page("savings.html", "Savings guide and rate table – MoneyBySharma", "UK savings explained: easy access, fixed bonds, cash ISAs, regular savers, FSCS £120,000 protection, the Personal Savings Allowance and starting rate.",
 ph("Savings","Savings, explained","How the main UK savings accounts work, how your money is protected, and how savings interest is taxed in 2026/27."), W(f'''
<h2 id="table">Savings rates comparison</h2>
<div class="banner" id="rates-banner" role="status">Example data – live rates coming soon</div>
<p>This table shows facts only and is ordered by AER (highest first) by default. Click a column heading to re-sort. It is not a recommendation – the right account depends on your circumstances. Always check the provider's own page before applying.</p>
<div class="filters"><div><label for="f-type">Account type</label><select id="f-type"><option value="">All types</option><option value="easy-access">Easy access</option><option value="notice">Notice</option><option value="fixed">Fixed bond</option><option value="cash-isa">Cash ISA</option><option value="regular-saver">Regular saver</option></select></div>
<div><label for="f-min">I can deposit up to (£)</label><input id="f-min" type="number" min="0" inputmode="numeric" placeholder="Any"></div>
<div class="check"><input id="f-fscs" type="checkbox"><label for="f-fscs">FSCS-protected only</label></div></div>
<div class="table-scroll" id="rates"><table><caption class="sr">Savings accounts</caption><thead><tr>
<th data-k="provider" scope="col"><button>Provider</button></th><th data-k="product" scope="col"><button>Product</button></th><th data-k="type" scope="col"><button>Type</button></th><th data-k="aer" scope="col"><button>AER ▾</button></th><th data-k="termMonths" scope="col"><button>Term</button></th><th data-k="minDeposit" scope="col"><button>Min deposit</button></th><th data-k="fscs" scope="col"><button>FSCS</button></th><th scope="col">Source</th><th data-k="checked" scope="col"><button>Checked</button></th></tr></thead><tbody></tbody></table></div>
<p class="hint" id="rates-count" aria-live="polite"></p>
<div class="cols"><div>
<h2 id="types">The main types of savings account</h2>
<h3>Easy access</h3><p>You can pay in and take money out when you like. The rate is usually variable, so it can go up or down at any time – often following changes to the Bank of England Bank Rate (currently {BR["rate"]:.2f}%). Some accounts limit the number of withdrawals.</p>
<h3>Notice accounts</h3><p>You must give notice (for example 30, 60 or 95 days) before withdrawing. Rates are usually variable.</p>
<h3>Fixed-rate bonds</h3><p>You lock money away for a set term (often 1–5 years) at a fixed rate. You usually cannot add money after opening, and early access is often not allowed or carries a penalty. Interest may be paid monthly, yearly or at maturity – which can affect which tax year it falls in.</p>
<h3>Cash ISAs</h3><p>Interest in an ISA is free of UK Income Tax and doesn't use your Personal Savings Allowance. For 2026/27 the overall ISA allowance is <strong>£20,000</strong>, which you can put entirely into a cash ISA. Cash ISAs come in easy access, notice and fixed versions. Check whether yours is "flexible" (lets you withdraw and replace money in the same tax year).</p>
<div class="flag"><strong>Changing from 6 April 2027:</strong> following the November 2025 Budget, the annual cash ISA limit falls to <strong>£12,000</strong> for people aged 64 or under at the end of the tax year. The overall ISA allowance stays at £20,000, and people aged 65 or over keep a £20,000 cash ISA limit. New rules will also stop transfers from stocks and shares ISAs into cash ISAs for under-65s. The regulations (SI 2026/1018) were made on 10 September 2026. None of this affects the 2026/27 tax year.</div>
<h3>Regular savers</h3><p>You pay in a fixed monthly amount (often £25–£500) for usually 12 months. Headline rates can look high, but because money goes in gradually, the interest you actually earn is roughly half what the AER suggests on the full year-end balance. Many require a current account with the same provider.</p>
<h2 id="fscs">FSCS protection: £120,000</h2><p>Since <strong>1 December 2025</strong>, the Financial Services Compensation Scheme protects eligible deposits up to <strong>£120,000 per person, per authorised firm</strong> (it was £85,000 from 2017 to 30 November 2025). Key points:</p>
<ul><li>Brands that share one banking licence count as one firm, so the limit covers your total across them.</li><li>Joint accounts: each holder is protected up to £120,000.</li><li>Temporary high balances (for example from a house sale or inheritance) can be protected up to £1.4 million for up to six months.</li><li>Cash ISAs with UK-authorised banks and building societies are covered.</li></ul>
<p>You can check a firm on the <a href="https://www.fscs.org.uk/check/check-your-money-is-protected/" rel="noopener">FSCS protection checker</a>.</p><div class="note"><strong>Choosing a current account?</strong> See <a href="bank-accounts.html">Bank accounts</a>: account types, switching with CASS, overdraft rules, an A–Z of banks and switching bonuses.</div>
<h2 id="tax">How savings interest is taxed (2026/27)</h2>
<table><caption class="sr">Savings tax allowances</caption><thead><tr><th scope="col">Allowance</th><th scope="col">2026/27</th></tr></thead><tbody>
<tr><td>Personal Allowance</td><td>£12,570 (reduced by £1 for every £2 of income over £100,000)</td></tr>
<tr><td>Starting rate for savings</td><td>0% on up to £5,000 of savings income – reduced by £1 for every £1 of other income above your Personal Allowance</td></tr>
<tr><td>Personal Savings Allowance – basic-rate taxpayer</td><td>£1,000</td></tr>
<tr><td>Personal Savings Allowance – higher-rate taxpayer</td><td>£500</td></tr>
<tr><td>Personal Savings Allowance – additional-rate taxpayer</td><td>£0</td></tr>
<tr><td>Savings tax rates above allowances</td><td>20% basic, 40% higher, 45% additional</td></tr></tbody></table>
<p><strong>Example:</strong> if your only income is a salary of £15,000, your other income is £2,430 above the Personal Allowance, so your starting rate band is £5,000 − £2,430 = £2,570. You could then earn £2,570 of interest at 0% plus £1,000 under the Personal Savings Allowance before paying tax.</p>
<div class="flag"><strong>Changing from 6 April 2027:</strong> savings income tax rates rise by 2 percentage points to <strong>22% / 42% / 47%</strong> (Finance Act 2026). The Personal Savings Allowance and starting rate figures above are for 2026/27. Scottish taxpayers: savings income uses UK (not Scottish) rates and bands.</div>
{src("rates","savtax","sav27","fscs","isa","cashisa","isasi","boe")}
</div><aside><div class="card toc"><h3>On this page</h3><a href="#table">Rates table</a><a href="#types">Account types</a><a href="#fscs">FSCS £120,000</a><a href="#tax">Savings tax</a><p class="hint" style="margin-top:.8rem">Compare gilts with savings on the <a href="gilts.html#calc">gilt calculator</a>.</p></div></aside></div>'''), scripts=("savings-table.js",))
# ---------- INVESTMENTS ----------
pages["investments.html"] = page("investments.html", "Investments: ISAs, SIPPs, index funds and fees – MoneyBySharma", "Stocks and shares ISAs, Lifetime ISAs, SIPP tax relief and access age, index funds and platform fees explained, with a fee-impact calculator.",
 ph("Investments","Investing basics","ISAs, pensions, index funds and fees – the rules for 2026/27 in plain English. Investments can fall as well as rise; your capital is at risk."), W(f'''
<div class="cols"><div>
<h2 id="isa">ISAs</h2><p>An Individual Savings Account shelters savings and investments from UK Income Tax and Capital Gains Tax. You must be a UK resident aged 18 or over (16 or over for a cash ISA under current rules).</p>
<ul><li><strong>Allowance:</strong> £20,000 in 2026/27, which can be split across cash, stocks and shares, Innovative Finance and Lifetime ISAs. Unused allowance does not roll over. The government has said the £20,000 limit stays until April 2031.</li>
<li><strong>Stocks and shares ISA:</strong> holds funds, shares, investment trusts, bonds and gilts. Values go up and down.</li>
<li><strong>Lifetime ISA (LISA):</strong> open aged 18–39 and pay in up to £4,000 a year (counts towards the £20,000) until age 50. The government adds a 25% bonus (up to £1,000 a year). Withdrawals for a first home (up to £450,000) or from age 60 are bonus-free; other withdrawals face a 25% charge, which means you can get back less than you paid in.</li>
<li><strong>Junior ISA:</strong> £9,000 a year for under-18s.</li>
<li>Since 6 April 2024 you can pay into more than one ISA of the same type in a tax year, as long as you stay within the overall limit.</li></ul>
<div class="flag"><strong>From 6 April 2027:</strong> under-65s will be able to put at most £12,000 of the £20,000 into cash ISAs, and interest on cash held inside a stocks and shares ISA will face a charge. The November 2025 Budget also said the government would consult on a new, simpler ISA product for first-time buyers to replace the Lifetime ISA. That change isn't confirmed in law yet, so check GOV.UK for the latest.</div>
<h2 id="sipp">SIPPs and pension tax relief</h2><p>See also our <a href="pensions.html">Pensions guide</a> for the State Pension, workplace pensions and a start-age calculator. A Self-Invested Personal Pension is a personal pension where you choose the investments.</p>
<ul><li><strong>Tax relief:</strong> personal contributions get relief at your marginal rate. With "relief at source", you pay £80 and the provider claims £20 basic-rate relief from HMRC, so £100 goes in. Higher- and additional-rate taxpayers claim the extra through Self Assessment.</li>
<li><strong>Limits:</strong> relief applies to contributions up to 100% of your UK relevant earnings, or £3,600 gross if you have little or no earnings. The annual allowance (all contributions, including employer) is <strong>£60,000</strong>, tapered for very high incomes. Once you've flexibly accessed a pension, the Money Purchase Annual Allowance of £10,000 applies.</li>
<li><strong>Access age:</strong> the normal minimum pension age is <strong>55</strong>, rising to <strong>57 on 6 April 2028</strong> (some people have a protected pension age).</li>
<li><strong>Tax-free cash:</strong> usually up to 25% of your pension, capped by the Lump Sum Allowance of £268,275. The rest is taxed as income when you take it.</li></ul>
<p class="hint">The November 2025 Budget announced that salary-sacrifice pension contributions above £2,000 a year will attract National Insurance from April 2029. This affects workplace schemes, not the income-tax relief described above.</p>
<h2 id="index">Index funds</h2><p>An index (tracker) fund aims to match a market index, such as the FTSE All-Share or a global index, rather than trying to beat it. They usually have lower ongoing charges than actively managed funds. The value still rises and falls with the market, and the fund's return will be slightly below the index after charges. Things to compare: the ongoing charges figure (OCF), how closely it tracks its index ("tracking difference"), whether income is paid out or reinvested ("inc" or "acc" units), and whether it's a fund (OEIC/unit trust) or an exchange-traded fund (ETF).</p>
<h2 id="fees">Platform fees explained</h2><p>Your total cost is usually the <strong>platform fee</strong> (for holding your account) + the <strong>fund's ongoing charge</strong> + any <strong>dealing charges</strong>. Platforms usually charge either:</p>
<ul><li><strong>a percentage</strong> of your pot each year (often tiered, sometimes capped), which suits smaller pots, or</li><li><strong>a flat fee</strong> in pounds, which costs relatively less as your pot grows.</li></ul>
<p>We don't list specific platform prices here until we've verified and sourced them. Check each platform's current charges page.</p>
<section class="calc" id="calc" aria-labelledby="fee-h"><h3 id="fee-h" style="margin-top:0">Fee-impact calculator: percentage fee vs flat fee</h3>
<form id="fee-form" class="fields">
<div><label for="fee-start">Starting pot (£)</label><input id="fee-start" type="number" min="0" step="100" value="10000"></div>
<div><label for="fee-years">Years</label><input id="fee-years" type="number" min="1" max="60" value="10"></div>
<div><label for="fee-growth">Assumed growth before fees (% a year)</label><input id="fee-growth" type="number" step="0.1" value="5"></div>
<div><label for="fee-pct">Percentage platform fee (% a year)</label><input id="fee-pct" type="number" step="0.01" min="0" value="0.45"></div>
<div><label for="fee-flat">Flat platform fee (£ a year)</label><input id="fee-flat" type="number" step="1" min="0" value="120"></div></form>
<div class="results" aria-live="polite"><div class="res"><span>With % fee</span><b id="fee-r-pct">–</b></div><div class="res"><span>With flat fee</span><b id="fee-r-flat">–</b></div><div class="res"><span>No platform fee</span><b id="fee-r-none">–</b></div></div>
<p id="fee-r-text"></p>
<p class="hint"><strong>Assumptions:</strong> a single lump sum, no further contributions or withdrawals; growth compounds once a year at a steady rate (real returns vary and can be negative); the percentage fee is taken on the year-end value; the flat fee is taken at each year end; fund charges, dealing costs, inflation and tax are ignored. Figures are illustrations, not forecasts.</p></section>
{src("rates","isa","cashisa","tfs","lisa","pentax","aa","nmpa")}
</div><aside><div class="card toc"><h3>On this page</h3><a href="#isa">ISAs</a><a href="#sipp">SIPPs</a><a href="#index">Index funds</a><a href="#fees">Platform fees</a><a href="#calc">Fee calculator</a></div></aside></div>'''), scripts=("calc.js","calc-ui.js"))
# ---------- MORTGAGES ----------
pages["mortgages.html"] = page("mortgages.html", "Mortgages: fixed vs tracker and repayment calculator – MoneyBySharma", "Fixed vs tracker mortgages, remortgage timing and a repayment / interest-only calculator with overpayments and an amortisation chart.",
 ph("Mortgages","Mortgages, explained","How fixed and tracker deals work, when to start thinking about remortgaging, and what your monthly payment might be."), W(f'''
<div class="cols"><div>
<h2 id="types">Fixed vs tracker</h2>
<div class="grid g2"><div class="card"><h3>Fixed rate</h3><p>Your interest rate stays the same for a set period (commonly 2, 3, 5 or 10 years), so payments are predictable. Leaving early usually means an early repayment charge (ERC). If rates fall, you don't benefit until the deal ends.</p></div>
<div class="card"><h3>Tracker</h3><p>Your rate moves with the Bank of England Bank Rate (currently {BR["rate"]:.2f}%) plus a set margin. Payments rise and fall with Bank Rate. Some trackers have no ERCs; some have a "collar" (a minimum rate).</p></div></div>
<p>When a deal ends you usually move to the lender's <strong>standard variable rate (SVR)</strong>, which is often higher.</p>
<h2 id="remortgage">Remortgage timing</h2><ul><li>Many lenders let you secure a new deal about <strong>3–6 months</strong> before your current one ends – check your lender's policy.</li><li>Look up any ERC and its end date in your mortgage offer.</li><li>Your loan-to-value (LTV) matters: a lower LTV often unlocks lower rates.</li><li>Factor in arrangement, valuation and legal fees – a lower rate with a large fee isn't always cheaper over the deal.</li><li>Product transfers (staying with your lender) may need less paperwork; switching lenders means a fresh affordability check.</li></ul>
<p>Free, impartial guidance is available from <a href="{S["mas"][1]}" rel="noopener">MoneyHelper</a>. Mortgage advice is regulated; MoneyBySharma doesn't give it.</p>
<section class="calc" id="calc" aria-labelledby="m-h"><h3 id="m-h" style="margin-top:0">Mortgage repayment calculator</h3>
<form id="mort-form" class="fields">
<div><label for="mort-amt">Loan amount (£)</label><input id="mort-amt" type="number" min="1000" step="1000" value="200000"></div>
<div><label for="mort-rate">Interest rate (% a year)</label><input id="mort-rate" type="number" min="0" step="0.01" value="5"></div>
<div><label for="mort-years">Term (years)</label><input id="mort-years" type="number" min="1" max="40" value="25"></div>
<div><label for="mort-type">Type</label><select id="mort-type"><option value="repayment">Repayment</option><option value="interest">Interest-only</option></select></div>
<div><label for="mort-over">Monthly overpayment (£, optional)</label><input id="mort-over" type="number" min="0" step="10" value="0"></div></form>
<div class="results" aria-live="polite"><div class="res"><span>Monthly payment</span><b id="mort-r-monthly">–</b></div><div class="res"><span>Total interest</span><b id="mort-r-int">–</b></div><div class="res"><span id="mort-r-term-label">Time to clear</span><b id="mort-r-term">–</b></div></div>
<h4>Outstanding balance by year</h4><div class="chart-box"><canvas id="mort-chart" style="width:100%;height:100%" role="img" aria-describedby="mort-chart-desc"></canvas></div><p class="sr" id="mort-chart-desc"></p>
<p class="hint"><strong>Assumptions:</strong> the rate stays the same for the whole term (in reality deals end and rates change); interest is calculated monthly at one-twelfth of the annual rate; overpayments are added on top of the monthly payment and reduce the term, not the payment; fees, ERCs and overpayment limits (often 10% a year) are ignored. For interest-only, the loan must be repaid in full at the end of the term.</p></section>
{src("boe","mas")}
</div><aside><div class="card toc"><h3>On this page</h3><a href="#types">Fixed vs tracker</a><a href="#remortgage">Remortgage timing</a><a href="#calc">Repayment calculator</a></div></aside></div>'''), scripts=("calc.js","calc-ui.js"))
# ---------- GILTS ----------
pages["gilts.html"] = page("gilts.html", "Gilts explained and gilt vs savings calculator – MoneyBySharma", "What UK gilts are, why low-coupon gilts can be tax-efficient, and a calculator comparing gilt yields with savings after tax.",
 ph("Gilts","Gilts, explained","UK government bonds, how they're taxed, and how a gilt held to maturity compares with a savings account after tax."), W(f'''
<div class="cols"><div>
<h2 id="what">What is a gilt?</h2><p>A gilt is a bond issued by the UK government through the Debt Management Office (DMO). A conventional gilt pays a fixed <strong>coupon</strong> (interest) twice a year on each £100 of nominal value and repays <strong>£100</strong> at its maturity date. Gilts trade on the market, so their price moves – mainly with interest rates. If you sell before maturity you could get back less than you paid; if you hold to maturity you receive £100 per £100 nominal.</p>
<h2 id="tax">Why low-coupon gilts can be tax-efficient</h2><ul><li><strong>Capital gains on gilts are exempt from Capital Gains Tax</strong> for individuals.</li><li><strong>The coupon is taxable</strong> as savings income (it can use your Personal Savings Allowance and starting rate).</li></ul>
<p>A low-coupon gilt trading below £100 delivers most of its return as a tax-free gain at maturity rather than as taxable interest. For a higher- or additional-rate taxpayer, that can mean a better after-tax return than a savings account paying a similar headline rate. The calculator below shows the effect. Inside an ISA or SIPP, the tax difference doesn't apply.</p>
<p>Example of a real low-coupon gilt in issue: <strong>{html.escape(lowc["name"])}</strong> – {lowc["coupon"]}% coupon, maturing {d(lowc["maturity"])} (DMO data, close of business {d(GI["closeOfBusiness"])}). This is shown to illustrate the idea, not as a recommendation to buy.</p>
<section class="calc" id="calc" aria-labelledby="g-h"><h3 id="g-h" style="margin-top:0">Gilt vs savings after tax</h3>
<form id="gilt-form" class="fields">
<div style="grid-column:1/-1"><label for="gilt-pick">Pick a gilt in issue (optional)</label><select id="gilt-pick"><option value="">– Enter details manually –</option></select><p class="hint" id="gilt-src"></p></div>
<div><label for="gilt-price">Clean price per £100 nominal (£) <span class="hint">from your broker or the DMO</span></label><input id="gilt-price" type="number" step="0.01" min="1" value="95"></div>
<div><label for="gilt-coupon">Coupon (% a year)</label><input id="gilt-coupon" type="number" step="0.001" min="0" value="{lowc["coupon"]}"></div>
<div><label for="gilt-mat">Maturity date</label><input id="gilt-mat" type="date" value="{lowc["maturity"]}"></div>
<div><label for="gilt-band">Your tax rate on savings income</label><select id="gilt-band">
<option value="0">0% – within allowances / non-taxpayer</option><option value="20">20% – basic rate (2026/27)</option><option value="40" selected>40% – higher rate (2026/27)</option><option value="45">45% – additional rate (2026/27)</option>
<option value="22">22% – basic rate (from 6 Apr 2027)</option><option value="42">42% – higher rate (from 6 Apr 2027)</option><option value="47">47% – additional rate (from 6 Apr 2027)</option></select></div></form>
<div class="results" aria-live="polite"><div class="res"><span>Gross redemption yield</span><b id="gilt-r-gry">–</b></div><div class="res"><span>Net yield after tax</span><b id="gilt-r-net">–</b></div><div class="res"><span>Equivalent gross savings rate (AER)</span><b id="gilt-r-eq">–</b></div></div>
<p id="gilt-r-text"></p>
<p class="hint"><strong>How it works:</strong> bought today and held to maturity. You pay the clean price plus accrued interest (dirty price). The gross redemption yield (GRY) uses semi-annual compounding (the market convention). The net yield taxes each coupon at your chosen rate, leaves the gain to £100 untaxed (CGT-exempt), and is shown as an annual effective rate. The equivalent savings rate is the AER a savings account would need to pay to match it after tax: net ÷ (1 − tax rate). Simplifications: coupon dates are counted back from maturity, ex-dividend periods and dealing costs are ignored, and the Accrued Income Scheme (which can apply if your gilts' total nominal value is over £5,000) isn't modelled. The 2027/28 options use the higher savings rates legislated for that year. If you pay 0% on all coupons, the "equivalent" is simply the gross figure.</p></section>
<div class="note">Prices aren't fetched automatically: the DMO's free published reference data gives each gilt's name, coupon and maturity (refreshed when the site is rebuilt), but not live dealing prices. Enter the current price from your broker.</div>
{src("giltcgt","savtax","rates","sav27","dmo","aischeme")}
</div><aside><div class="card toc"><h3>On this page</h3><a href="#what">What is a gilt?</a><a href="#tax">Tax efficiency</a><a href="#calc">Calculator</a></div></aside></div>'''), scripts=("calc.js","calc-ui.js"))
# ---------- JARGON ----------
G = [("AER","Annual Equivalent Rate – the interest you'd earn over a year if interest were compounded, so you can compare accounts that pay interest at different intervals."),
("Accrued interest","Interest built up on a bond since its last coupon date. The buyer pays it to the seller on top of the clean price."),
("Active fund","A fund whose manager picks investments aiming to beat a benchmark. Usually charges more than an index fund."),
("Additional-rate taxpayer","Someone with taxable income over £125,140 (2026/27, rest of UK)."),
("Amortisation","Paying off a loan gradually through regular payments that cover interest and part of the capital."),
("Annual allowance","The most that can be paid into your pensions each tax year with tax relief – £60,000 for most people in 2026/27."),
("Annuity","A product that turns a pension pot into a guaranteed income, usually for life."),
("Arrangement fee","A fee some lenders charge to set up a mortgage deal."),
("Bank Rate","The Bank of England's main interest rate, set by its Monetary Policy Committee. It influences savings and mortgage rates."),
("Basic-rate taxpayer","Someone whose taxable income falls in the basic-rate band (£12,571 to £50,270 in 2026/27 for most people, rest of UK)."),
("Bond","A loan to a government or company that pays interest and returns your money at a set date."),
("Capital Gains Tax (CGT)","Tax on the profit when you sell certain assets for more than you paid. The annual exempt amount is £3,000 in 2026/27. Gilts are exempt."),
("Cash ISA","An ISA holding cash savings. Interest is tax-free."),
("Clean price","A bond's quoted price, excluding accrued interest."),
("Collar","A minimum rate below which a tracker mortgage won't fall."),
("Compound interest","Interest earned on previous interest as well as on your original money."),
("Coupon","The fixed interest a bond pays, as a percentage of its nominal (face) value."),
("Defined benefit pension","A pension paying an income based on salary and years of service (a 'final salary' or 'career average' scheme)."),
("Defined contribution pension","A pension where the pot depends on contributions and investment growth. SIPPs and most workplace pensions are this type."),
("Dirty price","A bond's price including accrued interest – what you actually pay."),
("Dividend","A payment a company makes to its shareholders out of profits."),
("Dividend Allowance","Dividend income you can receive tax-free each year – £500 in 2026/27."),
("Drawdown","Taking income directly from your invested pension pot while the rest stays invested."),
("Early repayment charge (ERC)","A fee for paying off or leaving a mortgage deal early."),
("Easy access account","A savings account that lets you withdraw money whenever you like."),
("ETF","Exchange-traded fund – a fund that trades on a stock exchange like a share."),
("Equity","Your share of a property's value that you own outright; also another word for shares."),
("FCA","Financial Conduct Authority – the UK regulator for financial firms and advice."),
("Fixed-rate bond","A savings account paying a fixed rate for a set term, usually with no access until it ends."),
("Fixed-rate mortgage","A mortgage whose interest rate stays the same for a set period."),
("Flexible ISA","An ISA that lets you withdraw money and pay it back in the same tax year without using more allowance."),
("FSCS","Financial Services Compensation Scheme – protects eligible deposits up to £120,000 per person, per authorised firm (from 1 December 2025)."),
("Gilt","A bond issued by the UK government."),
("Gross","Before tax or charges are taken off."),
("Gross redemption yield (GRY)","The annual return on a bond held to maturity, including coupons and any gain or loss to its £100 redemption value, before tax."),
("Higher-rate taxpayer","Someone with taxable income between £50,271 and £125,140 (2026/27, rest of UK)."),
("Index","A measure of a market's performance, such as the FTSE 100."),
("Index fund","A fund that aims to track an index rather than beat it. Also called a tracker fund."),
("Inflation","The rate at which prices rise over time, usually measured by CPI in the UK."),
("Interest-only mortgage","You pay only the interest each month, so the full loan must be repaid at the end."),
("ISA","Individual Savings Account – a tax-free wrapper for savings or investments. Allowance £20,000 in 2026/27."),
("Junior ISA","A tax-free account for under-18s; £9,000 a year in 2026/27."),
("Lifetime ISA (LISA)","An ISA for 18–39s to open, with a 25% government bonus on up to £4,000 a year, for a first home or retirement from 60."),
("Loan-to-value (LTV)","The size of a mortgage as a percentage of the property's value."),
("Lump Sum Allowance","The cap on tax-free cash you can take from pensions – £268,275 for most people."),
("Maturity","The date a bond or fixed account ends and your money is repaid."),
("Money Purchase Annual Allowance","A reduced pension annual allowance (£10,000) after you've flexibly accessed a defined contribution pension."),
("Net","After tax or charges have been taken off."),
("Nominal value","A bond's face value – usually £100 for gilts – which is repaid at maturity."),
("Normal minimum pension age","The earliest age most people can take pension benefits: 55, rising to 57 on 6 April 2028."),
("Notice account","A savings account where you must give notice before withdrawing."),
("OCF","Ongoing charges figure – a fund's yearly running costs as a percentage."),
("Overpayment","Paying more than your required mortgage payment to clear the loan sooner."),
("Personal Allowance","Income you can receive tax-free each year – £12,570 in 2026/27, reduced above £100,000 of income."),
("Personal Savings Allowance (PSA)","Savings interest you can earn tax-free: £1,000 basic rate, £500 higher rate, £0 additional rate (2026/27)."),
("Platform","A website or app for buying and holding investments, such as funds and shares, in ISAs, SIPPs and general accounts."),
("Regular saver","An account where you pay in a set amount each month, usually for a year."),
("Relief at source","How personal pension tax relief is usually given: you pay 80% and the provider claims 20% basic-rate relief."),
("Remortgage","Switching your mortgage to a new deal, with your current lender or a new one."),
("SIPP","Self-Invested Personal Pension – a personal pension where you choose the investments."),
("Standard variable rate (SVR)","A lender's default mortgage rate, often applied when a deal ends."),
("Starting rate for savings","Up to £5,000 of savings interest taxed at 0%, reduced by other income above your Personal Allowance."),
("Stocks and shares ISA","An ISA holding investments such as funds and shares. Your capital is at risk."),
("Tax year","In the UK, runs from 6 April to 5 April the following year."),
("Tracker mortgage","A mortgage whose rate follows Bank Rate plus a set margin."),
("Yield","The income from an investment as a percentage of its price."),
("Auto-enrolment","The legal duty on employers to put eligible workers (aged 22 to State Pension age, earning over £10,000 a year) into a workplace pension."),
("Benefit in kind (BIK)","A taxable perk from your employer, such as a company car. Tax is based on a percentage of the car's list price – 4% for zero-emission cars in 2026/27."),
("Battery degradation","The gradual loss of a battery's usable capacity as it ages and is cycled."),
("Economy 7","An electricity meter and tariff with a cheaper rate for seven hours overnight."),
("eVED","Electric Vehicle Excise Duty – a proposed pay-per-mile charge on electric (3p) and plug-in hybrid (1.5p) cars from April 2028. Draft legislation, not yet law."),
("Expensive car supplement","An extra £440 a year of vehicle tax in years 2 to 6 for cars with a list price over £40,000 (over £50,000 for zero-emission cars from April 2026)."),
("Junior SIPP","A SIPP opened for a child by a parent or guardian. Up to £2,880 a year can go in, topped up to £3,600 by tax relief."),
("kWh","Kilowatt-hour – the unit energy is billed in. A 1 kW appliance running for an hour uses 1 kWh."),
("kWp","Kilowatt peak – a solar system's maximum output in ideal conditions."),
("Pound-cost averaging","Investing a fixed amount regularly, so you buy more units when prices are low and fewer when they're high."),
("Price cap","Ofgem's limit on the unit rates and standing charges suppliers can charge on standard variable (default) tariffs."),
("Qualifying year","A tax year in which you paid or were credited with enough National Insurance to count towards your State Pension."),
("Round-trip efficiency","The share of energy put into a battery that you get back out. 90% means 10 kWh in gives 9 kWh out."),
("Salary sacrifice","Giving up some salary in exchange for a non-cash benefit, such as pension contributions or an electric car."),
("Smart Export Guarantee (SEG)","A scheme requiring larger electricity suppliers to pay small generators, such as homes with solar panels, for electricity exported to the grid."),
("Standing charge","A fixed daily charge for being connected to the energy supply, whatever you use."),
("State Pension","A regular payment from the government once you reach State Pension age, based on your National Insurance record. The full new State Pension is £241.30 a week in 2026/27."),
("Time-of-use tariff","An energy tariff whose unit rate changes by time of day, often with cheap overnight hours."),
("Unit rate","The price you pay for each kWh of electricity or gas."),
("Vehicle-to-grid (V2G)","Technology that lets an electric car send power from its battery back to the home or the grid."),
("ZEV mandate","Rules requiring carmakers to make a rising share of new car and van sales zero-emission: 80% of new cars by 2030 and 100% by 2035.")]
G += [("Arranged overdraft","A borrowing limit on a current account agreed with your bank in advance. Since April 2020 it's charged as a single annual interest rate."),
("Unarranged overdraft","Going overdrawn without an agreed limit, or beyond it. The interest rate can't be higher than the arranged overdraft rate."),
("Basic bank account","A fee-free account with no overdraft. Nine designated UK banks must offer one to eligible people who can't get a standard account."),
("Current Account Switch Service (CASS)","The free service that moves your current account, payments and Direct Debits to a new bank in 7 working days, with a guarantee."),
("Packaged bank account","A current account with a monthly fee that includes extras such as travel or phone insurance."),
("Financial association","A link on your credit files with someone you share credit with, such as a joint account. It stays until you ask for it to be removed."),
("Banking licence","A bank's authorisation. The FSCS limit applies per licence, so brands sharing one licence count as one bank."),
("Temporary high balance","A large sum from a life event, such as a house sale, protected by the FSCS up to £1.4 million for six months."),
("Switching bonus","A cash payment some banks offer when you switch your current account and meet set conditions. Offers change often."),
("Refused payment fee","A charge for refusing a payment because there isn't enough money. The FCA says it should reflect the bank's actual costs.")]
G += [("Representative APR","The APR at or below which a lender expects at least 51% of people accepted through an advert to be charged. Others may get a higher rate."),
("Balance transfer","Moving debt from one credit card to another, often at 0% for a period in exchange for a one-off fee."),
("Money transfer","Moving money from a credit card into a bank account, usually for a fee."),
("Minimum payment","The smallest amount you must pay each month to keep a credit card account up to date. Paying only this makes debt last much longer."),
("Persistent debt","FCA term for when, over 18 months, you've paid more in interest, fees and charges than you've repaid of the borrowing on a card."),
("Section 75","The Consumer Credit Act rule that makes a card provider jointly liable for purchases over £100 and up to £30,000 paid at least partly by credit card."),
("Chargeback","A voluntary card-scheme process for asking your card provider to reverse a payment. It covers debit and credit cards, with time limits."),
("Soft search","A credit check only you can see. It doesn't affect your credit score. Used by eligibility checkers."),
("Hard search","A credit check made when you apply for credit. Other lenders can see it."),
("Credit reference agency (CRA)","A company holding credit records. The three main UK CRAs are Equifax, Experian and TransUnion."),
("Avios","Reward points used by British Airways and some other airlines, collected on some credit cards."),
("Foreign transaction fee","A charge, often a percentage, added when you spend in a foreign currency.")]
G += [("FTTC (fibre to the cabinet)","Broadband with fibre to the street cabinet and copper to your home. Speed falls with distance from the cabinet."),
("FTTP (full fibre)","Broadband with fibre all the way into your home – the fastest widely available connection."),
("Mbps","Megabits per second – the unit broadband speed is measured in."),
("PSTN switch-off","The closure of the UK's analogue phone network. Openreach's deadline is 31 January 2027; landlines move to digital."),
("Social tariff","A cheaper broadband or phone package for people on Universal Credit and some other benefits."),
("One Touch Switch","The broadband and landline switching process since September 2024: you only contact your new provider."),
("PAC code","Porting Authorisation Code – text PAC to 65075 to switch mobile network and keep your number."),
("STAC code","Service Termination Authorisation Code – text STAC to 75075 to switch mobile network without keeping your number."),
("MVNO","Mobile virtual network operator – a mobile provider that uses another company's network, such as giffgaff or Tesco Mobile."),
("SIM-only","A mobile plan for calls, texts and data without a handset."),
("Split contract","A mobile contract with the handset and airtime on separate plans, so you pay only for airtime once the phone is paid off."),
("Roaming","Using your mobile abroad on another country's network. Charges vary by provider.")]
G.sort(key=lambda t: t[0].lower())
letters = sorted(set(t[0][0].upper() for t in G))
gl = "".join(f'<dt id="t-{i}" data-l="{t[0][0].upper()}">{html.escape(t[0])}</dt><dd>{html.escape(t[1])}</dd>' for i,t in enumerate(G))
pages["jargon.html"] = page("jargon.html", "Jargon buster: A–Z money glossary – MoneyBySharma", "A searchable A–Z glossary of UK personal-finance terms.",
 ph("Jargon buster","Jargon buster",f"{len(G)} money terms in plain English. Start typing to search."), W(f'''
<div style="max-width:760px"><label for="gq">Search the glossary</label><input id="gq" type="search" placeholder="e.g. AER, ISA, coupon" autocomplete="off"><p class="hint" id="gcount" aria-live="polite"></p>
<nav class="az" aria-label="Jump to letter">{"".join(f'<a href="#L-{l}">{l}</a>' for l in letters)}</nav>
<dl class="gloss" id="gloss">{gl}</dl>
<p class="src">Figures in definitions are for 2026/27 and are sourced on the relevant guide pages (checked {CHECKED}).</p></div>
<script>(function(){{var q=document.getElementById('gq'),dts=[].slice.call(document.querySelectorAll('#gloss dt')),c=document.getElementById('gcount'),seen={{}};dts.forEach(function(dt){{var l=dt.dataset.l;if(!seen[l]){{seen[l]=1;var a=document.createElement('span');a.id='L-'+l;dt.prepend(a)}}}});
function f(){{var s=q.value.trim().toLowerCase(),n=0;dts.forEach(function(dt){{var dd=dt.nextElementSibling,m=!s||(dt.textContent+' '+dd.textContent).toLowerCase().indexOf(s)>-1;dt.hidden=dd.hidden=!m;if(m)n++}});c.textContent=n+' of '+dts.length+' terms'}}q.addEventListener('input',f);f()}})();</script>'''))
# ---------- RESOURCES ----------
pages["resources.html"] = page("resources.html", "Resources – MoneyBySharma", "The free MoneyBySharma Money Matters cheat sheet: UK personal finance figures for 2026/27 on one page, with a printable PDF.",
 ph("Resources","Resources","Free resources from MoneyBySharma."), W('''
<div class="grid g3" style="margin-top:1.5rem">
<div class="card"><span class="tag">Free</span><h3>Money Matters cheat sheet 2026/27</h3><p>The key UK allowances, tax bands, protections and rates on one page, each with its source and "as at" date, plus a money basics checklist.</p>
<p><a class="btn" href="money-matters-cheat-sheet.html">View the cheat sheet</a></p><p><a href="assets/money-matters-cheat-sheet-2026-27.pdf" download>Download the printable PDF (A4)</a></p></div>
<div class="card"><span class="tag">Free PDF</span><h3>Explained Simply: Money Matters</h3><p>A free illustrated guide by Subhash Sharma covering payslips and tax, budgeting, bank accounts, saving and ISAs, borrowing, student loans, pensions, investing and scams, with figures checked for 2026/27.</p>
<p><a class="btn" href="assets/explained-simply-money-matters.pdf" download>Download the guide</a></p><p class="hint">PDF, 1.7 MB, 15 pages.</p></div></div>
<p class="hint" style="margin-top:1rem"><strong>Information only – not financial advice.</strong> These resources give general information, not regulated financial advice, and MoneyBySharma isn't authorised or regulated by the FCA. Figures can change, so check the current rules before making decisions.</p>'''))
# ---------- ABOUT / DISCLAIMER / PRIVACY ----------
pages["about.html"] = page("about.html", "About – MoneyBySharma", "Why I started MoneyBySharma, and how I check the figures.", ph("About","About MoneyBySharma","Plain-English UK money information, by Subhash Sharma."), W(f'''
<div style="max-width:760px"><h2>Why I started MoneyBySharma</h2>
<p>Hello, I'm Subhash Sharma. I'm passionate about helping everyone become financially free – and I believe that starts with understanding what money actually is and how it works.</p>
<p>How money works should be taught in schools, but for most of us it isn't. So I've built this site to explain it in plain English: how savings, pensions, mortgages, gilts and investing fit together, without the jargon.</p>
<p>My hope is to reach as many individuals and families as possible. If you're new to all this, a good place to start is my illustrated guide, <a href="how-money-works.html"><strong>How money works, in pictures</strong></a>.</p>
<p>For a one-page summary of the key figures, see my free <a href="money-matters-cheat-sheet.html">Money Matters cheat sheet</a> on the <a href="resources.html">Resources</a> page.</p>
<h2>What this site isn't</h2><p>MoneyBySharma gives information only, not regulated financial advice. It isn't a financial adviser, broker or comparison service, and it isn't authorised or regulated by the Financial Conduct Authority (FCA). I don't recommend products or tell you what to buy, and comparison tables show facts only.</p>
<h2>How I check the figures</h2><p>Every allowance, rate and limit is checked against official sources – GOV.UK, HMRC, legislation.gov.uk, the FSCS, the Bank of England, the ONS and the UK Debt Management Office – and linked with the date I checked it. Figures on this site were last checked on {CHECKED}. The Bank Rate, gilt and inflation data are refreshed automatically whenever the site is rebuilt. If you spot an error, please let me know at <a href="mailto:hello@moneybysharma.co.uk">hello@moneybysharma.co.uk</a>.</p>
<p><a href="disclaimer.html">Read the full disclaimer</a> · <a href="privacy.html">Privacy</a></p></div>'''))
pages["disclaimer.html"] = page("disclaimer.html", "Disclaimer – MoneyBySharma", "Important information about using MoneyBySharma.", ph("Disclaimer","Disclaimer","Please read this before relying on anything on this site."), W(f'''
<div style="max-width:760px"><h2>Information, not advice</h2><p>Everything on MoneyBySharma is general information for people in the UK. It isn't regulated financial, tax, mortgage or legal advice, and it doesn't take your personal circumstances into account.</p>
<h2>Not FCA authorised</h2><p>MoneyBySharma isn't authorised or regulated by the Financial Conduct Authority. Nothing here is an invitation or inducement to buy or sell any investment. To get regulated advice, use an adviser listed on the <a href="{S["fcareg"][1]}" rel="noopener">FCA Register</a>. Free guidance is available from <a href="https://www.moneyhelper.org.uk/" rel="noopener">MoneyHelper</a>.</p>
<h2>Investments carry risk</h2><p>The value of investments, including gilts sold before maturity, can fall as well as rise, and you may get back less than you invest. Past performance isn't a reliable guide to future results.</p>
<h2>Tax</h2><p>Tax treatment depends on your individual circumstances and may change in future. Figures are for the 2026/27 tax year unless stated. Scottish income tax bands differ for non-savings income.</p>
<h2>Accuracy and calculators</h2><p>We work hard to keep figures accurate and sourced, but we can't guarantee that everything is complete or up to date. Calculators give illustrations based on stated assumptions, not forecasts or quotes. Any example rates in the comparison table are clearly marked as placeholders and aren't real.</p>
<h2>Links</h2><p>We link to external sites, such as GOV.UK and the FSCS, for convenience. We aren't responsible for their content.</p></div>'''))
pages["privacy.html"] = page("privacy.html", "Privacy – MoneyBySharma", "MoneyBySharma uses no cookies and no analytics.", ph("Privacy","Privacy","Short version: we don't use cookies, we don't track you and we don't collect your data."), W('''
<div style="max-width:760px"><h2>No cookies, no analytics</h2><p>This site sets no cookies and uses no analytics, advertising or tracking scripts. All fonts, scripts and data are served from this site itself – there are no third-party embeds.</p>
<h2>Calculators</h2><p>Calculator inputs stay in your browser and are never sent anywhere.</p>
<h2>Email sign-up</h2><p>The "weekly best 3 rates" sign-up is switched off ("coming soon") and collects nothing. If we launch it, we'll update this page first to explain what's collected and why.</p>
<h2>Hosting</h2><p>The site is hosted on GitHub Pages. Like any web host, GitHub may process technical data such as IP addresses to deliver and secure the site – see the <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">GitHub Privacy Statement</a>.</p>
<h2>Contacting us</h2><p>You can email <a href="mailto:hello@moneybysharma.co.uk">hello@moneybysharma.co.uk</a>. If you do, your email address and message are used only to reply to you. They aren't added to any mailing list or shared.</p>
<h2>External links</h2><p>Links to other sites (for example GOV.UK or the FSCS) are covered by those sites' own privacy policies.</p></div>'''))
pages["404.html"] = page("404.html", "Page not found – MoneyBySharma", "Page not found.", ph("Not found","Page not found","Sorry, that page doesn't exist."), W('<p style="margin-top:1.5rem"><a class="btn" href="index.html">Go to the home page</a></p>'))
exec(open("scripts/pages2.py").read())
exec(open("scripts/pages3.py").read())
exec(open("scripts/pages4.py").read())
exec(open("scripts/pages5.py").read())
exec(open("scripts/pages6.py").read())
exec(open("scripts/pages7.py").read())
exec(open("scripts/pages8.py").read())
exec(open("scripts/pages9.py").read())
exec(open("scripts/pages10.py").read())
exec(open("scripts/pages11.py").read())
pages["tools.html"] = page("tools.html","Tools – MoneyBySharma","Free tools by Subhash Sharma, including Garmin Fitness Insights.",
 ph("Tools","Tools","Free tools by Subhash Sharma."), W('''
<div class="grid g3" style="margin-top:1.5rem">
<div class="card"><span class="tag">Free tool</span><h3>Garmin Fitness Insights</h3><p>Upload your Garmin export and see your activity trends. Everything is processed in your browser, and nothing is uploaded.</p>
<p><a class="btn" href="tools/garmin-insights/">Open Garmin Fitness Insights</a></p></div>
<div class="card"><span class="tag">Experiment</span><h3>Paper trading experiment</h3><p>A log of two fake-money trading books: trades, positions and totals. Experiment only, not advice or a recommendation.</p>
<p><a class="btn" href="paper-trading.html">View the experiment</a></p></div></div>
<p class="hint" style="margin-top:1rem">Garmin Fitness Insights runs entirely in your browser on this site. It isn't affiliated with or endorsed by Garmin. Looking for money calculators? They're in the <a href="savings.html">Guides</a>, for example the <a href="pensions.html#calc">pension</a>, <a href="credit-cards.html#calc">balance transfer</a> and <a href="mortgages.html#calc">mortgage</a> calculators.</p>'''))
from seo import ext_links
EXT = 0
for fn, h in pages.items():
    h, c = ext_links(h); EXT += c
    open(fn, "w").write(h)
print("external links set to open in a new tab:", EXT)
from seo import write_sitemap
write_sitemap([f for f in pages if f!="404.html" and not (f=="paper-trading.html" and PT_PREVIEW)] + ["tools/garmin-insights/"], CHECKED_ISO)
print("built", len(pages), "pages; low-coupon example:", lowc["name"])
