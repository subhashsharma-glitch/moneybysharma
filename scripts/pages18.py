# Annuities page (exec'd from build.py after pages17). Reference rates come ONLY from data/annuity-rates.json, which copies a
# published, dated market table. Combinations not in that table show "estimate not available"; no invented adjustment factors.
import json as _json
AN = _json.load(open("data/annuity-rates.json"))
AN_CHK = "20 Oct 2026"
def _x(h,t): return f'<a href="{h}" target="_blank" rel="noopener">{t}</a>'
AN_PROV = [
 ("Aviva","https://www.aviva.co.uk/retirement/pension-annuity/","Pension annuity: standard and enhanced options."),
 ("Canada Life","https://www.canadalife.co.uk/retirement/annuities/","Lifetime annuities, including enhanced options."),
 ("Just","https://www.justadviser.com/products/guaranteed-solutions/guaranteed-income-for-life/","Pension Annuity (Guaranteed Income for Life), based on health and lifestyle details. Just's official product page is on its adviser site; it is sold through advisers and brokers."),
 ("Legal &amp; General","https://www.legalandgeneral.com/retirement/pension-annuity/","Pension Annuity: level or increasing income, guarantee periods up to 30 years, dependant's income."),
 ("Scottish Widows","https://www.scottishwidows.co.uk/retirement/retirement-options/your-pension-options/guaranteed-income.html","Standard and enhanced annuities. Non-customers buy through an adviser or intermediary; minimum £10,000 after tax-free cash."),
 ("Standard Life","https://www.standardlife.co.uk/retirement/options/pension-annuity","Pension annuity; minimum pot £10,000, maximum age 85."),
]
_rows = "".join(f'<li class="an-prov"><h3>{_x(u,n+" ↗")}</h3><p>{d}</p><p class="an-rate"><b>Rates on request:</b> get a quote via {_x("https://comparison.moneyhelper.org.uk/en/tools/annuities","MoneyHelper")} or the provider.</p><p class="src">Official page checked {AN_CHK}. No published rate table found on this page.</p></li>' for n,u,d in AN_PROV)
_ages = AN["ages"]; _sm = AN["smoker_example"]
_tbl_rows = ""
_lbl = {"single|level|0":"Single life, level, no guarantee","single|level|5":"Single life, level, 5-year guarantee","single|rpi|5":"Single life, RPI-linked, 5-year guarantee","single|3pc|5":"Single life, rising 3% a year, 5-year guarantee","joint|level|0":"Joint life (50% to partner), level, no guarantee","joint|3pc|0":"Joint life (50% to partner), rising 3% a year, no guarantee"}
for k,v in AN["rates"].items():
    _tbl_rows += f'<tr><th scope="row">{_lbl[k]}</th>' + "".join(f'<td class="num">£{x:,}</td>' for x in v) + "</tr>"
