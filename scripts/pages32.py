# Standalone calculator pages at /calculators/<name>.html plus /calculators/index.html.
# Each page reuses the guide's calculator markup and the same figures/data (annuity rates
# from data/annuity-rates.json via pages18; gilt defaults from the same low-coupon example;
# energy/EV price-cap figures from the energy guide). A normal build.py run — including the
# Monday annuity refresh — regenerates these pages. Not added to the main nav.
import re as _c32_re

def _c32_fix(h, depth=1):
    pre = "../" * depth
    return _c32_re.sub(
        r'(\s(?:href|src|action)=")(?!https?:|mailto:|#|/|data:|\.\./)([^"]*)"',
        lambda m: f'{m.group(1)}{pre}{m.group(2)}"',
        h,
    )

def _c32_extract(fn, pat):
    ms = list(_c32_re.finditer(pat, pages[fn], _c32_re.S))
    assert len(ms) == 1, f"{fn}: expected 1 calculator block, got {len(ms)}"
    return ms[0].group(0)

def _c32_link(guide, block, href):
    """Add a preview/standalone link on the guide, after the embedded calculator (which stays)."""
    if href in pages[guide]:
        return
    assert pages[guide].count(block) == 1, f"{guide}: calculator block not found uniquely"
    pages[guide] = pages[guide].replace(
        block,
        block + f'\n<p class="hint"><a href="{href}">Open this calculator on its own page</a></p>',
        1,
    )

def _c32_page(fn, title, desc, h1, lead, intro, calc, scripts, related, articles=""):
    body = ph(
        f'<a href="calculators/index.html">Calculators</a> › {h1}',
        h1,
        lead,
    ) + W(
        intro
        + calc
        + articles
        + '''
<p class="hint">Information only, not financial advice. The figures are an illustration. This is not a quote, a forecast or a recommendation.</p>
<p class="related" style="margin:1.5rem 0 2rem"><strong>Related:</strong> '''
        + related
        + "</p>\n"
    )
    pages[fn] = _c32_fix(page(fn, title, desc, body, scripts=scripts))

# Latest CPI already loaded for how-money-works (pages3.py); use the same figures, invent nothing.
_c32_cpi = CPI["latestMonth"]
_c32_cpi_txt = f"{_c32_cpi['rate']}% for {_c32_cpi['period'].title()}"

