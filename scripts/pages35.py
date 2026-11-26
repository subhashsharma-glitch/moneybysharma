# pages35.py – energy supporting articles (PREVIEW, 26 Nov 2026), written for Subhash's review.
# Two sets of four articles, each set built around an existing calculator:
#   home battery payback  (calculators/home-battery.html)  and  EV charging cost  (calculators/ev-charging.html)
# ENERGY_LIVE = False (build.py): preview only - noindex, off the sitemap, out of site search, no Article schema,
# no menu entry, and a "draft" notice at the top of each page. Set ENERGY_LIVE = True in build.py to publish:
# the pages then join search and the sitemap (like the gilt articles, they are not in GUIDES so get no sign-up card), and the
# draft notice disappears. Nothing here is added to the main menu either way.
# Every figure below is either a sourced fact (see each page's "Sources and dates checked" list, all checked
# 26 November 2026) or a clearly labelled hypothetical example worked through the calculator's own formulas.
_EA_LIVE = bool(globals().get("ENERGY_LIVE"))
_EA_CHK = "26 November 2026"

def _ea_src(label, url, note=""):
    n = f" {note}" if note else ""
    return f'<li><a href="{url}">{label}</a>{n}</li>'

_EA_SETS = {
 "bat": {
   "calc": ("calculators/home-battery.html", "Home battery payback calculator"),
   "guide": ("energy.html#battery", "Energy guide: home batteries"),
   "items": [
     ("home-battery-payback-explained.html", "How home battery payback is worked out"),
     ("home-battery-time-of-use-tariffs.html", "Time-of-use tariffs and home batteries"),
     ("home-battery-smart-export-guarantee.html", "The Smart Export Guarantee and home batteries"),
     ("home-battery-cost-vat-quotes.html", "Home battery costs, VAT and quotes"),
   ]},
 "ev": {
   "calc": ("calculators/ev-charging.html", "EV charging cost calculator"),
   "guide": ("electric-cars.html#calc", "Electric cars guide: running costs"),
   "items": [
     ("ev-charging-cost-per-mile-explained.html", "EV charging cost per mile, explained"),
     ("ev-home-vs-public-charging-cost.html", "Home vs public charging: cost per mile"),
     ("ev-tariffs-off-peak-charging.html", "EV tariffs and off-peak charging"),
     ("ev-charging-calculator-limits.html", "What the charging calculator leaves out"),
   ]},
}
ENERGY_FILES = [fn for s in _EA_SETS.values() for fn, _ in s["items"]]

_EA_DISC = ('<div class="card" style="background:#e7f2ef;border-left:5px solid #d9822b;margin:1.5rem 0"><p><strong>This is information, not financial advice.</strong> '
  'MoneyBySharma gives general information. It does not recommend any supplier, tariff, battery, charger, installer or product, and it is not authorised or regulated by the Financial Conduct Authority (FCA). '
  'Worked examples use made-up figures that are stated on the page. They are not quotes or forecasts. Your own prices, usage and circumstances will differ.</p></div>')
_EA_KEY = '<div class="card" style="background:#e7f2ef;border-left:5px solid #d9822b;margin:0 0 1.2rem"><p><strong>Key points</strong></p><ul>{}</ul></div>'
_EA_ASSUME = '<div class="card"><p><strong>Assumptions - an example, not a quote.</strong> {}</p></div>'.replace(" - ", " – ")

def _ea_page(key, fn, title, desc, short, lead, toc, body, sources):
    S = _EA_SETS[key]
    calc_fn, calc_name = S["calc"]
    guide_fn, guide_name = S["guide"]
    other = [(f, t) for f, t in S["items"] if f != fn]
    rel = "".join(f'<li><a href="{f}">{t}</a></li>' for f, t in other)
    if key == "bat":
        cross = '<li><a href="ev-tariffs-off-peak-charging.html">EV tariffs and off-peak charging</a> (the same kind of tariff, used for an electric car)</li>'
    else:
        cross = '<li><a href="home-battery-time-of-use-tariffs.html">Time-of-use tariffs and home batteries</a> (the same kind of tariff, used with a battery)</li>'
    crumb = f'<a href="calculators/index.html">Calculators</a> › <a href="{calc_fn}">{calc_name}</a> › {short}'
    draft = '' if _EA_LIVE else ('<div class="card" style="background:#fff7ec;border-left:5px solid #d9822b;margin:0 0 1.2rem"><p><strong>Draft for review – not published.</strong> '
        'This page is a preview. It is hidden from search engines, the menu, the sitemap and site search until it is approved.</p></div>')
    cta = (f'<div class="card feature" style="margin:0 0 1.5rem"><h2 style="margin-top:0" id="try">Try the numbers yourself</h2>'
           f'<p>Put your own figures into the <a href="{calc_fn}"><strong>{calc_name}</strong></a>. The values already in it are examples, so replace them with your own.</p>'
           f'<p><a class="btn" href="{calc_fn}">Open the {calc_name.lower()}</a></p></div>')
    tocs = "".join(f'<a href="#{i}">{t}</a>' for i, t in toc) + '<a href="#sources">Sources</a><a href="#more">More in this series</a>'
    inner = (f'{draft}{cta}<div class="cols"><div>\n{body}\n'
      f'<h2 id="sources">Sources and dates checked</h2><p class="hint">All sources below were opened on {_EA_CHK}. A source’s own publication or update date is shown where it has one.</p><ul>\n{"".join(sources)}\n</ul>\n'
      f'<h2 id="more">More in this series</h2><ul><li><a href="{calc_fn}"><strong>{calc_name}</strong></a></li>{rel}<li><a href="{guide_fn}">{guide_name}</a></li>{cross}</ul>\n'
      f'{_EA_DISC}\n</div><aside><div class="card toc"><h3>On this page</h3>{tocs}<p class="hint" style="margin-top:.8rem"><a href="{calc_fn}">Open the calculator</a></p></div></aside></div>')
    pages[fn] = page(fn, title, desc, ph(crumb, lead[0], lead[1]) + W(inner))

# ---------------------------------------------------------------- shared source snippets
_OFGEM_CAP = _ea_src("Ofgem – Energy price cap unit rates and standing charges", "https://www.ofgem.gov.uk/information-consumers/energy-advice-households/energy-price-cap-unit-rates-and-standing-charges",
  "(shows 26.32p/kWh for 1 Oct–31 Dec 2026 and 32.69p/kWh for 1 Jan–31 Mar 2027, Direct Debit averages; no VAT on electricity from 1 Oct 2026 to 30 June 2027; for multi-rate tariffs “together, they cannot be more than the price cap”)")
