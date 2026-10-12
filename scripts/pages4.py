# Energy providers and deals page (exec'd from build.py)
S.update({
 "ofsw": ("Ofgem – Switch your home energy supplier", "https://www.ofgem.gov.uk/your-energy-supply/how-manage-your-energy-supply/switch-your-home-energy-supplier"),
 "rmi": ("Ofgem – Retail market indicators (number of active domestic suppliers, March 2026)", "https://www.ofgem.gov.uk/news-and-insight/data/data-portal/retail-market-indicators"),
 "esg": ("Energy UK – Energy Switch Guarantee (Q1 2026 compliance update, 26 Jun 2026)", "https://www.energy-uk.org.uk/our-work/energy-switch-guarantee/"),
 "cacs": ("Citizens Advice – Compare domestic energy suppliers' customer service", "https://www.citizensadvice.org.uk/consumer/energy/energy-supply/get-a-better-energy-deal/compare-domestic-energy-suppliers-customer-service/"),
 "ccode": ("Ofgem – Confidence Code: code of practice for online domestic price comparison services", "https://www.ofgem.gov.uk/sites/default/files/docs/2015/03/confidence_code_-_code_of_practice_0.pdf"),
})
SUPP = [("British Gas","https://www.britishgas.co.uk/energy.html"),("Ecotricity","https://www.ecotricity.co.uk/your-green-energy/our-tariffs"),
 ("EDF","https://www.edfenergy.com/gas-and-electricity"),("E.ON Next","https://www.eonnext.com/tariffs"),("Octopus Energy","https://octopus.energy/tariffs/"),
 ("Outfox the Market","https://outfox.energy/tariffs"),("OVO","https://www.ovoenergy.com/home-energy-plans/compare-energy-tariff"),
 ("ScottishPower","https://www.scottishpower.co.uk/energy-tariffs"),("So Energy","https://www.so.energy/our-tariffs"),
 ("Utilita","https://utilita.co.uk/power-price-list"),("Utility Warehouse","https://uw.co.uk/energy")]
PCW = [("Energylinx","https://www.energylinx.co.uk/"),("MoneySupermarket","https://www.moneysupermarket.com/gas-and-electricity/"),
 ("My Utility Genius","https://www.myutilitygenius.co.uk/"),("Quotezone","https://www.quotezone.co.uk/energy"),("Simply Switch","https://www.simplyswitch.com/"),
 ("Switch Gas and Electric","https://switchgasandelectric.com/"),("The Energy Shop","https://www.theenergyshop.com/"),("Unravel It","https://www.unravelit.com/"),
 ("Uswitch","https://www.uswitch.com/gas-electricity/")]