# Annuity quote/checked dates already formatted by pages18.
_C32 = [
    {
        "fn": "calculators/compound-interest.html",
        "guide": "savings.html",
        "pat": r'<section class="calc" id="grow-calc".*?</section>',
        "prep": lambda h: h.replace('id="grow-calc"', 'id="calc"', 1),
        "scripts": ("calc-ui6.js",),
        "title": "Compound Interest Calculator UK – MoneyBySharma",
        "desc": "A UK compound interest calculator: compare simple and compound interest, see the AER, and estimate how long money takes to double. Plain English, illustration only, not financial advice.",
        "h1": "Compound interest calculator",
        "lead": "See how simple and compound interest compare, what the AER is, and how long money takes to double.",
        "intro": """
<p>Simple interest is paid only on the amount you first put in. Compound interest is paid on that amount <em>and</em> on the interest already added, so growth can build on itself. Savings accounts normally pay compound interest.</p>
<p>This is the same calculator as on our <a href="savings.html#grow">Savings guide: how interest grows</a>, where you'll also find a worked example and a fuller explanation of the Rule of 72.</p>
""",
        "related": '<a href="savings.html#grow">How interest grows</a> · <a href="savings.html">Savings and cash ISAs</a> · <a href="power-of-compounding.html">The power of compounding</a>',
        "index": ("Compound interest", "Compare simple and compound interest, see the AER, and estimate how long money takes to double."),
    },
    {
        "fn": "calculators/mortgage-repayment.html",
        "guide": "mortgages.html",
        "pat": r'<section class="calc" id="calc".*?</section>',
        "scripts": ("calc.js", "calc-ui.js"),
        "title": "Mortgage Repayment Calculator UK – MoneyBySharma",
        "desc": "A UK mortgage repayment calculator: estimate the monthly payment, total interest and time to clear a repayment or interest-only loan, including optional overpayments. Illustration only, not advice.",
        "h1": "Mortgage repayment calculator",
        "lead": "Estimate the monthly payment, total interest and how long a loan takes to clear.",
        "intro": """
<p>This illustration uses a fixed interest rate for the whole term. Real mortgage deals end, and rates change, so your actual payments can be different.</p>
<p>This is the same calculator as on our <a href="mortgages.html#calc">Mortgages guide</a>, which also explains fixed and tracker deals and remortgage timing.</p>
""",
        "related": '<a href="mortgages.html#calc">Mortgage repayment calculator on the guide</a> · <a href="mortgages.html">Mortgages</a>',
        "index": ("Mortgage repayment", "Estimate the monthly payment, total interest and time to clear a repayment or interest-only mortgage."),
    },
    {
        "fn": "calculators/take-home-pay.html",
        "guide": "pay-tax-payslip.html",
        "pat": r'<section class="calc" id="takehome".*?</section>',
        "prep": lambda h: h.replace('id="takehome"', 'id="calc"', 1),
        "scripts": ("calc-ui7.js",),
        "title": "Take-Home Pay Calculator UK – MoneyBySharma",
        "desc": "A UK take-home pay calculator for 2026/27: Income Tax, National Insurance, pension and student loan, using the same England, Wales and Northern Ireland figures as our payslip guide. Illustration only, not advice.",
        "h1": "Take-home pay calculator",
        "lead": "See how Income Tax, National Insurance, pension contributions and a student loan change monthly take-home pay.",
        "intro": """
<p>This uses the same 2026/27 tax and National Insurance figures as our payslip guide, for England, Wales or Northern Ireland, with tax code 1257L and NI category A. It does not cover Scottish rates, salary sacrifice or part-years.</p>
<p>This is the same calculator as on our <a href="pay-tax-payslip.html#takehome">Pay, tax and your payslip</a> guide, which walks through a payslip line by line.</p>
""",
        "related": '<a href="pay-tax-payslip.html#takehome">Take-home pay on the guide</a> · <a href="pay-tax-payslip.html">Pay, tax and your payslip</a> · <a href="budgeting-emergency-fund.html">Budgeting and emergency funds</a>',
        "index": ("Take-home pay", "Estimate monthly take-home pay after Income Tax, National Insurance, pension and student loan (2026/27)."),
    },
    {
        "fn": "calculators/platform-fees.html",
        "guide": "investments.html",
        "pat": r'<section class="calc" id="calc".*?</section>',
        "scripts": ("calc.js", "calc-ui.js"),
        "title": "Investment Platform Fees Calculator UK – MoneyBySharma",
        "desc": "See how a percentage platform fee compares with a flat annual fee over time, using the same illustration as our investing guide. Not a forecast or advice.",
        "h1": "Platform fees calculator",
        "lead": "Compare a percentage platform fee with a flat annual fee, and with no platform fee at all.",
        "intro": """
<p>Fees look small as a percentage, but they are taken every year, so they can quietly reduce a pot. This illustration assumes a single lump sum, steady growth and no further contributions or withdrawals. Real returns vary and can be negative.</p>
<p>This is the same calculator as on our <a href="investments.html#calc">Investing basics</a> guide, in the platform fees section.</p>
""",
        "related": '<a href="investments.html#fees">Platform fees explained</a> · <a href="investments.html">Investing basics</a>',
        "index": ("Platform fees", "Compare a percentage platform fee with a flat annual fee, and with no platform fee."),
    },
    {
        "fn": "calculators/pension-start-age.html",
        "guide": "pensions.html",
        "pat": r'<section class="calc" id="calc".*?</section>',
        "scripts": ("calc.js", "calc-ui2.js"),
        "title": "Pension Start Age Calculator UK – MoneyBySharma",
        "desc": "See how the age you start paying into a pension changes the pot at 67, in today's money, using the same illustration as our pensions guide. Not a forecast or advice.",
        "h1": "Pension start age calculator",
        "lead": "See how the age you start contributing changes the pot at 67, in today's money.",
        "intro": """
<p>Starting earlier gives contributions more time to grow, but this is only an illustration: growth, charges and inflation are assumed to stay steady, and tax on withdrawal is ignored. Your capital is at risk.</p>
<p>This is the same calculator as on our <a href="pensions.html#calc">Pensions guide</a>.</p>
""",
        "related": '<a href="pensions.html#calc">Start age calculator on the guide</a> · <a href="pensions.html">Pensions</a> · <a href="annuities.html">Annuities</a>',
        "index": ("Pension start age", "See how the age you start contributing changes the pot at 67, in today's money."),
    },
    {
        "fn": "calculators/gilt-vs-savings.html",
        "guide": "gilts.html",
        "pat": r'<section class="calc" id="calc".*?</section>',
        "scripts": ("calc.js", "calc-ui.js"),
        "title": "Gilt vs Savings Calculator UK – MoneyBySharma",
        "desc": "Compare a UK gilt held to maturity with a savings account after tax, using the same DMO gilt list and tax-band options as our gilts guide. Illustration only, not advice.",
        "h1": "Gilt vs savings calculator",
        "lead": "Compare a gilt held to maturity with a savings account after tax, for your tax band.",
        "intro": f"""
<p>The default coupon and maturity are the same low-coupon example as on our gilts guide, from DMO data (close of business {d(GI['closeOfBusiness'])}). Prices are not fetched automatically: enter the clean price from your broker. This is not a recommendation to buy.</p>
<p>This is the same calculator as on our <a href="gilts.html#calc">Gilts guide</a>, which also explains why low-coupon gilts can be tax-efficient.</p>
""",
        "related": '<a href="gilts.html#calc">Gilt vs savings on the guide</a> · <a href="gilts.html">Gilts</a> · <a href="savings.html">Savings and cash ISAs</a>',
        "index": ("Gilt vs savings", "Compare a gilt held to maturity with a savings account after tax, for your tax band."),
    },
    {
        "fn": "calculators/balance-transfer.html",
        "guide": "credit-cards.html",
        "pat": r'<h3 id="calc">.*?</form>',
        "prep": lambda h: '<section class="calc" aria-labelledby="calc">' + h + "</section>",
        "scripts": ("calc.js", "calc-ui4.js"),
        "title": "Balance Transfer Calculator UK – MoneyBySharma",
        "desc": "Compare a balance-transfer fee with the interest you'd pay on your current card over the same period. The filled-in values are examples, not real offers. Illustration only, not advice.",
        "h1": "Balance transfer calculator",
        "lead": "Compare the one-off transfer fee with the interest you'd pay on your current card over the same period.",
        "intro": """
<p>The values filled in are examples only, not real offers. Change them to match your own balance, APR, fee and 0% period. Being accepted, and the terms you're offered, depend on the lender's assessment of you.</p>
<p>This is the same calculator as on our <a href="credit-cards.html#calc">Credit cards guide</a>.</p>
""",
        "related": '<a href="credit-cards.html#calc">Balance transfer calculator on the guide</a> · <a href="credit-cards.html">Credit cards</a>',
        "index": ("Balance transfer", "Compare a transfer fee with the interest you'd pay on your current card over the same period."),
    },
    {
        "fn": "calculators/annuity-income.html",
        "guide": "annuities.html",
        "pat": r'<section class="calc" id="calc".*?</section>',
        "scripts": ("annuity-calc.js",),
        "title": "Annuity Income Calculator UK – MoneyBySharma",
        "desc": "Estimate UK annuity income from the same published market rates as our annuities guide (Hargreaves Lansdown table). This is an estimate, not a quote, and not financial advice.",
        "h1": "Annuity income calculator",
        "lead": "Estimate yearly income from published market rates, for a given pot, age and annuity type.",
        "intro": f"""
<p>This uses the same published reference rates as our annuities guide, from the Hargreaves Lansdown annuity rate table, quotes dated {AN_QD}, checked {AN_CHK}. It is an estimate, not a personal quote. Your actual quote will differ.</p>
<p>This is the same calculator as on our <a href="annuities.html#calc">Annuities guide</a>, which also covers enhanced annuities, tax-free cash, drawdown and UK providers.</p>
""",
        "related": '<a href="annuities.html#calc">Annuity income estimate on the guide</a> · <a href="annuities.html">Annuities</a> · <a href="pensions.html">Pensions</a>',
        "index": ("Annuity income", "Estimate yearly income from published market rates, for a given pot, age and annuity type."),
    },
    {
        "fn": "calculators/ev-charging.html",
        "guide": "electric-cars.html",
        "pat": r'<section class="calc" id="calc".*?</section>',
        "scripts": ("calc.js", "calc-ui2.js"),
        "title": "EV Charging Cost Calculator UK – MoneyBySharma",
        "desc": "Estimate home and public electric-car charging costs, using the same example rates and price-cap reference figure as our electric cars guide. Illustration only, not a tariff or advice.",
        "h1": "EV charging cost calculator",
        "lead": "Estimate the cost of charging an electric car at home and in public, and the yearly total.",
        "intro": """
<p>The default home and public rates are examples, not real tariffs. The price-cap reference figure in the calculator is the same one used on our electric cars guide. Replace the rates with your own tariff.</p>
<p>This is the same calculator as on our <a href="electric-cars.html#calc">Electric cars guide</a>.</p>
""",
        "related": '<a href="electric-cars.html#calc">EV charging calculator on the guide</a> · <a href="electric-cars.html">Electric cars</a> · <a href="energy.html">Energy</a>',
        "articles": '''<aside class="card" style="margin:1.5rem 0" aria-labelledby="ev-arts"><h2 id="ev-arts" style="margin-top:0">EV charging explainers</h2><p>Four plain-English articles that go with this calculator:</p><ul>
<li><a href="../ev-charging-cost-per-mile-explained.html">EV charging cost per mile, explained</a></li>
<li><a href="../ev-home-vs-public-charging-cost.html">Home vs public charging: cost per mile</a></li>
<li><a href="../ev-tariffs-off-peak-charging.html">EV tariffs and off-peak charging</a></li>
<li><a href="../ev-charging-calculator-limits.html">What the charging calculator leaves out</a></li></ul></aside>''',
        "index": ("EV charging cost", "Estimate home and public charging costs, and the yearly total, from your mileage and rates."),
    },
    {
        "fn": "calculators/home-battery.html",
        "guide": "energy.html",
        "pat": r'<section class="calc" id="calc".*?</section>',
        "scripts": ("calc.js", "calc-ui2.js"),
        "title": "Home Battery Payback Calculator UK – MoneyBySharma",
        "desc": "Estimate first-year saving, payback and net gain for a home battery, using the same price-cap peak rate and example figures as our energy guide. Illustration only, not advice.",
        "h1": "Home battery payback calculator",
        "lead": "Estimate first-year saving, payback and net gain for a home battery on a cheap-rate tariff.",
        "intro": """
<p>The default peak rate is the same price-cap average unit rate used on our energy guide. The cheap rate, battery cost, efficiency and lifespan are example figures only. Replace them with your own quote and tariff.</p>
<p>This is the same calculator as on our <a href="energy.html#calc">Energy guide</a>.</p>
""",
        "related": '<a href="energy.html#calc">Home battery calculator on the guide</a> · <a href="energy.html">Energy bills, solar and batteries</a>',
        "articles": '''<aside class="card" style="margin:1.5rem 0" aria-labelledby="bat-arts"><h2 id="bat-arts" style="margin-top:0">Home battery explainers</h2><p>Four plain-English articles that go with this calculator:</p><ul>
<li><a href="../home-battery-payback-explained.html">How home battery payback is worked out</a></li>
<li><a href="../home-battery-time-of-use-tariffs.html">Time-of-use tariffs and home batteries</a></li>
<li><a href="../home-battery-smart-export-guarantee.html">The Smart Export Guarantee and home batteries</a></li>
<li><a href="../home-battery-cost-vat-quotes.html">Home battery costs, VAT and quotes</a></li></ul></aside>''',
        "index": ("Home battery payback", "Estimate first-year saving, payback and net gain for a home battery on a cheap-rate tariff."),
    },
    {
        "fn": "calculators/inflation-and-cash.html",
        "guide": "how-money-works.html",
        "pat": r'<form id="rv-form".*?</form>',
        "prep": lambda h: '<section class="calc" id="calc" aria-labelledby="rv-h"><h3 id="rv-h" style="margin-top:0">What inflation does to cash</h3>' + h + "</section>",
        "scripts": ("calc.js", "calc-ui3.js"),
        "title": "Inflation and Cash Calculator UK – MoneyBySharma",
        "desc": "See how inflation and interest change the real value of cash over time. The same illustration as in How money works. Not a forecast or advice.",
        "h1": "Inflation and cash calculator",
        "lead": "See how inflation and interest change what a sum of cash can buy over time.",
        "intro": f"""
<p>If prices rise faster than the interest on your savings, your money buys less each year, even if the number in the account goes up. The latest UK CPI figure used on this site is <strong>{_c32_cpi_txt}</strong>. The default rate in the calculator is an example, which you can change.</p>
<p>This is the same calculator as in <a href="how-money-works.html#s8">How money works: what inflation does to cash</a>.</p>
""",
        "related": '<a href="how-money-works.html#s8">What inflation does to cash</a> · <a href="how-money-works.html">How money works</a> · <a href="cash-vs-inflation.html">Cash vs inflation</a>',
        "index": ("Inflation and cash", "See how inflation and interest change the real value of a sum of cash over time."),
    },
    {
        "fn": "calculators/broadband-speed.html",
        "guide": "broadband-phones.html",
        "pat": r'<h3 id="calc">.*?</form>',
        "prep": lambda h: '<section class="calc" aria-labelledby="calc">' + h + "</section>",
        "scripts": ("calc.js", "calc-ui5.js"),
        "title": "Broadband Speed Calculator UK – MoneyBySharma",
        "desc": "A rough guide to the broadband speed a household might need, from how many people stream, call or game at once. The same planning figures as our broadband guide. Illustration only, not a recommendation.",
        "h1": "Broadband speed calculator",
        "lead": "A rough guide to the speed a household might need, from what happens at the same time.",
        "intro": """
<p>This uses the same planning figures as our broadband guide (not official numbers): HD stream 5 Mbps, 4K stream 25 Mbps, video call 3 Mbps, online gaming 3 Mbps, plus 1 Mbps per person, then 50% headroom. Real needs vary.</p>
<p>This is the same tool as on our <a href="broadband-phones.html#calc">Broadband and phones guide</a>. The postcode checker stays on that guide.</p>
""",
        "related": '<a href="broadband-phones.html#calc">What speed do I need? on the guide</a> · <a href="broadband-phones.html">Broadband and phones</a>',
        "index": ("Broadband speed", "A rough guide to the speed a household might need, from what happens at the same time."),
    },
]