_OFGEM_PR = _ea_src("Ofgem – Energy price cap to rise by 26% from January 2027", "https://www.ofgem.gov.uk/press-release/energy-price-cap-rise-26-january-2027", "(press release, 25 November 2026)")
_EST_BATT = _ea_src("Energy Saving Trust – Battery storage", "https://energysavingtrust.org.uk/advice/battery-storage/", "(undated page)")
_EST_RES = _ea_src("Energy Saving Trust – What really cuts energy bills", "https://energysavingtrust.org.uk/renewable-technologies-what-really-cuts-energy-bills/", "(12 August 2026)")
_CA_TARIFF = _ea_src("Citizens Advice – Choosing your energy tariff", "https://www.citizensadvice.org.uk/consumer/energy/energy-supply/get-a-better-energy-deal/choosing-energy-tariff/")
_SEGB = _ea_src("Smart Energy GB – Using energy flexibly", "https://www.smartenergygb.org/using-your-smart-meter/understanding-energy/using-energy-flexibly", "(page last updated 14 April 2026)")
_SEGB2 = _ea_src("Smart Energy GB – Time-of-use tariffs", "https://www.smartenergygb.org/using-your-smart-meter/understanding-energy/time-of-use-tariffs-the-benefits", "(undated page)")
_ZAPMAP = _ea_src("Zapmap – UK EV Charging Price Index", "https://www.zapmap.com/ev-stats/charging-price-index", "(updated 25 November 2026; October 2026 data)")
_EST_SMART = _ea_src("Energy Saving Trust – Smart charging for electric vehicles", "https://energysavingtrust.org.uk/advice/smart-charging-electric-vehicles/", "(last updated 25 March 2025)")
_HMRC_RCB = _ea_src("GOV.UK / HMRC – Revenue and Customs Brief 13 (2026): VAT and Climate Change Levy on electric vehicle charging for non-domestic use", "https://www.gov.uk/government/publications/revenue-and-customs-brief-13-2026-vat-and-climate-change-levy-on-electric-vehicle-charging-for-non-domestic-use/vat-and-climate-change-levy-on-electric-vehicle-charging-for-non-domestic-use", "(published 28 October 2026)")
_EON = _ea_src("E.ON Next – Understanding where EV charging losses occur", "https://www.eonnext.com/electric-vehicles/guides/understanding-where-ev-charging-losses-occur", "(a supplier’s guide, undated; named here as a source only, not recommended)")
_WHICH = _ea_src("Which? – Revealed: the truth about electric car range", "https://www.which.co.uk/news/article/revealed-the-truth-about-electric-car-mileage-aC1bt9t5jU50", "(14 July 2022, so older than the other sources)")

# ================================================================ SET 1: HOME BATTERY
_ea_page("bat", "home-battery-payback-explained.html",
 "How Home Battery Payback Is Worked Out (UK Example)",
 "The sums behind a home battery payback figure: cheap rate, peak rate, efficiency, cycles, cost and fading capacity, with a worked example and clear assumptions.",
 "Payback explained",
 ("How home battery payback is worked out", "A payback figure sounds precise, but it is only as good as the five or six numbers behind it. Here are the sums, step by step, and which inputs move the answer most. Information, not financial advice."),
 [("idea","The idea"),("sums","The sums"),("example","Worked example"),("moves","What moves the answer"),("leaves","What it leaves out"),("ask","Questions to ask")],
'''
<div class="card" style="background:#e7f2ef;border-left:5px solid #d9822b;margin:0 0 1.2rem"><p><strong>Key points</strong></p><ul>
<li>Payback is the battery’s cost divided by what it saves each year. The saving comes from the gap between a cheap rate and the rate you avoid paying.</li>
<li>A battery loses some energy each time it is used, and it slowly loses capacity as it ages. Both reduce the saving.</li>
<li>In the example below, the battery does not pay back within its 12-year life. It takes a combination of changes to get it there.</li>
</ul></div>

<h2 id="idea">The idea</h2>
<p>In this calculator, a home battery on a cheap-rate tariff does one job. It charges when electricity is cheap, then supplies your home when electricity would otherwise cost more. The saving is the difference between the two prices, less the energy lost along the way. Whether that adds up to more than the battery’s cost depends on how big the difference is and how often you can use it.</p>
<p>This only works on a tariff with a cheaper rate at some times of day (see <a href="home-battery-time-of-use-tariffs.html">time-of-use tariffs and home batteries</a>). On a standard tariff the price is the same at any time, so there is no gap to use. Smart Energy GB says it is only cheaper to use electricity at night if you are on a tariff that charges less at night.</p>

<h2 id="sums">The sums, step by step</h2>
<p>These are the same steps the <a href="calculators/home-battery.html">home battery payback calculator</a> uses.</p>
<ol>
<li><strong>Energy you buy to fill the battery.</strong> Usable capacity ÷ round-trip efficiency. Because some energy is lost, you buy a bit more than you get back.</li>
<li><strong>What that charge costs.</strong> Energy bought × the cheap rate.</li>
<li><strong>What the same energy is worth when you use it.</strong> Usable capacity × the rate you avoid paying.</li>
<li><strong>Saving per cycle.</strong> Step 3 minus step 2.</li>
<li><strong>First-year saving.</strong> Saving per cycle × full cycles per year.</li>
<li><strong>Later years.</strong> The saving falls each year by the capacity loss (degradation) rate, because the battery holds less.</li>
<li><strong>Payback.</strong> The point where the running total of savings reaches the installed cost. If it never does within the battery’s lifespan, the calculator says so.</li>
</ol>

<h2 id="example">Worked example (hypothetical)</h2>
<div class="card"><p><strong>Assumptions – an example, not a quote.</strong> 5 kWh usable battery. 90% round-trip efficiency. Cheap rate 7p/kWh (made up). Rate avoided 32.69p/kWh (Ofgem’s average electricity unit rate for 1 January to 31 March 2027, Direct Debit). 300 full cycles a year. Cost £4,600 (the Energy Saving Trust’s figure for a 5 kWh battery system; a real quote will differ). 12-year lifespan. Capacity falls 2% a year (made up). These are the calculator’s starting values.</p></div>
<ul>
<li>Energy bought: 5 ÷ 0.90 = 5.56 kWh. Cost: 5.56 × 7p = about 39p.</li>
<li>Value when used: 5 × 32.69p = about £1.63.</li>
<li>Saving per cycle: £1.63 − £0.39 = about <strong>£1.25</strong>.</li>
<li>First-year saving: £1.25 × 300 = about <strong>£374</strong>.</li>
<li>Simple payback ignoring fading capacity: £4,600 ÷ £374 = about <strong>12.3 years</strong>. With 2% a year capacity loss, it does <strong>not pay back within 12 years</strong>.</li>
<li>Total saving over 12 years after fading: about £4,022, so a net result of about <strong>−£578</strong> after the £4,600 cost.</li>
</ul>
<p>On these assumptions the battery does not pay for itself within its life. That is not a verdict on any particular battery. The next table shows what would change the answer.</p>

<h2 id="moves">What moves the answer most</h2>
<p>Here is the same example with one input changed at a time, then two together. Everything else stays as above. The figures come from the calculator’s own formulas.</p>
<div class="table-scroll"><table><caption class="sr">One change at a time, then two together, hypothetical home battery example</caption><thead><tr><th scope="col">Change</th><th scope="col">First-year saving</th><th scope="col">Simple payback</th><th scope="col">Payback with fading capacity</th><th scope="col">Net result over 12 years</th></tr></thead><tbody>
<tr><td>Example as above</td><td>£374</td><td>12.3 years</td><td>Not within 12 years</td><td>−£578</td></tr>
<tr><td>365 cycles a year, not 300</td><td>£455</td><td>10.1 years</td><td>11.2 years</td><td>+£294</td></tr>
<tr><td>Cheap rate 12p, not 7p</td><td>£290</td><td>15.8 years</td><td>Not within 12 years</td><td>−£1,475</td></tr>
<tr><td>Efficiency 80%, not 90%</td><td>£359</td><td>12.8 years</td><td>Not within 12 years</td><td>−£735</td></tr>
<tr><td>Cost £3,500 (made up), not £4,600</td><td>£374</td><td>9.4 years</td><td>10.3 years</td><td>+£522</td></tr>
<tr><td>Rate avoided 26.32p, not 32.69p (the previous quarter’s average)</td><td>£278</td><td>16.5 years</td><td>Not within 12 years</td><td>−£1,606</td></tr>
<tr><td>Both of the 365-cycle and £3,500 changes together</td><td>£455</td><td>7.7 years</td><td>8.3 years</td><td>+£1,394</td></tr>
</tbody></table></div>
<p class="hint">The 26.32p row uses Ofgem’s average electricity unit rate for 1 October to 31 December 2026, the quarter before. The example’s 32.69p is the average for 1 January to 31 March 2027 (announced 25 November 2026). The price cap changes every three months, and the rate you actually avoid is your own tariff’s peak or day rate, which may be higher or lower than the cap.</p>
<p>Two lessons stand out. The <strong>gap between the cheap rate and the rate you avoid</strong> matters most. And you only gain from cycles you actually use, so a battery that sits part-empty because your evening demand is low saves less than the formula suggests.</p>

<h2 id="leaves">What the sums leave out</h2>
<ul>
<li><strong>Standing charges.</strong> A tariff with a cheap night rate may have a different daily standing charge from your current one. The calculator ignores this.</li>
<li><strong>Changing prices.</strong> The sums assume tariffs stay the same for the battery’s whole life. Ofgem’s average electricity unit rate alone moved from 26.32p to 32.69p per kWh between two consecutive quarters (1 October to 31 December 2026, then 1 January to 31 March 2027).</li>
<li><strong>Usable vs headline capacity.</strong> The Energy Saving Trust says a system stops taking electricity out of the battery at a set level, maybe around 20% of total capacity. Use the <em>usable</em> figure from the datasheet or quote.</li>
<li><strong>Lifespan and replacement.</strong> The Energy Saving Trust gives a typical battery lifespan of about 10 to 12 years and says to ask about warranties. The calculator ignores maintenance and inverter replacement.</li>
<li><strong>The time value of money.</strong> £556 saved in year 10 is worth less to you than £556 today.</li>
<li><strong>Solar and export payments.</strong> The calculator models grid-charged, cheap-rate use only. If you have solar panels, see <a href="home-battery-smart-export-guarantee.html">the Smart Export Guarantee and home batteries</a>.</li>
</ul>

<h2 id="ask">Questions to ask before relying on a payback figure</h2>
<ol>
<li>Which tariff is the saving based on, and what are its cheap and peak rates and standing charge?</li>
<li>How many full cycles a year are assumed, and do I have enough evening or peak demand to use them?</li>
<li>Is the capacity quoted usable capacity, and what round-trip efficiency is assumed?</li>
<li>What does the warranty cover, for how long, and does it set a limit on capacity loss?</li>
<li>Does the installed price include everything (installation, inverter, VAT)? See <a href="home-battery-cost-vat-quotes.html">costs, VAT and quotes</a>.</li>
</ol>
''',
 [_OFGEM_CAP, _OFGEM_PR, _EST_BATT, _SEGB])

