# pages23.py – SEO quick wins (approved by Subhash 29 Oct 2026 10:44 UK): shorter titles/descriptions,
# Article + FAQPage JSON-LD, visible FAQ blocks and in-text related-guide links.
# Runs after every page is built (exec'd just before the search index), so it survives rebuilds
# and the 4-hourly paper-trades refresh. Edit titles/descriptions/FAQs HERE, not in the HTML.
import html as _h, json as _j, re as _r, datetime as _dt

SEO_META = {
 "index.html": ("Plain-English UK Money Guides & Calculators | MoneyBySharma", "Plain-English guides to UK savings, ISAs, pensions, gilts and mortgages, with simple calculators. Figures linked to official sources. Information, not advice."),
 "budget-2026.html": ("Budget 2026: Cash ISA Limit Stays £20,000, Savings Tax Rises", "The 28 Oct 2026 Budget: cash ISA limit stays £20,000, savings tax rises to 24%/44%/49% from April 2027, plus pensions, first-time buyers and drivers."),
 "savings.html": ("UK Savings Accounts & Cash ISAs Explained (2026/27)", "Easy access, fixed bonds, cash ISAs and regular savers explained, plus the Personal Savings Allowance and £120,000 FSCS protection. Plain English."),
 "gilts.html": ("What Is a Gilt? UK Gilts Explained + Tax Calculator", "What a UK gilt is, why low-coupon gilts can be tax-efficient (no CGT on gains) and a calculator comparing gilts with savings after tax."),
 "investments.html": ("Investing Basics UK: Stocks & Shares ISA, SIPP, Fees", "Stocks and shares ISAs, Lifetime ISAs, SIPP tax relief, index funds and why fees matter, explained in plain English for UK beginners."),
 "pensions.html": ("UK Pensions Explained: State, Workplace & SIPPs 2026/27", "State Pension 2026/27, auto-enrolment with a worked example, finding lost pensions, SIPPs and tax relief, plus a start-age calculator."),
 "annuities.html": ("Annuities UK: Income Estimate, Options & Providers", "Estimate annuity income from published rates, compare enhanced annuities and drawdown, see how 25% tax-free cash works and browse UK providers."),
 "mortgages.html": ("Fixed vs Tracker Mortgage + Repayment Calculator UK", "Fixed vs tracker mortgages, when to remortgage, and a repayment or interest-only calculator. Plain-English UK guide, not mortgage advice."),
 "pay-tax-payslip.html": ("UK Payslip Explained: Tax Codes, NI & Take-Home Pay", "How to read a UK payslip in 2026/27: gross vs net pay, tax codes like 1257L, Income Tax bands and National Insurance, in plain English."),
 "power-of-compounding.html": ("Compound Interest Explained Simply: The $24 Money Tree", "How compounding works, the rule of 72 doubling trick, and how $24 could have grown to $13.6 trillion at 7%. Illustrations, not forecasts."),
 "how-money-works.html": ("How Money Works in the UK, Explained in Pictures", "How banks create money, what the Bank of England and Bank Rate do, and what that means for your savings and mortgage. Ten illustrated steps."),
 "budgeting-emergency-fund.html": ("How to Budget UK: 50/30/20 Rule & Emergency Fund", "Build a budget from your take-home pay, try the 50/30/20 rule and work out how big an emergency fund to keep (3 to 6 months of essentials)."),
 "bank-accounts.html": ("UK Bank Accounts: Switching, FSCS & Your Protections", "Current account types, switching with CASS, £120,000 FSCS protection, overdraft rules, Section 75 and chargeback, and how switching bonuses work."),
 "credit-cards.html": ("How Credit Cards Work UK: APR, Section 75, Transfers", "Card types, representative APR, minimum payments, Section 75 and balance transfer fee maths, with an A to Z of UK card providers."),
 "credit-scores-debt-help.html": ("UK Credit Scores & Debt Help Explained", "How UK credit files work, how to check yours, fix mistakes and where to get free debt help from charities and services, including Breathing Space."),
 "energy.html": ("Ofgem Price Cap Oct–Dec 2026, Solar & Home Batteries", "The Ofgem price cap for Oct to Dec 2026, fixed vs variable deals, time-of-use tariffs, solar panels, export payments and a home battery calculator."),
 "energy-providers.html": ("UK Energy Suppliers: Deal Types & How to Switch", "The main UK household energy suppliers, fixed, variable and tracker deals explained, how switching works and accredited comparison sites."),
 "electric-cars.html": ("Electric Car Running Costs & Tax UK (2026 Guide)", "Home vs public charging costs, EV road tax from April 2025, the expensive car supplement, proposed pay-per-mile and company car tax explained."),
 "broadband-phones.html": ("Broadband & Mobile UK: Speeds, Switching, Social Tariffs", "Connection types, what speed you need, the 2027 digital landline switchover, Ofcom price-rise rules and social tariffs, explained simply."),
 "insurance-basics.html": ("Insurance Explained UK: Excess, Motor, Contents, Life", "What premium, excess and claim mean, the legal minimum for motor cover, and plain-English basics of contents, travel and life insurance."),
 "scams-fraud.html": ("How to Spot UK Money Scams and Who to Call", "Common UK money scams, warning signs, the numbers to call (159, 7726) and the reimbursement rules if you're tricked into sending a bank transfer."),
 "students.html": ("Student Finance 2026/27: Loans, Plan 5 Repayments", "Tuition and maintenance loans for 2026/27, Plan 5 and Plan 2 repayments, grants and bursaries, student overdrafts, railcards and discounts."),
 "deals.html": ("UK Loyalty Prices, Subscriptions & Cinema Deals", "Supermarket loyalty prices, cinema offers, streaming prices and high-street discounts, each with a checked date and a link to the official page."),
 "money-matters-cheat-sheet.html": ("UK Tax Year 2026/27 Key Figures: Cheat Sheet", "Income tax bands, NI, ISA and pension allowances and savings rules for 2026/27 on one page, each with its source and date. Also as a PDF."),
 "jargon.html": ("UK Money Jargon Buster: A to Z Finance Glossary", "A searchable A to Z of UK personal finance terms, from APR and AER to tax codes and gilts, each explained in one plain-English line."),
 "explained-simply-money-matters.html": ("Illustrated UK Money Guide (PDF) | MoneyBySharma", "A 15-page illustrated guide to UK money: payslips, tax, budgeting, savings, borrowing, student loans, pensions and scams."),
 "resources.html": ("UK Money PDFs & Cheat Sheets | MoneyBySharma", "Downloadable guides: the 2026/27 Money Matters cheat sheet, an illustrated UK money guide and a guide to the power of compounding."),
 "privacy.html": (None, "MoneyBySharma sets no cookies and uses no analytics. Feedback and the optional email sign-up go to third-party services only if you press Send or Subscribe."),
 "about.html": ("About MoneyBySharma | Subhash Sharma", "Why Subhash Sharma started MoneyBySharma, and how every figure is checked against official sources such as GOV.UK, with the date checked."),
 "tools.html": ("Tools: Garmin Insights & Paper Trading | MoneyBySharma", "Garmin Fitness Insights (your activity trends, processed in your browser) and a fake-money Paper Trading Experiment. Experiment only, not advice."),
 "paper-trading.html": (None, "Three fake-money trading books, their agents and a full trade log. An experiment only, not advice or a recommendation."),
 "cash-vs-inflation.html": ("Cash vs Inflation: Why Idle Savings Lose Value (UK)", "How inflation shrinks the buying power of cash, a 100-year UK chart, a worked example and the usual order to grow money long term. Information only."),
}