_sl = "".join(f'<li><a href="{u}" rel="noopener">{n}</a></li>' for n,u in SUPP)
_pl = "".join(f'<li><a href="{u}" rel="noopener">{n}</a></li>' for n,u in PCW)
pages["energy-providers.html"] = page("energy-providers.html","Energy providers and deals – MoneyBySharma",
 "The current Ofgem price cap, the main UK household energy suppliers, types of energy deal explained, how switching works and accredited comparison sites.",
 ph('<a href="energy.html">Energy</a> › Providers and deals',"Energy providers and deals","Who supplies household energy, the main kinds of tariff, and how switching works. A neutral list – we don't rate or recommend anyone."), W(f'''
<div class="cols"><div>
<div class="note" style="margin-top:1.5rem"><strong>Information only – not advice.</strong> MoneyBySharma has no affiliation with, and receives no payment or commission from, any energy supplier or comparison site. Nothing here is a recommendation. Tariffs and prices change often, so always check the current terms with the supplier before you switch.</div>
<h2 id="cap">The price cap right now: 1 October to 31 December 2026</h2>
<p>Ofgem's price cap limits the unit rates and standing charges on standard variable (default) tariffs. For this period the typical dual-fuel household paying by Direct Debit pays <strong>£1,723 a year</strong>. Average Direct Debit rates are 26.32p per kWh and 54.83p a day for electricity, and 7.97p per kWh and 29.68p a day for gas. Your own rates depend on region and payment method. See our <a href="energy.html#cap">energy guide</a> for more detail.</p>
{src("cap","capnews")}
<h2 id="suppliers">Household energy suppliers</h2>
<p>Ofgem counted <strong>17 active domestic suppliers</strong> in March 2026. Below are some of the main suppliers currently trading, in alphabetical order. Each link goes to the supplier's own tariff or energy page (all links checked on {CHECKED}). The list isn't complete, and the order says nothing about price or quality.</p>
<ul class="az" style="columns:2;max-width:560px">{_sl}</ul>
<p>To see how suppliers compare on complaints and customer service, Citizens Advice publishes an independent <a href="{S["cacs"][1]}" rel="noopener">customer service comparison</a>.</p>
{src("rmi","cacs")}
<h2 id="types">Types of deal explained</h2>
<ul>
<li><strong>Standard variable tariff (SVT).</strong> This is the default deal if you've never chosen one, or your fixed deal has ended. Rates move every three months but can't go above the price cap. There are usually no exit fees.</li>
<li><strong>Fixed tariff.</strong> Unit rates and standing charges are locked for a set period, often 12 or 24 months. Your bill still rises if you use more energy. Many fixed deals charge an exit fee if you leave early.</li>
<li><strong>Tracker tariff.</strong> Prices follow the wholesale market. Depending on the deal, they change daily or monthly, usually with a ceiling set in the terms. Bills can fall or rise quickly. Tracker deals usually need a smart meter.</li>
<li><strong>EV and time-of-use tariffs.</strong> Electricity costs different amounts at different times of day, with a cheaper overnight or off-peak window. They suit households that can shift use, such as charging an electric car or a home battery overnight, and they need a smart meter. <em>Example only (not a real tariff):</em> 8p per kWh from midnight to 5am and 30p per kWh at other times.</li>
<li><strong>Export tariffs.</strong> These pay you for electricity you send back to the grid from solar panels or a battery. Under the <a href="{S["seg"][1]}" rel="noopener">Smart Export Guarantee</a>, larger suppliers must offer at least one export tariff, but rates and terms vary, and you don't have to use your import supplier.</li>
</ul>
{src("seg")}
<h2 id="switch">How switching works</h2>
<ul>
<li><strong>Speed.</strong> Ofgem rules say your switch should happen within 5 working days. If it's late, the new supplier must pay you £40 compensation automatically.</li>
<li><strong>Cooling-off.</strong> You can cancel a switch within 14 days.</li>
<li><strong>Exit fees.</strong> If you leave a fixed tariff before it ends, you may have to pay an exit fee. Check your current terms first.</li>
<li><strong>Debt.</strong> Usually you can't switch if you owe your supplier money that's been outstanding for more than 28 days. Prepayment customers can switch with debts of up to £500.</li>
<li><strong>Credit balances.</strong> Your old supplier sends a final bill and should refund any credit left on the account.</li>
<li><strong>Switched by mistake?</strong> If you're switched without agreeing to it, you're entitled to £40 compensation, and your old supplier has 21 working days to switch you back.</li>
<li><strong>Smart meters.</strong> You don't need a smart meter to switch, but tracker, EV and time-of-use deals usually require one. Take a meter reading on the day you switch, so your final bill is accurate.</li>
</ul>
<h3>The Energy Switch Guarantee</h3>
<p>This is a voluntary commitment run by Energy UK, and it still applies in 2026. Suppliers that sign up commit to:</p>
<ul><li>complete 98% of switches within 5 working days</li><li>send 90% of final bills within 6 weeks</li><li>refund 90% of credit balances within 10 working days of the final bill.</li></ul>
<p>Energy UK's update for the first quarter of 2026, published on 26 June 2026, reported that all signatories met the commitments. Check the <a href="{S["esg"][1]}" rel="noopener">Energy UK page</a> for the current list of signatories.</p>
{src("ofsw","esg")}
<h2 id="compare">Accredited comparison sites (Ofgem Confidence Code)</h2>
<p>Ofgem's voluntary Confidence Code covers household energy price comparison websites. Accredited sites have to list tariffs in price order. They must also say clearly what each tariff includes, and whether it can be bought through their site. The sites below were listed by Ofgem as accredited, in alphabetical order. Ofgem's current home-switching page no longer shows the list, so we couldn't confirm it on Ofgem's live site on {CHECKED}. Look for the Confidence Code logo on the site itself.</p>
<ul class="az" style="columns:2;max-width:560px">{_pl}</ul>
<p class="hint">Comparison sites may not show every tariff, and some earn commission from suppliers. MoneyBySharma earns nothing from any of them.</p>
{src("ccode")}
</div><aside><div class="card toc"><h3>On this page</h3><a href="#cap">Price cap now</a><a href="#suppliers">Suppliers</a><a href="#types">Types of deal</a><a href="#switch">How switching works</a><a href="#compare">Comparison sites</a><a href="energy.html">← Energy guide</a></div></aside></div>'''))
