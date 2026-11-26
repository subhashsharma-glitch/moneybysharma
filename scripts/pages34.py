# pages34.py – four supporting articles around the gilt-vs-savings calculator.
# Exec'd from build.py before the search index so they join search and the sitemap.
# Not in GUIDES, so they do not get the weekly sign-up form. Not in the main nav.
# Every tax fact below was checked against GOV.UK / HMRC / legislation.gov.uk (and the DMO, see _DMO_NOTE) on 26 November 2026.
# Worked examples use stated hypothetical assumptions only; no rates or prices are quoted for real products.
_G_CHK = "checked 26 November 2026"
_G_CALC = "calculators/gilt-vs-savings.html"
_G_PAGES = {
    "what": "what-is-a-gilt.html",
    "tax": "gilts-cgt-and-coupon-tax.html",
    "vs": "gilts-vs-fixed-rate-bonds-and-savings.html",
    "buy": "how-to-buy-gilts.html",
}
_G_TITLES = {
    "what": "What is a gilt? How low-coupon gilts work",
    "tax": "Gilts and tax: why the gain is free of CGT but the coupon is taxed",
    "vs": "Gilts vs fixed-rate bonds and easy-access savings for higher-rate taxpayers",
    "buy": "How to buy gilts through an ISA, a SIPP or a general account",
}
def _gs(u, t): return f'<a href="{u}" target="_blank" rel="noopener">{t}</a>'
_GS = {
    "cgt":   ("https://www.gov.uk/capital-gains-tax/what-you-pay-it-on", "GOV.UK – Capital Gains Tax: what you pay it on (“UK government gilts and Premium Bonds”)"),
    "s115":  ("https://www.legislation.gov.uk/ukpga/1992/12/section/115", "legislation.gov.uk – Taxation of Chargeable Gains Act 1992, section 115"),
    "cg534": ("https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg53400", "HMRC Capital Gains Manual CG53400 – gilt-edged securities"),
    "saim22":("https://www.gov.uk/hmrc-internal-manuals/savings-and-investment-manual/saim2230", "HMRC Savings and Investment Manual SAIM2230 – profits on gilts"),
    "saim30":("https://www.gov.uk/hmrc-internal-manuals/savings-and-investment-manual/saim3040", "HMRC Savings and Investment Manual SAIM3040 – gilts and the deeply discounted securities rules"),
    "s369":  ("https://www.legislation.gov.uk/ukpga/2005/5/section/369", "legislation.gov.uk – Income Tax (Trading and Other Income) Act 2005, section 369 (income tax is charged on interest)"),
    "psa":   ("https://www.gov.uk/apply-tax-free-interest-on-savings/how-much-is-tax-free", "GOV.UK – Tax on savings interest: how much is tax free"),
    "psa18": ("https://www.gov.uk/government/publications/personal-savings-allowance-factsheet/personal-savings-allowance", "GOV.UK – Personal Savings Allowance factsheet (archived 2018; lists income from government bonds as savings income)"),
    "ais":   ("https://www.gov.uk/government/publications/accrued-income-scheme-hs343-self-assessment-helpsheet/hs343-accrued-income-scheme-2025", "GOV.UK/HMRC – HS343 Accrued Income Scheme (2025)"),
    "exdiv": ("https://www.gov.uk/hmrc-internal-manuals/savings-and-investment-manual/saim4020", "HMRC Savings and Investment Manual SAIM4020 – cum div and ex div (gilts: 7 business days)"),
    "rates": ("https://www.gov.uk/income-tax-rates", "GOV.UK – Income Tax rates and bands"),
    "ootlar":("https://www.gov.uk/government/publications/budget-2026-overview-of-tax-legislation-and-rates-ootlar/budget-2026-overview-of-tax-legislation-and-rates-ootlar", "GOV.UK/HM Treasury – Budget 2026: overview of tax legislation and rates (savings rates for 2027 to 2028)"),
    "isa":   ("https://www.gov.uk/individual-savings-accounts", "GOV.UK – Individual Savings Accounts"),
    "isahow":("https://www.gov.uk/individual-savings-accounts/how-isas-work", "GOV.UK – How ISAs work (stocks and shares ISAs can include government bonds)"),
    "sipp":  ("https://www.gov.uk/personal-pensions-your-rights", "GOV.UK – Personal pensions (SIPPs let you choose the investments)"),
    "aa":    ("https://www.gov.uk/tax-on-your-private-pension/annual-allowance", "GOV.UK – Pension annual allowance"),
    "relief":("https://www.gov.uk/tax-on-your-private-pension/pension-tax-relief", "GOV.UK – Tax relief on pension contributions"),
    "ptm":   ("https://www.gov.uk/hmrc-internal-manuals/pensions-tax-manual/ptm024400", "HMRC Pensions Tax Manual PTM024400 – tax exemptions for pension investments"),
    "nmpa":  ("https://www.gov.uk/government/publications/increasing-normal-minimum-pension-age/increasing-normal-minimum-pension-age", "GOV.UK/HMRC – Increasing Normal Minimum Pension Age (55 to 57 in April 2028)"),
    "taxpen":("https://www.gov.uk/tax-on-pension", "GOV.UK – Tax when you get a pension"),
    "fscs":  ("https://www.fscs.org.uk/what-we-cover/banks-building-societies-credit-unions/deposit-limit/", "FSCS – Deposit protection limit"),
    "dmo":   ("https://www.dmo.gov.uk/responsibilities/gilt-market/about-gilts/", "UK Debt Management Office – About gilts (ex-dividend dates and accrued interest)"),
    "dmotax":("https://www.dmo.gov.uk/responsibilities/gilt-market/buying-selling/taxation/", "UK Debt Management Office – Taxation of gilts (page dated November 2016)"),
    "dmofaq":("https://www.dmo.gov.uk/help/faqs/", "UK Debt Management Office – FAQs: how do I buy gilts?"),
    "dmodata":("https://www.dmo.gov.uk/data/gilt-market/gilts-in-issue/", "UK Debt Management Office – Gilts in issue"),
}
def _gl(k, label=None): return _gs(_GS[k][0], label or _GS[k][1])
def _gsrc(keys): return "<ul>" + "".join(f"<li>{_gl(k)} ({_G_CHK})</li>" for k in keys) + "</ul>"
def _gp(k): return _G_PAGES[k]
_G_DISC = '<p class="hint"><strong>This is information, not financial advice.</strong> It does not take your circumstances into account and is not a personal recommendation to buy, sell or hold any gilt or other product. Gilts can fall in price, and tax rules can change. If in doubt, speak to an FCA-authorised adviser.</p>'
_DMO_NOTE = '<p class="hint">The DMO’s website blocked our automated check on 26 November 2026, so DMO statements on this page were read from its published pages as shown in search results, not opened in full. Where HMRC or legislation covers the same point, that is the source relied on for the tax rule.</p>'
def _g_cta(label="Open the gilt vs savings calculator"):
    return f'<div class="card" style="margin:1.2rem 0"><p style="margin:0 0 .6rem"><strong>Try it with your own numbers.</strong> Our calculator compares a gilt held to maturity with a savings account after tax, for your tax band.</p><p class="cs-actions" style="margin:0"><a class="btn" href="{_G_CALC}">{label}</a></p></div>'