# Fix the gilt intro: I used a quoted f-string with {d(...)} incorrectly inside a normal string
# that was itself in an f-string in the list. Rebuild that one item's intro after the list? 
# Actually the gilt intro is an f-string: f"""... {d(GI["closeOfBusiness"])} ..."""
# That's evaluated now and is correct.

_C32_INDEX_ITEMS = []
for _c in _C32:
    _block = _c32_extract(_c["guide"], _c["pat"])
    _calc = _c.get("prep", lambda h: h)(_block)
    _c32_page(_c["fn"], _c["title"], _c["desc"], _c["h1"], _c["lead"], _c["intro"], _calc, _c["scripts"], _c["related"], _c.get("articles", ""))
    _c32_link(_c["guide"], _block, _c["fn"])
    _C32_INDEX_ITEMS.append((_c["fn"],) + _c["index"])

_c32_lis = "\n".join(
    f'<li><a href="/calculators/{fn.rsplit("/",1)[-1]}"><strong>{name}</strong></a> — {blurb}</li>'
    for fn, name, blurb in _C32_INDEX_ITEMS
)
_C32_INDEX = "calculators/index.html"
pages[_C32_INDEX] = _c32_fix(page(
    _C32_INDEX,
    "UK Money Calculators – MoneyBySharma",
    "Simple UK money calculators for savings, mortgages, take-home pay, pensions, gilts, energy and more. Illustrations in plain English, not financial advice.",
    ph(
        "Calculators",
        "Calculators",
        "Simple illustrations you can try with your own figures. Each calculator also sits on its guide, with a fuller explanation.",
    )
    + W(f'''
<ul class="calc-index">
{_c32_lis}
</ul>
<p class="hint">Information only, not financial advice. The figures are illustrations, not quotes, forecasts or recommendations. Open a calculator, then read the linked guide for the assumptions and sources.</p>
'''),
))
print("calculators:", ", ".join(fn for fn, *_ in _C32_INDEX_ITEMS), "+ index")