_ea_page("bat", "home-battery-time-of-use-tariffs.html",
 "Time-of-Use Tariffs and Home Batteries: What to Check",
 "How time-of-use and off-peak electricity tariffs work, why a home battery needs one, and the questions to ask about rates, standing charges, smart meters and contracts.",
 "Time-of-use tariffs",
 ("Time-of-use tariffs and home batteries: what to check", "A home battery that charges on cheap electricity only makes sense on a tariff that has a cheap rate. Here is how those tariffs work and what to look at before you rely on one. Information, not financial advice."),
 [("why","Why you need one"),("types","Types of tariff"),("meter","Smart meters"),("three","Three things to check"),("example","Worked example"),("contract","Contracts and the cap"),("ask","Questions to ask")],
'''
<div class="card" style="background:#e7f2ef;border-left:5px solid #d9822b;margin:0 0 1.2rem"><p><strong>Key points</strong></p><ul>
<li>On a standard tariff, electricity costs the same at any time of day. A battery needs a tariff with a cheaper period to have anything to save.</li>
<li>The size of the gap between the cheap rate and the rate you avoid matters more than the cheap rate on its own.</li>
<li>Time-of-use tariffs usually need a smart meter, and you choose whether to change tariff.</li>
</ul></div>

<h2 id="why">Why a battery needs a time-of-use tariff</h2>
<p>A time-of-use tariff charges different prices at different times of the day or week. Citizens Advice describes the usual split as a peak (or day) rate and an off-peak (or night) rate, sometimes with more than two rates.</p>
<p>Smart Energy GB points out that on a fixed or standard variable tariff, the price you pay for electricity at night is no different from the price in the day. So a battery that fills overnight on a standard tariff saves nothing. The saving only exists where the tariff has a cheaper window.</p>
<p>The <a href="calculators/home-battery.html">home battery payback calculator</a> assumes exactly this set-up: it charges at a cheap rate and discharges when you would otherwise pay a higher one. The <a href="home-battery-payback-explained.html">payback article</a> shows the sums.</p>

<h2 id="types">Static and dynamic tariffs</h2>
<p>Citizens Advice splits time-of-use tariffs into two types, and says to check the terms to see which you are looking at:</p>
<ul>
<li><strong>Static:</strong> fixed prices for peak and off-peak rates, at fixed times. Economy 7 and most EV charging tariffs are examples, according to Smart Energy GB.</li>
<li><strong>Dynamic:</strong> the rates change based on wholesale market prices, so they can change from day to day. Some rates can even be negative, which means you could be paid to use electricity at those times. Citizens Advice says you may not get much notice, and that the supplier’s own price limit on these tariffs may be higher than the Ofgem price cap, or there may be none.</li>
</ul>
<p>A static tariff is easier to plan around. A dynamic tariff can offer a wider gap on some days, but your payback becomes harder to predict.</p>

<h2 id="meter">Smart meters</h2>
<p>Most time-of-use tariffs need a smart meter, because it sends readings every half hour so your supplier can charge the right rate for each period. Citizens Advice adds that if you have a two-rate (dual-rate) meter you may be able to use a tariff such as Economy 7 or Economy 10 without a smart meter.</p>
<p>Smart Energy GB also says that having a smart meter does not change your price. You only change tariff if you choose to.</p>

<h2 id="three">Three things to check</h2>
<ol>
<li><strong>The cheap rate and its hours.</strong> How many hours are cheap, and are they when the battery can charge? A short window may not fill a large battery.</li>
<li><strong>The rate you would avoid, and the standing charge.</strong> The “peak rate you avoid” in the calculator is <em>your tariff’s</em> peak or day rate, not necessarily the price cap. Ofgem notes that for multi-rate tariffs such as Economy 7, the peak and off-peak rates together cannot be more than the price cap. Rates on other tariffs can differ. Also compare daily standing charges.</li>
<li><strong>The rest of your home.</strong> The Energy Saving Trust notes that these tariffs usually apply to all the electricity used in the home. If your other use falls in the pricier hours, you may pay more for that part. The battery can cover some of it, but not necessarily all of it.</li>
</ol>

<h2 id="example">Worked example (hypothetical)</h2>
<div class="card"><p><strong>Assumptions – an example, not a quote.</strong> The same battery as in the <a href="home-battery-payback-explained.html">payback article</a>: 5 kWh usable, 90% round-trip efficiency, 300 full cycles a year, £4,600 cost (the Energy Saving Trust’s figure for a 5 kWh system), 12-year life, capacity falls 2% a year. The rate avoided is 32.69p/kWh (Ofgem’s average electricity unit rate for 1 January to 31 March 2027). Only the cheap rate changes, and the four cheap rates (5p, 7p, 12p, 20p) are made up for illustration.</p></div>
<div class="table-scroll"><table><caption class="sr">Effect of the cheap rate on a hypothetical home battery</caption><thead><tr><th scope="col">Cheap rate</th><th scope="col">Gap to 32.69p</th><th scope="col">First-year saving</th><th scope="col">Simple payback</th><th scope="col">Net result over 12 years</th></tr></thead><tbody>
<tr><td>5p</td><td>27.69p</td><td>£407</td><td>11.3 years</td><td>−£219</td></tr>
<tr><td>7p</td><td>25.69p</td><td>£374</td><td>12.3 years</td><td>−£578</td></tr>
<tr><td>12p</td><td>20.69p</td><td>£290</td><td>15.8 years</td><td>−£1,475</td></tr>
<tr><td>20p</td><td>12.69p</td><td>£157</td><td>29.3 years</td><td>−£2,910</td></tr>
</tbody></table></div>
<p class="hint">Simple payback ignores fading capacity. With fading capacity, none of these pays back within 12 years on these assumptions.</p>
<p>The gap shrinks by about half between the 7p and 20p rows, but the saving falls by well over half, from about £374 to about £157. That is because the energy lost in the battery is bought at the cheap rate too, so a narrow gap leaves very little margin.</p>
<p>The Energy Saving Trust’s August 2026 research modelled over a million combinations of technology and tariff. It found tariff choice mattered a great deal, and that batteries did better paired with a heat pump on a suitable tariff than with solar panels alone. Its figures are scenario-based, so your results will differ.</p>

<h2 id="contract">Contracts and the price cap</h2>
<ul>
<li><strong>Fixed tariffs</strong> keep your rates for the contract. Citizens Advice says that with 49 days or less left you can switch without an exit fee, but with 50 days or more you might have to pay one.</li>
<li><strong>The price cap</strong> limits unit rates and standing charges on default tariffs, and does not limit your total bill. Ofgem’s average electricity unit rate is 32.69p/kWh for 1 January to 31 March 2027, up from 26.32p/kWh for 1 October to 31 December 2026. These are national Direct Debit averages, and your own rate depends on your region and how you pay.</li>
</ul>

<h2 id="ask">Questions to ask about a tariff</h2>
<ol>
<li>What are the cheap and peak rates, the hours they apply, and the daily standing charge?</li>
<li>Is it static or dynamic? If dynamic, what is the highest price I could pay?</li>
<li>Do I need a smart meter, and is a battery allowed to charge during the cheap window?</li>
<li>How long is the contract, and is there an exit fee?</li>
<li>What would my other electricity use cost at the peak or day rate?</li>
</ol>
''',
 [_CA_TARIFF, _SEGB, _SEGB2, _OFGEM_CAP, _OFGEM_PR, _EST_SMART, _EST_RES])