def _g_next(me):
    items = "".join(f'<li><a href="{_gp(k)}">{_G_TITLES[k]}</a></li>' for k in ("what", "tax", "vs", "buy") if k != me)
    return f'<h2 id="next">Keep reading</h2><ul>{items}<li><a href="gilts.html">Gilts, explained (the main guide)</a></li><li><a href="{_G_CALC}">Gilt vs savings calculator</a></li></ul>'
def _g_page(key, title, desc, crumb, h1, lead, body, sources):
    fn = _gp(key)
    pages[fn] = page(fn, title, desc,
        ph(f'<a href="gilts.html">Gilts</a> › {crumb}', h1, lead) + W(
            _g_cta() + body + _g_cta("Compare a gilt with savings") + _G_DISC + _g_next(key) +
            f'<h2 id="sources">Sources</h2>{_gsrc(sources)}'))

# ---------- 1. What a gilt is ----------
_g_page("what",
 "What Is a Gilt? How Low-Coupon Gilts Work (UK) – MoneyBySharma",
 "Plain-English guide to UK gilts: nominal value, coupon, maturity and price, and why a low-coupon gilt bought below £100 earns most of its return as a gain.",
 "What is a gilt?", "What is a gilt, and how do low-coupon gilts work?",
 "A gilt is a UK government bond. Here is what the terms mean and why a gilt with a small coupon can behave very differently from a savings account. Information, not financial advice.",
 f'''
<h2 id="terms">The words you will meet</h2>
<table><thead><tr><th>Term</th><th>What it means</th></tr></thead><tbody>
<tr><td>Gilt</td><td>A bond issued by the UK government through the Debt Management Office (DMO). The DMO publishes the list of gilts in issue ({_gl("dmodata", "DMO – Gilts in issue")}).</td></tr>
<tr><td>Nominal value</td><td>The face value the coupon and the final repayment are worked out on. Gilts are quoted per £100 nominal.</td></tr>
<tr><td>Coupon</td><td>The fixed yearly interest, set when the gilt is issued and paid twice a year, as a percentage of nominal value.</td></tr>
<tr><td>Maturity date</td><td>The date the government repays £100 per £100 nominal.</td></tr>
<tr><td>Clean price</td><td>The quoted market price per £100 nominal, before accrued interest.</td></tr>
<tr><td>Accrued interest</td><td>The part of the next coupon that has built up since the last coupon date. A buyer normally pays it on top of the clean price ({_gl("dmo", "DMO – About gilts")}, {_G_CHK}).</td></tr>
</tbody></table>
<p class="hint">This article is about conventional gilts. Index-linked gilts and gilt strips follow different rules and are not covered here.</p>

<h2 id="how">How a gilt pays you</h2>
<p>A conventional gilt pays its coupon every six months and repays £100 per £100 nominal on its maturity date. Gilts are traded on the market, so their price moves, mainly with interest rates. If you sell before maturity you could get back less than you paid; if you hold to maturity you receive £100 per £100 nominal, as set out in our {_gs("gilts.html", "gilts guide")}.</p>

<h2 id="lowcoupon">What “low-coupon” means</h2>
<p>A low-coupon gilt pays a small yearly coupon. Because market interest rates are usually higher than that coupon, such a gilt tends to trade below £100. If you buy it below £100 and hold it to maturity, part of your return is the coupon and part is the rise from your purchase price up to £100. That rise is the point of interest to taxpayers, because it is treated differently from the coupon. See {_gs(_gp("tax"), "why the gain is exempt from CGT but the coupon is taxed")}.</p>

<h2 id="example">A worked example (hypothetical)</h2>
<p class="hint"><strong>Example only.</strong> This is not a real gilt or a real price. Assumptions: a gilt with a 1% coupon and exactly two years to maturity, bought just after a coupon payment (so no accrued interest) at a clean price of £95.00 per £100 nominal, £1,000 nominal, ignoring dealing costs.</p>
<table><thead><tr><th>Item</th><th>Amount</th></tr></thead><tbody>
<tr><td>You pay (£1,000 nominal × £95 ÷ £100)</td><td>£950</td></tr>
<tr><td>Coupons over two years (1% × £1,000 × 2)</td><td>£20</td></tr>
<tr><td>Repaid at maturity</td><td>£1,000</td></tr>
<tr><td>Total return before tax (£20 + £1,000 − £950)</td><td>£70</td></tr>
<tr><td>Of which comes from the rise to £100</td><td>£50</td></tr>
</tbody></table>
<p>In this example £50 of the £70 is the rise to £100 and only £20 is coupon. The calculator above does the same sum for real gilts, using each gilt’s coupon and maturity date from DMO data and a price you enter.</p>

<h2 id="risks">What can go wrong</h2>
<ul>
<li><strong>Price risk.</strong> If you sell before maturity the market price may be below what you paid.</li>
<li><strong>Not a bank deposit.</strong> Gilts are government debt, not savings accounts, so they are not covered by the {_gl("fscs", "FSCS deposit limit")} that applies to bank and building society deposits.</li>
<li><strong>Inflation.</strong> A conventional gilt’s payments are fixed in pounds, so rising prices reduce what they buy.</li>
<li><strong>Costs.</strong> Brokers and platforms can charge for dealing and holding gilts.</li>
</ul>''',
 ["dmo", "dmodata", "fscs"])

