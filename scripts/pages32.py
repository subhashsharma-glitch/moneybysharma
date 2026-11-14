# Preview only (calculators-preview branch): one standalone calculator page at
# calculators/compound-interest.html, plus a link to it from savings.html.
# Not in the nav, sitemap or search index. Reuses assets/calc-ui6.js.
import os as _c32_os, re as _c32_re

_C32_FN = "calculators/compound-interest.html"
_C32_CALC = _c32_re.search(
    r'<section class="calc" id="grow-calc".*</section>', GROW, _c32_re.S
).group(0)
# Standalone page uses #calc as the section id; form IDs stay the same so calc-ui6.js works.
_C32_CALC = _C32_CALC.replace('id="grow-calc"', 'id="calc"', 1)

_C32_TITLE = "Compound Interest Calculator UK – MoneyBySharma"
_C32_DESC = (
    "A UK compound interest calculator: compare simple and compound interest, see the AER, "
    "and estimate how long money takes to double. Plain English, illustration only, not financial advice."
)
pages[_C32_FN] = page(
    _C32_FN,
    _C32_TITLE,
    _C32_DESC,
    ph(
        "Compound interest calculator",
        "Compound interest calculator",
        "See how simple and compound interest compare, what the AER is, and how long money takes to double.",
    )
    + W(
        '''
<p>Simple interest is paid only on the amount you first put in. Compound interest is paid on that amount <em>and</em> on the interest already added, so growth can build on itself. Savings accounts normally pay compound interest.</p>
<p>This is the same calculator as on our <a href="savings.html#grow">Savings guide: how interest grows</a>, where you'll also find a worked example and a fuller explanation of the Rule of 72.</p>
'''
        + _C32_CALC
        + '''
<p class="hint">Information only, not financial advice. The figures are an illustration with a fixed rate, no tax and no withdrawals. Real accounts can change their rate. This is not a forecast or a recommendation.</p>
<p class="related" style="margin:1.5rem 0 2rem"><strong>Related:</strong> <a href="savings.html#grow">How interest grows</a> · <a href="savings.html">Savings and cash ISAs</a> · <a href="power-of-compounding.html">The power of compounding</a></p>
'''
    ),
    scripts=("calc-ui6.js",),
)

def _c32_fix(h, depth=1):
    pre = "../" * depth
    return _c32_re.sub(
        r'(\s(?:href|src|action)=")(?!https?:|mailto:|#|/|data:|\.\./)([^"]*)"',
        lambda m: f'{m.group(1)}{pre}{m.group(2)}"',
        h,
    )

pages[_C32_FN] = _c32_fix(pages[_C32_FN])

# Preview-only link on the Savings guide, back to the standalone page.
_c32_mk = '<p class="hint" style="grid-column:1/-1">Illustration only: a fixed rate, no tax, no withdrawals or extra deposits, before any inflation. Real accounts can change their rate. Not a forecast.</p></form></section>'
_c32_link = (
    _c32_mk
    + '\n<p class="hint"><a href="calculators/compound-interest.html">Open this calculator on its own page</a></p>'
)
assert pages["savings.html"].count(_c32_mk) == 1, "savings.html calculator marker not found"
pages["savings.html"] = pages["savings.html"].replace(_c32_mk, _c32_link, 1)

# Keep the preview page out of the sitemap until it is published.
PREVIEW_PAGES.add(_C32_FN)
print("calculators preview:", _C32_FN)