_ea_page("bat", "home-battery-smart-export-guarantee.html",
 "The Smart Export Guarantee and Home Batteries Explained",
 "What the Smart Export Guarantee (SEG) pays for, who can claim it, and how a home battery changes things: solar exports, grid-charged batteries and what to ask your supplier.",
 "Smart Export Guarantee",
 ("The Smart Export Guarantee and home batteries", "The Smart Export Guarantee pays you for some electricity you send to the grid. A battery changes what you export and what counts. Here is how it works. Information, not financial advice."),
 [("what","What the SEG is"),("who","Who can claim"),("solar","Solar with a battery"),("grid","Grid-charged batteries"),("example","Worked example"),("ask","Questions to ask")],
'''
<div class="card" style="background:#e7f2ef;border-left:5px solid #d9822b;margin:0 0 1.2rem"><p><strong>Key points</strong></p><ul>
<li>The SEG pays small-scale generators, such as solar panels, for the low-carbon electricity they export. A battery is not itself an eligible generator.</li>
<li>Suppliers set their own SEG rates and contract terms, but the rate must be above zero.</li>
<li>Under the SEG, a supplier is not obliged to pay for electricity you bought from the grid, stored and exported. Check before you assume it.</li>
</ul></div>

<h2 id="what">What the Smart Export Guarantee is</h2>
<p>Ofgem says the SEG launched on 1 January 2020. It requires some electricity suppliers, called SEG licensees, to pay small-scale generators for low-carbon electricity they export back to the National Grid, as long as certain criteria are met. Payments are calculated from export meter readings.</p>
<p>SEG licensees decide the rate, contract length and other terms. Any SEG tariff must always be above zero. Ofgem does not set a rate, and this page does not quote one, because rates differ between suppliers and change over time. The <a href="calculators/home-battery.html">home battery payback calculator</a> does not include SEG payments.</p>

<h2 id="who">Who can claim</h2>
<ul>
<li>Ofgem lists five eligible technology types: solar photovoltaic (solar PV), wind, micro combined heat and power, hydro and anaerobic digestion. The installation must be in Great Britain, meet the eligibility criteria and be within the capacity limits (up to 5MW, or 50kW for micro-CHP).</li>
<li>Ofgem’s guidance for licensees says suppliers with at least 150,000 domestic electricity customers must offer at least one SEG tariff. Smaller suppliers can offer one voluntarily.</li>
<li>You can apply to any SEG licensee. It does not have to be your current electricity supplier.</li>
</ul>

<h2 id="solar">If you have solar panels and a battery</h2>
<p>With solar, a battery changes what happens to your spare electricity. Without a battery, surplus solar is exported and paid for under a SEG tariff. With a battery, you can store some of that surplus and use it later, which avoids buying from the grid at your normal rate.</p>
<p>Ofgem has published separate guidance for adding electricity storage to installations that receive SEG payments (version 6.2, 23 May 2025). The central question is whether the export meter can tell electricity generated by the eligible installation apart from electricity from other sources. Check with your SEG supplier how it would treat your set-up before you buy.</p>
<p>The Energy Saving Trust’s research (12 August 2026) found that, strictly on savings, adding a battery to solar panels may not be enough to justify the cost, because current export tariff rates are good enough that selling surplus can be almost as valuable as storing it. It adds that a battery can protect you if export rates fall, because stored electricity then becomes more valuable to use yourself.</p>

<h2 id="grid">Batteries charged from the grid</h2>
<p>This is where the SEG is often misunderstood. Ofgem’s guidance for licensees describes “green export” as electricity generated by the eligible installation, and says a licensee is only obliged to make SEG payments for that. Where the export meter also records electricity from another source that it cannot separate out (“brown export”), the licensee is not obliged to pay, although it can choose to. One of Ofgem’s examples is co-located storage that is charged from a source other than the eligible generator.</p>
<p>So the idea of buying cheap electricity overnight and exporting it for a payment is not something a supplier has to pay for under the SEG. Some suppliers may offer separate schemes with their own terms. That is a supplier’s commercial choice, so treat any such income as uncertain until it is confirmed in writing. This is why the calculator’s battery saving comes from using the stored energy in your own home, not from exporting it.</p>

<h2 id="example">Worked example (hypothetical)</h2>
<div class="card"><p><strong>Assumptions – an example, not a quote.</strong> A home with solar panels and a battery. Spare solar is either exported at an example SEG rate of 15p/kWh (made up) or stored and used later. Stored energy is used in the evening instead of buying electricity at 32.69p/kWh (Ofgem’s average unit rate for 1 January to 31 March 2027). Round-trip battery efficiency 90%.</p></div>
<ul>
<li>Export 1 kWh: 15p.</li>
<li>Store 1 kWh: you get back 0.90 kWh, which avoids buying 0.90 kWh at 32.69p, so about 29.4p.</li>
<li>Difference: about 14.4p per kWh stored, or about £144 for every 1,000 kWh moved into the battery.</li>
</ul>
<p>On these made-up numbers the advantage is real but modest. It shrinks as the export rate rises. If the example export rate were 30p/kWh, storing would give about 29.4p against 30p exported, a small loss of about 0.6p per kWh. It also depends on how many kWh you actually shift in a year, which depends on your solar output and your evening use.</p>

<h2 id="ask">Questions to ask a supplier or installer</h2>
<ol>
<li>Is this a SEG tariff, and what are the rate, the contract length and how often the rate can change?</li>
<li>Will my battery and metering let the supplier separate solar export from any grid-charged electricity, and will it pay on that basis? Ask for this in writing.</li>
<li>Can the battery be set to charge only from solar, and does that suit my tariff plan?</li>
<li>Is the export meter I need included in the quote?</li>
</ol>
''',
 [_ea_src("Ofgem – Smart Export Guarantee (SEG)", "https://www.ofgem.gov.uk/environmental-and-social-schemes/smart-export-guarantee-seg"),
  _ea_src("Ofgem – SEG: Generators", "https://www.ofgem.gov.uk/environmental-and-social-schemes/smart-export-guarantee-seg/smart-export-guarantee-seg-generators"),
  _ea_src("Ofgem – Guidance for SEG Licensees (PDF)", "https://www.ofgem.gov.uk/sites/default/files/docs/2019/12/guidance_for_seg_licensees_final.pdf", "(December 2019; see sections 1.2, 3.7 and 4.26 to 4.29)"),
  _ea_src("Ofgem – Guidance for generators: co-location of electricity storage and hydrogen production under the RO, FIT, REGO and SEG (version 6.2)", "https://www.ofgem.gov.uk/guidance/guidance-generators-co-location-electricity-storage-and-hydrogen-production-under-ro-fit-rego-and-seg-version-62", "(23 May 2025; we read the summary page only, which says it includes an appendix on batteries with SEG installations, not the full PDF)"),
  _EST_RES, _EST_BATT, _OFGEM_CAP])