# ---------- 2. CGT vs coupon ----------
_g_page("tax",
 "Gilts and Tax: Why the Gain Is Free of CGT but the Coupon Is Taxed – MoneyBySharma",
 "Why gilt gains are exempt from Capital Gains Tax but the coupon is taxed as savings income, with the Personal Savings Allowance and a hypothetical example.",
 "Gilts and tax", "Why the gain on a gilt is free of CGT but the coupon is taxed",
 "Gilts are taxed in two different ways: the coupon as income, the gain as an exempt capital gain. Here is the rule, the allowances and a worked example. Information, not financial advice.",
 f'''
<h2 id="short">The short version</h2>
<table><thead><tr><th>Part of your return</th><th>Tax treatment (individuals, 2026/27)</th><th>Source</th></tr></thead><tbody>
<tr><td>Gain (the rise in price, including up to £100 at maturity)</td><td>Not a chargeable gain, so no Capital Gains Tax. HMRC says gains <em>or losses</em> on gilts are exempt, so a loss is not an allowable loss either.</td><td>{_gl("cgt", "GOV.UK CGT")}; {_gl("s115", "TCGA 1992 s115")}; {_gl("cg534", "HMRC CG53400")} ({_G_CHK})</td></tr>
<tr><td>Coupon (the interest)</td><td>Taxed as interest, which is savings income. The Personal Savings Allowance and starting rate for savings can cover some or all of it.</td><td>{_gl("s369", "ITTOIA 2005 s369")}; {_gl("psa", "GOV.UK savings interest")} ({_G_CHK})</td></tr>
</tbody></table>

<h2 id="why">Why the two are treated differently</h2>
<p>Parliament exempted gilts from Capital Gains Tax: section 115 of the Taxation of Chargeable Gains Act 1992 says a gain on the disposal of gilt-edged securities “shall not be a chargeable gain”. HMRC’s manual says profits and losses on gilts are not charged under an income regime either, apart from gilt strips ({_gl("saim22", "SAIM2230")}, {_gl("saim30", "SAIM3040")}). The coupon is different: income tax is charged on interest, and the interest on a gilt is a coupon. We found no mention of gilts in the Budget 2026 tax document we checked ({_gl("ootlar", "Budget 2026 overview of tax legislation and rates")}), and section 115 on legislation.gov.uk was up to date to 24 November 2026.</p>
<p>That is why a low-coupon gilt bought below £100 can be tax-efficient: more of the return arrives as the exempt gain and less as taxable coupon. The same does not apply to gilt strips, which are taxed as income.</p>

<h2 id="coupon">How the coupon is taxed</h2>
<ul>
<li><strong>It is paid gross.</strong> The DMO’s taxation page says interest on registered gilts is payable without tax deducted ({_gl("dmotax")}, a 2016 page, so check it is still current).</li>
<li><strong>It counts as savings income.</strong> That is the same bucket as bank interest ({_gl("psa18")}).</li>
<li><strong>Personal Savings Allowance.</strong> £1,000 of savings interest is tax-free for basic-rate taxpayers, £500 for higher-rate taxpayers and £0 for additional-rate taxpayers. The starting rate for savings can also apply, up to £5,000 of interest, if your other taxable income is under £17,570 ({_gl("psa")}, {_G_CHK}).</li>
<li><strong>Reporting.</strong> Because no tax is taken off, you may need to tell HMRC about the coupon above your allowances, for example on a Self Assessment return.</li>
</ul>

<h2 id="ais">Accrued Income Scheme</h2>
<p>When gilts change hands, part of the price is accrued interest. The Accrued Income Scheme taxes the seller on interest built up to the sale and gives the buyer relief for interest they paid for. It does not apply if the total nominal value of all your securities was £5,000 or less at all times in the tax year and the previous one ({_gl("ais")}, {_G_CHK}). Above £5,000 it applies to any transfer, however small. Gilts go ex-dividend 7 business days before each coupon date ({_gl("exdiv")}).</p>

<h2 id="example">A worked example (hypothetical)</h2>
<p class="hint"><strong>Example only.</strong> Assumptions: the same imaginary gilt as in {_gs(_gp("what"), "our first article")} (£1,000 nominal bought at £950, £20 of coupons over two years, £1,000 repaid, £70 total return before tax); a higher-rate taxpayer paying 40% on savings interest in 2026/27; savings allowances ignored; no dealing costs, accrued interest or compounding.</p>
<table><thead><tr><th></th><th>Gilt (£20 coupon + £50 exempt gain)</th><th>If all £70 were taxable interest</th></tr></thead><tbody>
<tr><td>Return before tax</td><td>£70</td><td>£70</td></tr>
<tr><td>Tax at 40%</td><td>£8 (on the £20 coupon)</td><td>£28 (on £70)</td></tr>
<tr><td>Left after tax</td><td>£62</td><td>£42</td></tr>
</tbody></table>
<p>The difference comes entirely from the £50 that is a gain rather than interest.</p>

<h2 id="rates">Rates from April 2027</h2>
<p>At Budget 2026 the government announced that from 2027 to 2028 the savings income tax rates will be 24% (basic), 44% (higher) and 49% (additional), to be legislated in Finance Bill 2026-27 ({_gl("ootlar")}, {_G_CHK}). They are not law until that Bill passes. Gilt coupons are savings income, so they would be taxed at the new rates if enacted.</p>
{_DMO_NOTE}''',
 ["cgt", "s115", "cg534", "saim22", "saim30", "s369", "psa", "psa18", "ais", "exdiv", "ootlar", "dmotax"])