GUIDES = ["budget-2026.html","savings.html","gilts.html","investments.html","pensions.html","annuities.html","mortgages.html","pay-tax-payslip.html",
 "power-of-compounding.html","how-money-works.html","budgeting-emergency-fund.html","bank-accounts.html","credit-cards.html","credit-scores-debt-help.html",
 "energy.html","energy-providers.html","electric-cars.html","broadband-phones.html","insurance-basics.html","scams-fraud.html","students.html","deals.html",
 "money-matters-cheat-sheet.html","explained-simply-money-matters.html","cash-vs-inflation.html"]

_BASE = "https://moneybysharma.co.uk/"
_MON = {m:i for i,m in enumerate(["January","February","March","April","May","June","July","August","September","October","November","December"],1)}

def _set_meta(h, title, desc):
    if title:
        t = _h.escape(_h.unescape(title), quote=False); ta = _h.escape(_h.unescape(title))
        h = _r.sub(r"<title>.*?</title>", lambda m: f"<title>{t}</title>", h, count=1, flags=_r.S)
        h = _r.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*"', lambda m: m.group(1) + ta + '"', h)
    if desc:
        d = _h.escape(_h.unescape(desc))
        h = _r.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*"', lambda m: m.group(1) + d + '"', h)
    return h

def _checked(h):
    """Latest 'checked <d> <Month> <yyyy>' date stated on the page (ISO), or None."""
    best = None
    for d, mo, y in _r.findall(r"[Cc]hecked (?:on )?(\d{1,2}) (January|February|March|April|May|June|July|August|September|October|November|December) (20\d\d)", h):
        iso = _dt.date(int(y), _MON[mo], int(d)).isoformat()
        best = max(best or iso, iso)
    return best

