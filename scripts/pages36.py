# pages36.py - Gilts hub (PREVIEW: branch gilts-hub-preview only).
# Exec'd after the search index so the hub stays out of search. Added to PREVIEW_PAGES:
# noindex and off the sitemap. Not in GUIDES, so no sign-up form.
# The new top-nav "Gilts" link is added in scripts/build.py (NAVG) and only exists on this branch.
_GH = "gilts-hub.html"
pages[_GH] = page(
    _GH,
    "Gilts: UK Guides and Calculator – MoneyBySharma",
    "A short hub for UK gilts: the main guide, four supporting articles, and the gilt vs savings calculator. Information only, not financial advice.",
    ph("Gilts", "Gilts", "UK government bonds, gathered in one place: the main guide, four short articles and a calculator.")
    + W("""
<p>A gilt is a bond issued by the UK government. These pages explain how gilts work, how they are taxed, how they compare with savings, and how you can hold them. The calculator lets you compare a gilt held to maturity with a savings account after tax, using a price you enter.</p>
<p class="hint"><strong>This is information, not financial advice.</strong> It does not take your circumstances into account and is not a personal recommendation to buy, sell or hold any gilt or other product. Gilts can fall in price, and tax rules can change. If in doubt, speak to an FCA-authorised adviser.</p>
<div class="grid g3">
<a class="card" href="gilts.html"><span class="tag">Guide</span><h2 style="margin:.4rem 0">Gilts, explained</h2><p>What a gilt is, why low-coupon gilts can be tax-efficient, and the gilt vs savings calculator on the same page.</p><span class="btn">Read the guide →</span></a>
<a class="card" href="what-is-a-gilt.html"><span class="tag">Article</span><h2 style="margin:.4rem 0">What is a gilt? How low-coupon gilts work</h2><p>Nominal value, coupon, maturity and price, and why a gilt bought below &#163;100 earns part of its return as a gain at maturity.</p><span class="btn">Read the article →</span></a>
<a class="card" href="gilts-cgt-and-coupon-tax.html"><span class="tag">Article</span><h2 style="margin:.4rem 0">Why the gain is free of CGT but the coupon is taxed</h2><p>The CGT exemption, how the coupon is taxed as savings income, the Personal Savings Allowance and the Accrued Income Scheme.</p><span class="btn">Read the article →</span></a>
<a class="card" href="gilts-vs-fixed-rate-bonds-and-savings.html"><span class="tag">Article</span><h2 style="margin:.4rem 0">Gilts vs fixed-rate bonds and easy-access savings</h2><p>How the three compare for a higher-rate taxpayer: tax, access and protection, with a hypothetical worked example.</p><span class="btn">Read the article →</span></a>
<a class="card" href="how-to-buy-gilts.html"><span class="tag">Article</span><h2 style="margin:.4rem 0">How to buy gilts through an ISA, a SIPP or a general account</h2><p>Ways to buy a gilt, and how the tax treatment differs in a stocks and shares ISA, a SIPP and an account with no wrapper.</p><span class="btn">Read the article →</span></a>
<a class="card" href="calculators/gilt-vs-savings.html"><span class="tag">Calculator</span><h2 style="margin:.4rem 0">Gilt vs savings calculator</h2><p>Compare a gilt held to maturity with a savings account after tax, for your tax band. Illustration only, not a quote or advice.</p><span class="btn">Open the calculator →</span></a>
</div>
"""),
)
PREVIEW_PAGES.add(_GH)
pages[_GH] = pages[_GH].replace('<link rel="icon"', '<meta name="robots" content="noindex"><link rel="icon"', 1)