_ea_page("bat", "home-battery-cost-vat-quotes.html",
 "Home Battery Costs, VAT and What to Check in a Quote",
 "What UK home batteries typically cost, how VAT on installation is due to change on 1 April 2027, and a checklist of questions to ask when comparing installer quotes.",
 "Costs, VAT and quotes",
 ("Home battery costs, VAT and what to check in a quote", "A battery’s price is the biggest number in any payback sum. Here is what the Energy Saving Trust says about costs, how VAT on installation is due to change, and what to ask about in a quote. Information, not financial advice."),
 [("cost","What batteries cost"),("vat","VAT"),("example","Worked example"),("quote","Checking a quote"),("calc","Using the calculator")],
'''
<div class="card" style="background:#e7f2ef;border-left:5px solid #d9822b;margin:0 0 1.2rem"><p><strong>Key points</strong></p><ul>
<li>The Energy Saving Trust says costs range from £1,500 to £10,000, with a 5 kWh system around £4,600.</li>
<li>Installing a battery in a home is currently zero-rated for VAT. From 1 April 2027 the installation reverts to the reduced rate of 5%, according to HMRC’s VAT notice.</li>
<li>Compare quotes on the same basis: usable capacity, warranty, what is included and whether VAT is in the price.</li>
</ul></div>

<h2 id="cost">What home batteries cost</h2>
<p>The Energy Saving Trust says the cost depends on the type and size of battery. It can range from £1,500 to £10,000, and a 5 kWh battery system is around £4,600. It describes a typical home system as around 10 kWh, and the typical lifespan as about 10 to 12 years. It adds that installing a battery at the same time as solar panels, or a heat pump, may reduce the cost, because the installers are already on site.</p>
<p>The Energy Saving Trust recommends getting at least three quotes from installers certified with MCS (the Microgeneration Certification Scheme).</p>
<p>The calculator’s starting cost, £4,600 for a 5 kWh battery, is this Energy Saving Trust figure, and its capacity starts at 5 kWh to match. It is a guide, not a price you will necessarily be quoted, so use a real quote instead.</p>

<h2 id="vat">VAT on batteries</h2>
<p>HMRC’s VAT Notice 708/6 explains the temporary zero rate for energy-saving materials:</p>
<ul>
<li>From 1 February 2024, electrical storage batteries installed in residential accommodation qualify for the zero rate. The notice lists a battery fitted with solar panels or other microgeneration, a standalone battery that stores electricity from the grid, and one that stores both.</li>
<li>The zero rate applies to supplies up to 31 March 2027. From 1 April 2027, supplies of installations of energy-saving materials revert to the reduced rate of 5%.</li>
</ul>
<p>The rule is about the <em>installation</em>, so ask the installer how VAT is shown on the quote and on which date the work is supplied.</p>

<h2 id="example">Worked example (hypothetical)</h2>
<div class="card"><p><strong>Assumptions – an example, not a quote.</strong> Suppose an installer quotes £4,600 for a 5 kWh battery with no VAT charged, because the zero rate applies. If the same work were supplied on or after 1 April 2027 at 5% VAT, it would add 5% of £4,600, which is £230, making £4,830.</p></div>
<p>Put those into the <a href="calculators/home-battery.html">calculator</a> with its other starting values (5 kWh, 90% efficiency, 7p cheap rate, 32.69p rate avoided, 300 cycles, 12 years, 2% capacity loss). The first-year saving stays at about £374, but simple payback moves from about 12.3 years to about 12.9 years, and the net result over 12 years from about −£578 to about −£808. This only illustrates how a price change moves the result.</p>
<p>Capacity for the money matters too. Suppose, purely as a made-up illustration, that £4,600 bought a 10 kWh battery instead. With the other starting values unchanged, the calculator gives a first-year saving of about £747 and a payback with fading capacity of about 6.5 years. The Energy Saving Trust describes a typical home system as around 10 kWh but says prices run from £1,500 to £10,000, so ask each installer for the usable capacity and the total price, then work out the cost per kWh.</p>

<h2 id="quote">Checking a quote</h2>
<p>Quotes can look similar and differ a lot. These are questions to ask, not a ranking of any product or installer:</p>
<ol>
<li><strong>Capacity:</strong> is the figure usable capacity or total capacity? The Energy Saving Trust notes the system stops discharging at a set level, maybe around 20%.</li>
<li><strong>Efficiency:</strong> what round-trip efficiency is stated?</li>
<li><strong>Warranty:</strong> how long does it last, and does it guarantee a minimum capacity after a number of years or cycles? The Energy Saving Trust says to ask about warranties and guarantees for both the battery and the installation.</li>
<li><strong>What is included:</strong> installation, inverter, any wiring changes, and any smart or tariff integration.</li>
<li><strong>VAT:</strong> is it included, at what rate, and what changes after 31 March 2027?</li>
<li><strong>Tariff and solar:</strong> is the battery compatible with the tariff you plan to use, and does it affect solar export payments? See <a href="home-battery-time-of-use-tariffs.html">time-of-use tariffs and home batteries</a> and <a href="home-battery-smart-export-guarantee.html">the Smart Export Guarantee and home batteries</a>.</li>
<li><strong>Installer:</strong> is the installer MCS-certified, and can they show how they calculated your saving?</li>
</ol>
<p class="hint">Installers may also have a commercial interest in selling a battery. That is a reason to ask how their savings figure was worked out, and to compare it with the <a href="home-battery-payback-explained.html">sums in the payback article</a>.</p>

<h2 id="calc">Using the calculator with a real quote</h2>
<p>In the <a href="calculators/home-battery.html">home battery payback calculator</a>, replace the installed cost, usable capacity, efficiency and lifespan with the figures from your quote, and the cheap and peak rates with those of the tariff you would use. The result is only as reliable as those inputs.</p>
''',
 [_EST_BATT,
  _ea_src("GOV.UK / HMRC – Energy-saving materials and heating equipment (VAT Notice 708/6)", "https://www.gov.uk/guidance/vat-on-energy-saving-materials-and-heating-equipment-notice-7086", "(sections 1.1, 2.1 and 2.19, as shown on 26 November 2026)"),
  _EST_RES])