_src = f'{_x(AN["source_url"],"Hargreaves Lansdown annuity rate table")}, quotes dated 15 Oct 2026, checked {AN_CHK}'
AN_BODY = ph("Guides › Pensions › Annuities", "Annuities: income estimate and providers",
 "What an annuity is, a rough income estimate from published market rates, and the main UK providers. Information only, not advice.") + W(f'''
<p class="banner">Information only, not financial advice. MoneyBySharma has no affiliation with any provider listed and receives no payment or commission.</p>
<p>An annuity swaps some or all of your pension pot for a guaranteed income, usually for the rest of your life. Once bought it normally can't be changed or cashed in, so it's worth understanding the options first. {_x("https://www.moneyhelper.org.uk/en/pensions-and-retirement/pension-wise","Pension Wise")}, from MoneyHelper, offers a free, impartial, government-backed appointment explaining your options if you're 50 or over with a defined contribution pension.</p>
<section class="calc" id="calc" aria-labelledby="an-h"><h2 id="an-h" style="margin-top:0">Annuity income estimate</h2>
<form id="an-form" class="fields" novalidate>
<div><label for="an-pot">Pension pot (£)</label><input id="an-pot" type="number" value="100000" min="0" step="1000" inputmode="decimal"></div>
<div><label for="an-age">Your age</label><input id="an-age" type="number" value="65" min="40" max="100" step="1" inputmode="numeric"></div>
<div><label for="an-life">Single or joint life</label><select id="an-life"><option value="single">Single life (income stops when you die)</option><option value="joint">Joint life (50% continues to your partner)</option></select></div>
<div><label for="an-esc">Level or increasing</label><select id="an-esc"><option value="level">Level (stays the same)</option><option value="rpi">Rises with RPI inflation</option><option value="3pc">Rises 3% a year</option></select></div>
<div><label for="an-g">Guarantee period</label><select id="an-g"><option value="0">None</option><option value="5">5 years</option><option value="10">10 years</option></select></div>
<div><label for="an-tfc">Take 25% tax-free cash first?</label><select id="an-tfc"><option value="yes">Yes, take 25% first</option><option value="no">No, use the whole pot</option></select></div>
</form>
<div id="an-out" aria-live="polite"></div>
<p class="src">Reference rates: {_src}. These are the highest standard quotes HL's tool found across the providers it compares for a £100,000 purchase (average postcode, paid monthly in advance; joint life assumes a partner 3 years younger). We use the published figure for the nearest age at or below yours and apply it in proportion to the amount you'd use. We don't adjust for anything the source doesn't publish, so other combinations show "not available". Your actual quote will differ and is likely to be lower for small pots.</p>
<script type="application/json" id="an-data">{_json.dumps({"ages":_ages,"rates":AN["rates"],"src":"Hargreaves Lansdown annuity rate table","url":AN["source_url"],"dated":"15 Oct 2026","checked":AN_CHK})}</script>
</section>
<h2 id="table">The published reference figures</h2>
<p>Annual income before tax from a £100,000 annuity purchase. Source: {_src}.</p>
<div class="table-scroll"><table><thead><tr><th scope="col">Annuity type</th>{"".join(f'<th scope="col" class="num">Age {a}</th>' for a in _ages)}</tr></thead><tbody>{_tbl_rows}</tbody></table></div>
<h2 id="tfc">What the 25% tax-free cash does</h2>
<p>From age 55 (57 from 6 April 2028) you can usually take up to 25% of your pension as a tax-free lump sum, up to a lifetime limit of £268,275 (the Lump Sum Allowance). If you take it before buying an annuity, only the remaining 75% buys income, so your annuity is smaller. Annuity income itself is taxable like a salary. You can't add the cash back later to boost the annuity, so think about what you'd use it for.</p>
<h2 id="enhanced">Enhanced annuities: health and lifestyle</h2>
<p>If you have a health condition (such as diabetes, high blood pressure or heart problems) or lifestyle factors (such as smoking or being overweight), providers may expect to pay you for a shorter time and offer a higher income. This is called an enhanced annuity. Even common conditions can count, so it's worth answering the health questions fully when you get quotes.</p>
<p>Published example: for a 65-year-old buying a single life, level annuity with no guarantee, HL's table shows £{_sm["standard"]:,} a year from £100,000 at standard rates and £{_sm["smoker"]:,} for someone who has {_sm["profile"]} (quotes dated 15 Oct 2026). Our calculator shows standard rates only.</p>
<h2 id="drawdown">Drawdown versus annuity</h2>
<div class="table-scroll"><table><thead><tr><th scope="col"></th><th scope="col">Annuity</th><th scope="col">Drawdown</th></tr></thead><tbody>
<tr><th scope="row">Income</th><td>Guaranteed, set when you buy</td><td>You choose how much to take; it isn't guaranteed</td></tr>
<tr><th scope="row">Investment risk</th><td>None for you</td><td>Pot stays invested and can fall as well as rise</td></tr>
<tr><th scope="row">Running out</th><td>Can't run out; pays for life</td><td>Can run out if you take too much or investments fall</td></tr>
<tr><th scope="row">Flexibility</th><td>Can't usually change once bought</td><td>Change or stop withdrawals at any time</td></tr>
<tr><th scope="row">When you die</th><td>Stops unless you chose a joint life, guarantee or value protection</td><td>What's left can usually pass to your beneficiaries</td></tr>
</tbody></table></div>
<p>You don't have to choose one: some people use part of their pot for an annuity to cover essential bills and keep the rest in drawdown, or buy an annuity later, when rates for their age are higher.</p>
<h2 id="compare">Comparing quotes</h2>
<p>You don't have to buy from your current pension provider. {_x("https://comparison.moneyhelper.org.uk/en/tools/annuities","MoneyHelper's annuity comparison tool")} compares quotes across the market and is impartial and backed by government. A regulated financial adviser can recommend a product, usually for a fee.</p>
<h2 id="providers">UK annuity providers (A to Z)</h2>
<p class="note">Listed alphabetically, not ranked. Information only, no affiliation: MoneyBySharma isn't linked to any of these providers and doesn't receive payment from them. None of these official pages published an annuity rate table when we checked on {AN_CHK}.</p>
<ul class="an-provs">{_rows}</ul>
<h2 id="scams">Pension scam warning</h2>
<p class="banner">Be wary of cold calls, texts or emails about your pension, offers of a "free pension review", promises of high returns or early access before 55, and pressure to decide quickly. Check any firm on the FCA Register before you act. See the FCA's {_x("https://www.fca.org.uk/scamsmart","ScamSmart")} guidance and its {_x("https://www.fca.org.uk/consumers/pension-scams","pension scams page")}.</p>
<p class="src">Information only, not financial advice. Rates change often, and quotes are only guaranteed for a short time. Sources checked {AN_CHK}. Also see our <a href="pensions.html">Pensions guide</a> and <a href="scams-fraud.html">Scams &amp; fraud</a>.</p>
''')
pages["annuities.html"] = page("annuities.html","Annuities: income estimate, options and UK providers | MoneyBySharma",
 "Estimate annuity income from published, dated market rates, understand enhanced annuities, drawdown and tax-free cash, and see UK annuity providers A to Z. Information only.",
 AN_BODY, scripts=("annuity-calc.js",))
_pp = pages["pensions.html"]
_cta = '<p class="note"><b>Thinking about an annuity?</b> See our <a href="annuities.html">annuities page</a>: an income estimate from published market rates, enhanced annuities, drawdown versus annuity, and UK providers A to Z.</p>'
if 'Thinking about an annuity' not in _pp and '<h2 id="young">' in _pp:
    pages["pensions.html"] = _pp.replace('<h2 id="young">', _cta + '<h2 id="young">', 1)