def _ld(obj): return '<script type="application/ld+json">' + _j.dumps(obj, ensure_ascii=False).replace("</", "<\\/") + "</script>\n"

def _text(x): return _h.unescape(_r.sub(r"\s+", " ", _r.sub(r"<[^>]+>", "", x))).strip()

def _article(fn, h):
    h1 = _text(_r.search(r"<h1>(.*?)</h1>", h, _r.S).group(1))
    desc = _h.unescape(_r.search(r'<meta name="description" content="([^"]*)"', h).group(1))
    a = {"@context": "https://schema.org", "@type": "Article", "headline": h1[:110], "description": desc,
         "url": _BASE + fn, "mainEntityOfPage": _BASE + fn, "inLanguage": "en-GB",
         "image": _BASE + "assets/og-image.png",
         "author": {"@type": "Person", "name": "Subhash Sharma", "url": _BASE + "about.html"},
         "publisher": {"@type": "Organization", "name": "MoneyBySharma", "url": _BASE, "logo": {"@type": "ImageObject", "url": _BASE + "assets/og-square.png"}}}
    c = _checked(h)
    if c: a["dateModified"] = c
    return a

# ---- FAQs: every answer is shown on the page and uses only figures already on the site ----
FAQS = {
 "budget-2026.html": [
  ("Is the cash ISA limit changing after Budget 2026?", 'No. The planned cut to £12,000 a year for under-65s from April 2027 has been scrapped. The cash ISA limit stays at £20,000 for everyone aged 18 or over, and transfers from stocks and shares ISAs to cash ISAs are still allowed. This is due to be done by regulations laid in November 2026. See <a href="savings.html#types">Savings and cash ISAs</a>.'),
  ("How much tax will I pay on savings interest from April 2027?", 'Budget 2026 announced savings income tax rates of 24% (basic rate), 44% (higher rate) and 49% (additional rate) from 6 April 2027. They are in Finance Bill 2026-27, so they are not law yet. The Personal Savings Allowance (£1,000 / £500 / £0) and the £5,000 starting rate for savings don\'t change. See <a href="savings.html#tax">how savings interest is taxed</a>.'),
  ("Is interest in a cash ISA taxed?", 'No. Interest inside an ISA isn\'t taxed, so the higher savings rates don\'t apply to money held in one.'),
  ("Does the savings tax rise affect gilts?", 'Gilt coupons are savings income, so they would be taxed at the new rates. Gains on gilts stay free of Capital Gains Tax. The <a href="gilts.html#calc">gilt vs savings calculator</a> includes the 2027/28 rates.'),
  ("What did Budget 2026 change for pensions?", 'The full new State Pension is due to be £13,036.40 a year from April 2027, and a new Pension Tax Allowance from 6 April 2027 means people over State Pension age with total income up to £13,037 won\'t pay income tax. It isn\'t law yet. See <a href="pensions.html#state">Pensions</a>.'),
 ],
 "savings.html": [
  ("How much can I put in a cash ISA in 2026/27?", 'The overall ISA allowance for 2026/27 is £20,000, and you can put all of it into a cash ISA. At Budget 2026 (28 October 2026) the planned cut for under-65s from April 2027 was scrapped, so the cash ISA limit is due to stay at £20,000 for savers aged 18 or over. See <a href="budget-2026.html#savers">Budget 2026 for savers</a>.'),
  ("How much savings interest can I earn before paying tax?", 'The Personal Savings Allowance is £1,000 for basic-rate taxpayers, £500 for higher-rate and £0 for additional-rate taxpayers. Some people can also use the starting rate for savings of up to £5,000. Interest in an ISA is tax-free and doesn\'t use your allowance.'),
  ("How much of my savings is protected if a bank fails?", 'Since 1 December 2025 the FSCS protects eligible deposits up to £120,000 per person, per authorised firm. Brands that share one banking licence count as one firm. See <a href="#fscs">FSCS protection</a>.'),
  ("What is AER?", 'The Annual Equivalent Rate (AER) shows what a rate would be if interest were added once a year, so you can compare accounts fairly. For example, 4% a year paid monthly works out at an AER of about 4.07%.'),
  ("Are gilts an alternative to a savings account?", 'Some people compare them. Gains on gilts are free of Capital Gains Tax, while the coupon is taxed as savings income. See <a href="gilts.html">Gilts explained</a> and its gilt vs savings calculator.'),
 ],
 "gilts.html": [
  ("What is a gilt?", 'A gilt is a bond issued by the UK government through the Debt Management Office. A conventional gilt pays a fixed coupon twice a year on each £100 of nominal value and repays £100 at its maturity date.'),
  ("Do I pay tax on gilts?", 'Capital gains on gilts are exempt from Capital Gains Tax for individuals. The coupon is taxable as savings income, so it can use your Personal Savings Allowance and starting rate. Budget 2026 announced savings income tax rates of 24% / 44% / 49% from 6 April 2027, which aren\'t law yet. See <a href="budget-2026.html#savers">Budget 2026 for savers</a>.'),
  ("Why can low-coupon gilts be tax-efficient?", 'A low-coupon gilt trading below £100 delivers most of its return as a tax-free gain at maturity rather than as taxable interest. Inside an ISA or SIPP the tax difference doesn\'t apply.'),
  ("Can I lose money on a gilt?", 'Gilts trade on the market, so their price moves, mainly with interest rates. If you sell before maturity you could get back less than you paid. If you hold to maturity you receive £100 per £100 nominal.'),
  ("How does a gilt compare with a savings account?", 'Use the <a href="#calc">gilt vs savings calculator</a> to see the after-tax yield and the savings rate you\'d need to match it. For savings accounts and cash ISAs, see <a href="savings.html">Savings explained</a>.'),
 ],
 "pensions.html": [
  ("How much is the full new State Pension?", 'For 2026/27 it is £241.30 a week (about £12,548 a year). From April 2027 it rises by 3.9% under the triple lock to £13,036.40 a year, as announced at <a href="budget-2026.html#pensions">Budget 2026</a>.'),
  ("How many years of National Insurance do I need for the State Pension?", 'You usually need 35 qualifying years for the full new State Pension and at least 10 qualifying years to get anything. With 10 to 34 years you get a proportion.'),
  ("What is the minimum workplace pension contribution?", 'The legal minimum is 8% of qualifying earnings, with at least 3% from your employer. Qualifying earnings for 2026/27 are those between £6,240 and £50,270 a year.'),
  ("When can I take money from a private pension?", 'The access age for personal pensions such as SIPPs is 55, rising to 57 on 6 April 2028. See <a href="investments.html#sipp">SIPPs and tax relief</a>.'),
  ("How do I find a lost pension?", 'Use the GOV.UK Pension Tracing Service to find a scheme\'s contact details. You can also call 0800 731 0175 (Monday to Friday, 10am to 3pm). See <a href="#tracing">finding lost pensions</a>.'),
 ],
}