# ================================================================ SET 2: EV CHARGING
_ea_page("ev", "ev-charging-cost-per-mile-explained.html",
 "EV Charging Cost per Mile: How It's Worked Out (UK)",
 "How to work out what an electric car costs per mile: price per kWh divided by miles per kWh, why charging losses matter, and a worked example with stated assumptions.",
 "Cost per mile explained",
 ("EV charging cost per mile, explained", "Cost per mile is one division. The hard part is choosing the right two numbers. Here is how it works, and why your real figure may differ from a calculator’s. Information, not financial advice."),
 [("sum","The sum"),("example","Worked example"),("losses","Charging losses"),("real","Real-world efficiency"),("year","From a mile to a year")],
'''
<div class="card" style="background:#e7f2ef;border-left:5px solid #d9822b;margin:0 0 1.2rem"><p><strong>Key points</strong></p><ul>
<li>Cost per mile = price per kWh ÷ miles per kWh.</li>
<li>The price you pay depends heavily on where and when you charge, so there is no single figure for an electric car.</li>
<li>Some of the electricity you pay for is lost as heat, so the miles per kWh on the car’s display can flatter the cost.</li>
</ul></div>

<h2 id="sum">The sum</h2>
<p>An electric car’s efficiency is measured in miles per kWh. The price of electricity is in pence per kWh. Divide one by the other:</p>
<p><strong>Cost per mile = price per kWh ÷ miles per kWh.</strong></p>
<p>That is the formula in the <a href="calculators/ev-charging.html">EV charging cost calculator</a>. It uses separate prices for home and public charging, because they can be very different (see <a href="ev-home-vs-public-charging-cost.html">home vs public charging</a>), and a share of charging done at home to blend them.</p>

<h2 id="example">Worked example (hypothetical)</h2>
<div class="card"><p><strong>Assumptions – an example, not a quote.</strong> A car that does 3.5 miles per kWh (the calculator’s example value). Prices per kWh: 7p (a made-up overnight rate), 32.69p (Ofgem’s average electricity unit rate for 1 January to 31 March 2027, Direct Debit), 26.32p (Ofgem’s average for the previous quarter, 1 October to 31 December 2026), and 54p and 82p (Zapmap’s October 2026 average pay-as-you-go prices at public chargers, 3 to 49kW and 50kW and above).</p></div>
<div class="table-scroll"><table><caption class="sr">Cost per mile at different prices per kWh, at 3.5 miles per kWh</caption><thead><tr><th scope="col">Price per kWh</th><th scope="col">What it stands for</th><th scope="col">Cost per mile</th></tr></thead><tbody>
<tr><td>7p</td><td>Example cheap overnight rate (made up)</td><td>2.0p</td></tr>
<tr><td>32.69p</td><td>Ofgem average, Jan–Mar 2027</td><td>9.3p</td></tr>
<tr><td>26.32p</td><td>Ofgem average, previous quarter (Oct–Dec 2026)</td><td>7.5p</td></tr>
<tr><td>54p</td><td>Zapmap average, public 3–49kW, Oct 2026</td><td>15.4p</td></tr>
<tr><td>82p</td><td>Zapmap average, public 50kW and above, Oct 2026</td><td>23.4p</td></tr>
</tbody></table></div>
<p>So the same car can cost around 2p a mile or over 20p a mile, depending on the price. Zapmap’s own conversion for the two public averages is about 16p and 24p per mile. It uses an “average efficiency EV”, and the page does not say what figure it assumes. The Ofgem rates are national averages for default tariffs, and your own rate depends on your region, tariff and how you pay.</p>

<h2 id="losses">Charging losses</h2>
<p>You are billed for the electricity that passes through the meter, but not all of it ends up in the battery. E.ON Next’s guide says energy is lost as heat in the car’s on-board charger and in cables, and in warming the battery. It says you might lose 10% on a warm day with a high-quality wallbox but 25% on a chilly night with a 3-pin plug. It also says the car’s display usually shows only the energy stored in the battery, so a smart meter or charger app will show a higher figure. This is one supplier’s guide, so treat the range as indicative.</p>
<div class="card"><p><strong>Example with an assumed 10% loss (hypothetical).</strong> If the car does 3.5 miles per kWh stored in the battery, but 10% of the electricity from the meter is lost on the way, you get 3.5 × 0.90 = 3.15 miles per kWh drawn from the meter. At 32.69p that is about 10.4p per mile instead of 9.3p, and at 7p it is about 2.2p instead of 2.0p. The calculator ignores losses, so real home charging costs are a little higher than it shows.</p></div>

<h2 id="real">Real-world efficiency</h2>
<p>Miles per kWh is not fixed. Which? found in its 2022 tests that the real range of the electric cars it tested was on average 18% lower than the official figure. It says weather, driving style and speed all matter, and that you get fewer miles on a motorway than around town. That article is from 2022, so it is older than our other sources, but the point still holds: use the efficiency you actually get. Many cars show an average on the dashboard, and over a few weeks that is a better input than a brochure figure.</p>

<h2 id="year">From a mile to a year</h2>
<p>To get a yearly cost, multiply by your mileage. In the example above, 8,000 miles a year at 3.5 miles per kWh needs about 2,286 kWh of electricity a year (8,000 ÷ 3.5). At 32.69p that is about £747, and at the previous quarter’s 26.32p it would have been about £602. The <a href="calculators/ev-charging.html">calculator</a> does this sum for a mix of home and public charging. For what it leaves out, see <a href="ev-charging-calculator-limits.html">what the charging calculator leaves out</a>.</p>
''',
 [_OFGEM_CAP, _OFGEM_PR, _ZAPMAP, _EON, _WHICH])