# ---------- 3. Gilts vs fixed-rate bonds and easy access (higher-rate) ----------
_g_page("vs",
 "Gilts vs Fixed Bonds and Easy-Access Savings (Higher-Rate) – MoneyBySharma",
 "How a gilt held to maturity differs from a bank fixed-rate bond and an easy-access account for a higher-rate taxpayer: tax, access and protection. Information only.",
 "Gilts vs savings (higher-rate)", "Gilts vs fixed-rate bonds and easy-access savings for higher-rate taxpayers",
 "How three ways of holding cash-like money differ in tax, access and protection if you pay 40% tax on savings interest. This is not a ranking. Information, not financial advice.",
 f'''
<h2 id="who">Who this is about</h2>
<p>Higher-rate here means taxable income of £50,271 to £125,140 in England in 2026/27, taxed at 40% ({_gl("rates")}, {_G_CHK}; Scotland has different bands). A higher-rate taxpayer’s Personal Savings Allowance is £500 a year, so interest above that is taxed at 40% ({_gl("psa")}).</p>

<h2 id="table">Side by side</h2>
<table><thead><tr><th></th><th>Gilt held to maturity</th><th>Bank fixed-rate bond</th><th>Easy-access account</th></tr></thead><tbody>
<tr><td>What it is</td><td>UK government debt, fixed coupon, repaid at £100 per £100 nominal on maturity</td><td>A deposit locked for a set term at a fixed rate</td><td>A deposit you can usually withdraw from at any time</td></tr>
<tr><td>Return</td><td>Coupon plus any gain from your purchase price to £100</td><td>Interest at the agreed rate (terms vary by provider)</td><td>Variable interest; the provider can change the rate</td></tr>
<tr><td>Tax on the return</td><td>Coupon is savings income; the gain is exempt from CGT ({_gl("s115", "TCGA s115")})</td><td>All interest is savings income</td><td>All interest is savings income</td></tr>
<tr><td>Access before the end</td><td>Sell through a broker at the market price, which can be above or below what you paid</td><td>Depends on the provider’s terms; many restrict or penalise early withdrawal, so check</td><td>Usually any time (check the account’s terms)</td></tr>
<tr><td>Protection</td><td>Government debt, not a deposit, so not covered by FSCS deposit protection</td><td>FSCS covers eligible deposits up to £120,000 per person per authorised firm ({_gl("fscs", "FSCS")})</td><td>Same FSCS limit as the bond</td></tr>
</tbody></table>
<p class="hint">We do not quote current rates here, because they change daily. Check the provider’s own page for a bank product, and your broker or the {_gl("dmodata", "DMO")} for gilt details.</p>

<h2 id="tax">What changes for a higher-rate taxpayer</h2>
<p>With a £500 allowance and 40% tax above it, most of a higher-rate taxpayer’s bank interest is taxed. A low-coupon gilt held to maturity shifts some of the return from taxable coupon to an exempt gain. The calculator turns this into an “equivalent gross savings rate”: the AER a savings account would need to pay to match the gilt after tax, worked out as net yield ÷ (1 − tax rate).</p>

<h2 id="example">A worked example (hypothetical)</h2>
<p class="hint"><strong>Example only.</strong> Assumptions: an imaginary gilt with a 1% coupon, exactly two years to maturity and no accrued interest, bought at a clean price of £95.00 per £100 nominal and held to maturity; no dealing costs; savings allowances ignored; calculated with the same method as our calculator (semi-annual compounding, yields shown as an annual effective rate).</p>
<table><thead><tr><th>Tax rate on savings interest</th><th>Net yield after tax</th><th>Equivalent gross savings rate</th></tr></thead><tbody>
<tr><td>40% (higher rate, 2026/27)</td><td>about 3.23% a year</td><td>about 5.38% a year</td></tr>
<tr><td>44% (higher rate from April 2027, announced, not law yet)</td><td>about 3.18% a year</td><td>about 5.69% a year</td></tr>
</tbody></table>
<p>Read that as: under these made-up assumptions, a savings account would need to pay about 5.38% AER before tax to leave a 40% taxpayer with the same after-tax return. The inputs are invented to show the method. Real gilts, prices and savings rates will differ, which is why the calculator lets you enter your own.</p>

<h2 id="weigh">What else to weigh</h2>
<ul>
<li><strong>Do you need the money before the end date?</strong> A gilt can be sold, but not at a guaranteed price. An easy-access deposit has no market price that moves, and eligible deposits are covered by FSCS up to £120,000 per person per authorised firm.</li>
<li><strong>Is the rate fixed?</strong> A gilt’s coupon and a fixed bond’s rate are fixed. An easy-access rate can change.</li>
<li><strong>Could an ISA do the job?</strong> Interest in a cash ISA is tax-free, within the £20,000 yearly ISA allowance ({_gl("isa")}). See our {_gs("cash-isas.html", "cash ISAs guide")}. The tax advantage of low-coupon gilts matters less inside an ISA, where neither coupon nor gain is taxed.</li>
<li><strong>Admin.</strong> Gilts held outside a wrapper can mean declaring the coupon, and the Accrued Income Scheme if your holdings pass £5,000 nominal ({_gl("ais")}).</li>
</ul>''',
 ["rates", "psa", "s115", "fscs", "isa", "ais", "dmodata", "ootlar"])