RELATED = {
 "budget-2026.html": [("savings.html","Savings and cash ISAs"),("gilts.html","Gilts explained"),("pensions.html","Pensions explained"),("investments.html","Investing basics"),("money-matters-cheat-sheet.html","2026/27 key figures")],
 "savings.html": [("budget-2026.html","Budget 2026"),("gilts.html","Gilts explained"),("bank-accounts.html","Bank accounts and FSCS"),("budgeting-emergency-fund.html","Emergency funds")],
 "gilts.html": [("savings.html","Savings and cash ISAs"),("budget-2026.html","Budget 2026"),("investments.html","Investing basics")],
 "pensions.html": [("budget-2026.html","Budget 2026"),("investments.html","SIPPs and ISAs"),("annuities.html","Annuities")],
 "investments.html": [("savings.html","Savings and cash ISAs"),("pensions.html","Pensions explained"),("budget-2026.html","Budget 2026"),("power-of-compounding.html","The power of compounding")],
}

def _faq_html(items):
    qa = "".join(f'<h3>{_h.escape(q, quote=False)}</h3><p>{a}</p>' for q, a in items)
    return f'<div class="wrap"><section class="faq card" id="faq" aria-labelledby="faq-h" style="margin:1.5rem 0"><h2 id="faq-h">Common questions</h2>{qa}<p class="hint">Information, not financial advice.</p></section></div>'