_ea_page("ev", "ev-home-vs-public-charging-cost.html",
 "Home vs Public EV Charging: Cost per Mile Compared",
 "Why charging an electric car at home usually costs less per mile than at public chargers: Ofgem and Zapmap prices, VAT differences and a worked yearly example.",
 "Home vs public charging",
 ("Home vs public EV charging: cost per mile", "Home charging and public charging are priced very differently. Here are the published prices, the VAT difference and what that does to a year’s charging bill. Information, not financial advice."),
 [("prices","Published prices"),("vat","VAT"),("example","Worked example"),("mix","Why the mix matters"),("check","Checking your own prices")],
'''
<div class="card" style="background:#e7f2ef;border-left:5px solid #d9822b;margin:0 0 1.2rem"><p><strong>Key points</strong></p><ul>
<li>Zapmap’s October 2026 averages for pay-as-you-go public charging are 54p/kWh (3 to 49kW) and 82p/kWh (50kW and above).</li>
<li>Ofgem’s average home electricity rate on default tariffs is 32.69p/kWh for 1 January to 31 March 2027, up from 26.32p/kWh in the previous quarter.</li>
<li>Electricity from public charge points is standard-rated for VAT (20%), while domestic electricity currently has a temporary zero rate until 30 June 2027.</li>
</ul></div>

<h2 id="prices">Published prices</h2>
<p><strong>Public charging.</strong> Zapmap’s monthly index gives weighted average pay-as-you-go prices. For October 2026 they are <strong>54p/kWh</strong> for standard and standard-plus chargers (3kW up to 49kW) and <strong>82p/kWh</strong> for rapid and ultra-rapid chargers (50kW and above). Zapmap says the pay-as-you-go price is what drivers can pay without a membership or special deal, so many drivers pay less, and prices differ a lot between networks. It says its rapid and ultra-rapid average is up about 8% on a year earlier, and about 2% for the slower chargers.</p>
<p><strong>Home charging.</strong> On a default tariff, Ofgem’s average Direct Debit electricity unit rate is <strong>32.69p/kWh</strong> for 1 January to 31 March 2027 (it was 26.32p/kWh for 1 October to 31 December 2026), plus a standing charge of 54.77p a day. These are averages for England, Scotland and Wales. A time-of-use or EV tariff can have a much lower rate in some hours (see <a href="ev-tariffs-off-peak-charging.html">EV tariffs and off-peak charging</a>). The Energy Saving Trust (page last updated March 2025) says charging at home is currently the cheapest way to charge, and that charging at home at off-peak times can save more.</p>

<h2 id="vat">The VAT difference</h2>
<p>HMRC says electricity for domestic use is usually subject to the reduced rate of VAT, and a temporary zero rate has applied in Great Britain from 1 October 2026 (Ofgem says to 30 June 2027). Legislation that took effect on 1 November 2026 confirms that electricity supplied through publicly accessible charge points is not supplied for domestic use for VAT, so it is standard rated (20%). Electricity used to charge an EV as part of the general supply to your home may continue to qualify for the relief. HMRC’s brief is addressed to charge point operators. We have not checked whether each network’s advertised price includes VAT, so check this on the price you see.</p>

<h2 id="example">Worked example (hypothetical)</h2>
<div class="card"><p><strong>Assumptions – an example, not a quote.</strong> 8,000 miles a year at 3.5 miles per kWh (about 2,286 kWh a year). Charging losses are ignored, as in the calculator. The home price is Ofgem’s default-tariff average, and the public price is Zapmap’s 82p/kWh rapid average. Your own mix and prices will differ.</p></div>
<div class="table-scroll"><table><caption class="sr">Yearly charging cost under different mixes, hypothetical</caption><thead><tr><th scope="col">Where the car is charged</th><th scope="col">Home price</th><th scope="col">Cost per mile (blended)</th><th scope="col">Yearly cost</th></tr></thead><tbody>
<tr><td>All at home</td><td>32.69p</td><td>9.3p</td><td>£747</td></tr>
<tr><td>90% home, 10% public rapid</td><td>32.69p</td><td>10.8p</td><td>£860</td></tr>
<tr><td>80% home, 20% public rapid</td><td>32.69p</td><td>12.2p</td><td>£973</td></tr>
<tr><td>All at public 3–49kW (54p)</td><td>n/a</td><td>15.4p</td><td>£1,234</td></tr>
<tr><td>All at public rapid (82p)</td><td>n/a</td><td>23.4p</td><td>£1,874</td></tr>
</tbody></table></div>
<p>Moving from 90% to 80% home charging adds about £113 a year in this example, and doing everything on rapid chargers costs about three times as much as doing everything at home on a default tariff. The table comes from the <a href="calculators/ev-charging.html">EV charging cost calculator’s</a> own formula.</p>

<h2 id="mix">Why the mix matters</h2>
<p>The share of charging you do at home matters at least as much as the exact prices. A driver who can charge at home most of the time has a very different cost profile from one who relies on public rapid chargers. Zapmap says typical EV drivers use the most expensive rapid chargers for only a fraction of the time.</p>
<p>If you cannot charge at home, the type of public charger matters: Zapmap’s two averages differ by 28p per kWh. Zapmap also notes that some operators offer promotional deals that make the price paid lower than the pay-as-you-go average.</p>

<h2 id="check">Checking your own prices</h2>
<ol>
<li>Home: look at the unit rate on your tariff, and whether you have a cheaper rate at night.</li>
<li>Public: check the price per kWh in the charger network’s app before you plug in, and whether any extra fees apply.</li>
<li>Put both into the <a href="calculators/ev-charging.html">calculator</a>, with your own split between home and public.</li>
<li>Remember the calculator ignores charging losses (<a href="ev-charging-cost-per-mile-explained.html">see how cost per mile is worked out</a>).</li>
</ol>
''',
 [_ZAPMAP, _OFGEM_CAP, _OFGEM_PR, _HMRC_RCB, _EST_SMART])

_ea_page("ev", "ev-tariffs-off-peak-charging.html",
 "EV Tariffs and Off-Peak Charging Explained (UK)",
 "How EV and time-of-use electricity tariffs work, how smart charge points set off-peak hours, and a worked example of when a night rate saves money overall.",
 "EV tariffs and off-peak",
 ("EV tariffs and off-peak charging", "An EV tariff makes electricity cheaper at certain hours, usually overnight. Whether it saves you money depends on the rest of your home’s use too. Here is how to think it through. Information, not financial advice."),
 [("what","What an EV tariff is"),("home","Smart charge points"),("example","Worked example"),("types","Whole-home or EV-only"),("ask","Questions to ask")],
'''
<div class="card" style="background:#e7f2ef;border-left:5px solid #d9822b;margin:0 0 1.2rem"><p><strong>Key points</strong></p><ul>
<li>An EV tariff is a type of time-of-use tariff with a cheaper rate, usually overnight, so you can charge a car at a lower price.</li>
<li>Most EV tariffs apply to all the electricity used in the home, so the rest of your use at the higher rate matters.</li>
<li>Home charge points sold for private use in Great Britain must have off-peak default charging hours that you can change.</li>
</ul></div>

<h2 id="what">What an EV tariff is</h2>
<p>Citizens Advice says you can charge an electric vehicle on a standard variable or fixed tariff, but a time-of-use tariff usually works out cheaper. If you charge at night, a static time-of-use tariff, such as an EV tariff, might be cheaper. If you charge at different times of day, a dynamic tariff might save you money. Smart Energy GB says most EV charging tariffs are static, with fixed rates at fixed times, and that most flexible tariffs need a smart meter.</p>
<p>On a standard tariff, electricity costs the same at any time of day, so charging at night is not cheaper. See <a href="home-battery-time-of-use-tariffs.html">time-of-use tariffs and home batteries</a> for more on static and dynamic tariffs, which apply to batteries and cars alike.</p>

<h2 id="home">Smart charge points and off-peak hours</h2>
<p>You do not need a smart charge point to charge off-peak. The Energy Saving Trust says you can plug in manually during low-cost periods, or set a charging time through the car’s dashboard controls.</p>
<p>If you do have a smart one, GOV.UK says charge points sold for private (home or workplace) use in Great Britain must have smart functionality, under regulations in force since 30 June 2022. They must also include pre-set off-peak default charging hours, which the owner can accept, remove or change. The regulations define peak hours as 8am to 11am and 4pm to 10pm on weekdays, and the default hours must be outside those times. The owner must also be able to override the schedule. A charger’s default hours are not the same as your tariff’s cheap hours, so check that the two match.</p>
<p>The Energy Saving Trust says smart charging at home overnight could save up to 20% on charging costs, depending on your tariff, mileage and charging patterns. It gives the typical cost of installing a home charge point as around £800 to £1,200 (page last updated March 2025), and says you will typically need a smart meter and an EV or time-of-use tariff to make the most of it.</p>

<h2 id="example">Worked example (hypothetical)</h2>
<div class="card"><p><strong>Assumptions – an example, not a quote.</strong> A household that charges an EV with about 2,286 kWh a year (8,000 miles at 3.5 miles per kWh) and uses a further 2,500 kWh a year on everything else, all at the day rate. <em>Standard tariff:</em> 32.69p/kWh at any time (Ofgem’s average for 1 January to 31 March 2027). <em>EV tariff:</em> a made-up 7p/kWh at night and 40p/kWh by day. All EV charging happens at night. Standing charges and charging losses are ignored.</p></div>
<ul>
<li>Saving on EV charging: 2,286 kWh × (32.69p − 7p) = about <strong>£587</strong>.</li>
<li>Extra cost on the rest of the home: 2,500 kWh × (40p − 32.69p) = about <strong>£183</strong>.</li>
<li>Net: about <strong>£404 a year</strong> better off on this made-up tariff, before any difference in standing charge.</li>
</ul>
<p>If the day rate were 45p rather than 40p, the extra cost on the rest of the home would be about £308 a year, and the net saving would fall to about £279. If it were 30p, the rest of the home would cost less than on the standard tariff and the net saving would be larger. And if less of the car’s charging happened at night than assumed, the saving would be smaller still. The sum to remember is: <strong>kWh moved to the cheap rate × the saving per kWh, minus the extra cost on all your other use.</strong> The <a href="calculators/ev-charging.html">EV charging cost calculator</a> lets you try different home rates.</p>

<h2 id="types">Whole-home or EV-only</h2>
<p>The Energy Saving Trust says that most of these tariffs apply to all the electricity used in the home. Some suppliers offer tariffs where the cheaper rate is for EV charging only and is separate from other use (it calls these type-of-use tariffs). The two work differently, so ask which one you are being offered. Whole-home tariffs also reward shifting other use, such as running a washing machine or dishwasher on a timer, as Smart Energy GB suggests.</p>
<p>Smart Energy GB also says that you choose your tariff. When you get a smart meter the price you pay does not change unless you switch. Not every household suits a time-of-use tariff.</p>

<h2 id="ask">Questions to ask about an EV tariff</h2>
<ol>
<li>What are the night and day rates, the cheap hours, and the standing charge?</li>
<li>Does the cheap rate apply to the whole home or only to the car?</li>
<li>Is it a static or dynamic tariff? If dynamic, what is the highest price I could pay?</li>
<li>Do I need a smart meter and a smart charge point, and will the charger’s hours match the tariff’s?</li>
<li>How long is the contract, and what is the exit fee?</li>
</ol>
''',
 [_CA_TARIFF, _SEGB, _SEGB2, _EST_SMART, _OFGEM_CAP,
  _ea_src("GOV.UK – Regulations: electric vehicle smart charge points", "https://www.gov.uk/guidance/regulations-electric-vehicle-smart-charge-points", "(last updated 23 April 2024)"),
  _ea_src("legislation.gov.uk – The Electric Vehicles (Smart Charge Points) Regulations 2021, regulation 10", "https://www.legislation.gov.uk/uksi/2021/1467/regulation/10/made", "(as made; the page notes it is the original version)")])