# ---------- 4. How to buy gilts ----------
_g_page("buy",
 "How to Buy Gilts: Through an ISA, a SIPP or a General Account (UK) – MoneyBySharma",
 "How individuals buy UK gilts, and how a stocks and shares ISA, a SIPP and a general account differ on eligibility, limits and tax. Information only.",
 "How to buy gilts", "How to buy gilts through an ISA, a SIPP or a general account",
 "Ways to buy a gilt, and how the tax treatment differs between a stocks and shares ISA, a SIPP and an account with no tax wrapper. Information, not financial advice.",
 f'''
<h2 id="ways">How individuals buy gilts</h2>
<p>The DMO says gilts can be bought in the secondary market through a stockbroker or a bank, or through its Purchase and Sale Service, which is open only to its Approved Group of investors. It also says gilts can no longer be bought from the Bank of England, National Savings &amp; Investments or the Post Office ({_gl("dmofaq")}, {_G_CHK}). In practice most people use a stockbroker, bank or investment platform. Not every provider offers gilts, so check before you open an account. We do not recommend any provider.</p>
<ol>
<li><strong>Choose the account type</strong> (see the table below).</li>
<li><strong>Pick the gilt.</strong> Coupon, maturity date and the list of gilts in issue are on the {_gl("dmodata", "DMO’s gilts in issue page")}. Our {_gs(_G_CALC, "calculator")} shows the yield after tax for a price you enter.</li>
<li><strong>Place the order</strong> for an amount of nominal value. The price you see is usually the clean price.</li>
<li><strong>Expect accrued interest.</strong> A buyer normally pays accrued interest on top of the clean price. A gilt goes ex-dividend 7 business days before each coupon date, and a buyer who settles after that date does not get that coupon, so the price is adjusted ({_gl("dmo", "DMO – About gilts")}; {_gl("exdiv")}).</li>
<li><strong>Check the costs.</strong> Brokers and platforms can charge dealing commission and account fees, so check the charges before you deal.</li>
</ol>

<h2 id="accounts">Three ways to hold a gilt</h2>
<table><thead><tr><th></th><th>Stocks and shares ISA</th><th>SIPP</th><th>General account (no wrapper)</th></tr></thead><tbody>
<tr><td>Can it hold gilts?</td><td>Yes: stocks and shares ISAs can include government bonds ({_gl("isahow", "GOV.UK")})</td><td>A SIPP lets you choose the investments ({_gl("sipp", "GOV.UK")}); check your provider’s list</td><td>Yes</td></tr>
<tr><td>Who can use it</td><td>UK-resident adults aged 18 or over ({_gl("isa")})</td><td>Anyone the provider accepts; GOV.UK says to check the provider is FCA-registered and the scheme is registered with HMRC ({_gl("sipp", "GOV.UK")})</td><td>Anyone</td></tr>
<tr><td>Limit</td><td>£20,000 a year across all your ISAs in 2026/27</td><td>Tax relief on contributions up to 100% of your annual earnings ({_gl("relief", "GOV.UK")}); £60,000 annual allowance, which can be lower ({_gl("aa")})</td><td>None</td></tr>
<tr><td>Tax on coupon</td><td>None while it stays in the ISA ({_gl("isahow", "GOV.UK")})</td><td>Income is exempt from income tax inside the pension ({_gl("ptm")})</td><td>Taxed as savings income, after your allowances</td></tr>
<tr><td>Tax on gain</td><td>None</td><td>Exempt from CGT inside the pension ({_gl("ptm")})</td><td>Exempt from CGT on gilts ({_gl("s115", "TCGA s115")})</td></tr>
<tr><td>Getting the money out</td><td>Savings stay tax-free for as long as they are in the ISA ({_gl("isahow", "GOV.UK")})</td><td>Normal minimum pension age is 55, rising to 57 in April 2028 ({_gl("nmpa")}); you usually pay tax on pension income ({_gl("taxpen")})</td><td>Sell any time the market is open; coupon may need declaring</td></tr>
</tbody></table>

<h2 id="matters">Does the wrapper matter for low-coupon gilts?</h2>
<p>Outside a wrapper, a low-coupon gilt’s tax edge comes from the gain being exempt while the coupon is taxed ({_gs(_gp("tax"), "see the tax article")}). Inside an ISA or a SIPP neither coupon nor gain is taxed, so the split between coupon and gain stops mattering for tax, and the price, yield and your own needs are what is left to compare. A SIPP also adds tax relief on contributions, but money is locked away until pension age ({_gl("relief")}).</p>
<p>Compare how the same gilt looks to a higher-rate taxpayer in {_gs(_gp("vs"), "gilts vs fixed-rate bonds and easy-access savings")}.</p>
{_DMO_NOTE}''',
 ["dmofaq", "dmo", "dmodata", "exdiv", "isa", "isahow", "sipp", "aa", "relief", "ptm", "nmpa", "taxpen", "s115"])