def _faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": _text(a)}} for q, a in items]}

def _related_html(fn):
    links = " · ".join(f'<a href="{u}">{t}</a>' for u, t in RELATED[fn])
    return f'<div class="wrap"><p class="related" style="margin:1rem 0 1.5rem"><strong>Related guides:</strong> {links}</p></div>'

for _fn, _h0 in list(pages.items()):
    _x = _h0
    if _fn in SEO_META: _x = _set_meta(_x, *SEO_META[_fn])
    if _fn == "savings.html":
        _x = _x.replace("<h1>Savings, explained</h1>", "<h1>Savings and Cash ISAs, explained</h1>", 1)
    if _fn == "budget-2026.html":
        _x = _x.replace("<p>What the Budget on 28 October 2026 changes for workers, savers, investors, first-time buyers, pensioners, households and drivers, and what stays the same. Information, not financial advice.</p>",
          "<p>The cash ISA limit stays £20,000 for everyone aged 18 or over, but tax on savings interest outside an ISA rises to 24% / 44% / 49% from 6 April 2027 (not law yet). Here's what else the Budget on 28 October 2026 changes for workers, savers, investors, first-time buyers, pensioners, households and drivers, and what stays the same. Information, not financial advice.</p>", 1)
    _extra, _ldx = "", ""
    if _fn in FAQS:
        _extra += _faq_html(FAQS[_fn]); _ldx += _ld(_faq_ld(FAQS[_fn]))
    if _fn in RELATED: _extra += _related_html(_fn)
    if _extra: _x = _x.replace("</main>", _extra + "</main>", 1)
    if _fn in GUIDES: _ldx = _ld(_article(_fn, _x)) + _ldx
    if _ldx: _x = _x.replace("</head>", _ldx + "</head>", 1)
    pages[_fn] = _x
print("seo pass: meta", sum(f in pages for f in SEO_META), "| article schema", sum(f in pages for f in GUIDES), "| faq", len(FAQS))