_ea_page("ev", "ev-charging-calculator-limits.html",
 "What an EV Charging Cost Calculator Leaves Out (UK)",
 "What a charging cost calculator ignores: charging losses, cold weather and speed, a home charge point, vehicle tax and the proposed pay-per-mile eVED, with sources.",
 "What the calculator leaves out",
 ("What an EV charging calculator leaves out", "A charging calculator answers one question: what does the electricity cost? It does not answer what the car costs to run. Here is what is missing, with sources. Information, not financial advice."),
 [("losses","Charging losses"),("eff","Efficiency changes"),("charger","A home charge point"),("tax","Vehicle tax"),("eved","Pay-per-mile eVED"),("check","A fuller checklist")],
'''
<div class="card" style="background:#e7f2ef;border-left:5px solid #d9822b;margin:0 0 1.2rem"><p><strong>Key points</strong></p><ul>
<li>The <a href="calculators/ev-charging.html">EV charging cost calculator</a> multiplies units by prices. It ignores losses, changes in efficiency and everything that is not electricity.</li>
<li>Electric cars pay vehicle tax, and a pay-per-mile charge has been announced for April 2028 (not law yet).</li>
<li>Insurance, servicing and depreciation are not in the calculator either.</li>
</ul></div>

<h2 id="losses">Charging losses</h2>
<p>The calculator’s own note says charging losses are ignored. E.ON Next’s guide says some of the electricity you are billed for is lost as heat and in battery warming, from around 10% to 25% depending on the charger, cable and weather. The <a href="ev-charging-cost-per-mile-explained.html">cost per mile article</a> shows how an assumed 10% loss changes the sum, from 9.3p to about 10.4p per mile at 32.69p/kWh. That is one supplier’s guide, so treat the range as a rough guide.</p>

<h2 id="eff">Efficiency changes with conditions</h2>
<p>The calculator uses one figure for miles per kWh. Which? says in its 2022 article that weather, driving style and speed all affect an electric car’s range, and that you get fewer miles on a motorway than around town. Its tests found real range averaged 18% below the official figure. A lower miles-per-kWh figure raises the cost per mile directly, since the sum is price ÷ miles per kWh. For example, 3.0 miles per kWh instead of 3.5 at 32.69p gives about 10.9p per mile rather than 9.3p. E.ON Next also notes that in cold weather more energy goes into warming the battery.</p>

<h2 id="charger">A home charge point</h2>
<p>If you do not already have one, the Energy Saving Trust gives the typical cost of installing a home charge point as around £800 to £1,200 (page last updated 25 March 2025). It also says you need off-street parking, and typically a smart meter and a suitable tariff to get the most from it. The calculator’s home rate does not include this one-off cost.</p>

<h2 id="tax">Vehicle tax (VED)</h2>
<p>According to GOV.UK’s rate tables, a zero-emission car pays £10 when it is first registered. From the second payment onward, electric cars pay the standard rate of £200 for 12 months. An electric car with a list price of more than £50,000 can pay an extra £440 a year for five years (from the second time it is taxed). Check GOV.UK’s table for which registration dates and prices are affected.</p>

<h2 id="eved">Pay-per-mile eVED (announced, not law yet)</h2>
<p>GOV.UK’s page on Electric Vehicle Excise Duty (updated 28 October 2026) says that from 1 April 2028 a mileage-based charge will apply to electric cars: 3p per mile for battery-electric cars and 1.5p per mile for plug-in hybrids, rising with CPI from 2029 to 2030. It says primary legislation will be introduced, so it is not law until Parliament passes it, and the details could change.</p>
<div class="card"><p><strong>Illustration, if it goes ahead as announced (hypothetical use).</strong> At 3p per mile, 8,000 miles a year would be 8,000 × 3p = £240 a year. That is 3p on top of the electricity cost per mile in the <a href="ev-charging-cost-per-mile-explained.html">cost per mile article</a>, for example 9.3p per mile at 32.69p/kWh and 3.5 miles per kWh. The eVED would be separate from, and in addition to, the cost of the electricity.</p></div>

<h2 id="check">A fuller running-cost checklist</h2>
<ul>
<li>Electricity: your tariff and your mix of home and public charging (see <a href="ev-home-vs-public-charging-cost.html">home vs public</a> and <a href="ev-tariffs-off-peak-charging.html">EV tariffs</a>).</li>
<li>The efficiency you actually get, in the seasons and on the roads you actually drive.</li>
<li>A home charge point, if you need one.</li>
<li>Vehicle tax, and from April 2028 the announced pay-per-mile charge.</li>
<li>Insurance, servicing, tyres, depreciation and finance. The calculator includes none of these, and we give no figures here because they vary widely.</li>
</ul>
<p>Our <a href="electric-cars.html">Electric cars guide</a> covers company car tax, battery health and the wider rules.</p>
''',
 [_EON, _WHICH, _EST_SMART,
  _ea_src("GOV.UK – Vehicle tax rates: cars registered on or after 1 April 2017", "https://www.gov.uk/vehicle-tax-rate-tables", "(as shown on 26 November 2026)"),
  _ea_src("GOV.UK / HM Treasury – Electric Vehicle Excise Duty (eVED)", "https://www.gov.uk/government/publications/electric-vehicle-excise-duty-eved/electric-vehicle-excise-duty-eved", "(updated 28 October 2026)")])

if not _EA_LIVE:
    for _f in ENERGY_FILES:
        PREVIEW_PAGES.add(_f)
        pages[_f] = pages[_f].replace('<link rel="icon"', '<meta name="robots" content="noindex"><link rel="icon"', 1)
print("energy articles:", len(ENERGY_FILES), "pages", "(LIVE)" if _EA_LIVE else "(preview, noindex)")
