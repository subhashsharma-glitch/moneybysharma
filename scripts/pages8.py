# Broadband & phones page (exec'd from build.py)
DCHK = "13 October 2026"  # links and deals on this page checked on this date
S.update({
 "ofchk": ("Ofcom – Broadband and mobile coverage checker", "https://checker.ofcom.org.uk/"),
 "orchk": ("Openreach – Fibre checker", "https://www.openreach.com/fibre-checker"),
 "btwchk": ("BT Wholesale – Broadband availability checker", "https://www.broadbandchecker.btwholesale.com/"),
 "pstn": ("Openreach – Switching off the PSTN (31 January 2027)", "https://www.openreach.com/big-switch-off"),
 "pstngov": ("GOV.UK – UK transition from analogue to digital landlines", "https://www.gov.uk/guidance/uk-transition-from-analogue-to-digital-landlines"),
 "pstnor": ("Openreach – PSTN closure safeguards; 31 January 2027 deadline unchanged", "https://www.openreach.com/news/openreach-to-protect-broadband--connections-as-pstn-closure---approaches/"),
 "ofprice": ("Ofcom – Telecoms price rises: what are your rights?", "https://www.ofcom.org.uk/phones-and-broadband/saving-money/telecoms-price-rises-what-are-your-rights"),
 "ofprice25": ("Ofcom – Price rises must be shown in pounds and pence (17 Jan 2025)", "https://www.ofcom.org.uk/phones-and-broadband/bills-and-charges/protecting-consumers-from-uncertain-and-volatile-inflation"),
 "ofsocial": ("Ofcom – Social tariffs: cheaper broadband and phone packages", "https://www.ofcom.org.uk/phones-and-broadband/saving-money/social-tariffs"),
 "ots": ("Ofcom – Simpler and quicker broadband switching is here (One Touch Switch, 12 Sep 2024)", "https://www.ofcom.org.uk/phones-and-broadband/switching-provider/simpler-broadband-switching-is-here"),
 "ofcomp": ("Ofcom – Automatic compensation: what you need to know (rates from 1 April 2026)", "https://www.ofcom.org.uk/phones-and-broadband/service-quality/automatic-compensation-need-know"),
 "ofecn": ("Ofcom – Companies must tell customers about their best deals (end-of-contract notifications)", "https://www.ofcom.org.uk/phones-and-broadband/service-quality/companies-must-tell-customers-about-their-best-deals"),
 "ofmob": ("Ofcom – Switching mobile phone provider (Text to Switch)", "https://www.ofcom.org.uk/phones-and-broadband/switching-provider/switching-mobile-phone-provider"),
 "oflock": ("Ofcom – Fair treatment and easier switching statement (locked handset ban from December 2021)", "https://www.ofcom.org.uk/siteassets/resources/documents/consultations/category-1-10-weeks/184485-proposals-to-implement-the-new-european-electronic-communications-code/associated-documents/secondary-documents/statement-eecc-revised-proposals.pdf?v=325380"),
 "ofroam": ("Ofcom – Mobile roaming: strengthening customer protections (rules from 1 October 2024)", "https://www.ofcom.org.uk/phones-and-broadband/bills-and-charges/mobile-roaming-customer-protections"),
 "ofroamt": ("Ofcom – Travelling abroad? Check for roaming charges", "https://www.ofcom.org.uk/phones-and-broadband/saving-money/travelling-abroad-check-for-roaming-charges"),
})
BB = [("BT","https://www.bt.com/broadband"),("Community Fibre","https://communityfibre.co.uk/"),("Cuckoo","https://cuckoo.co/"),("EE","https://ee.co.uk/broadband"),
 ("Hyperoptic","https://www.hyperoptic.com/"),("KCOM (Hull area)","https://www.kcom.com/home/packages/"),("NOW","https://www.nowtv.com/broadband"),("Plusnet","https://www.plus.net/broadband/"),
 ("Sky","https://www.sky.com/broadband"),("TalkTalk","https://www.talktalk.co.uk/broadband"),("Three","https://www.three.co.uk/broadband"),("Utility Warehouse","https://uw.co.uk/broadband"),
 ("Virgin Media","https://www.virginmedia.com/broadband"),("Vodafone","https://www.vodafone.co.uk/broadband"),("YouFibre","https://www.youfibre.com/"),("Zen","https://www.zen.co.uk/broadband")]
NETS = [("EE","https://ee.co.uk/mobile","Network"),("O2","https://www.o2.co.uk/","Network"),("Three","https://www.three.co.uk/","Network"),("Vodafone","https://www.vodafone.co.uk/","Network"),
 ("Asda Mobile","https://mobile.asda.com/","MVNO"),("BT Mobile","https://www.bt.com/mobile","MVNO"),("giffgaff","https://www.giffgaff.com/","MVNO"),("iD Mobile","https://www.idmobile.co.uk/","MVNO"),
 ("Lebara","https://www.lebara.co.uk/","MVNO"),("Lyca Mobile","https://www.lycamobile.co.uk/en/","MVNO"),("Sky Mobile","https://www.sky.com/shop/mobile/","MVNO"),("SMARTY","https://smarty.co.uk/","MVNO"),
 ("Talkmobile","https://talkmobile.co.uk/","MVNO"),("Tesco Mobile","https://www.tescomobile.com/","MVNO"),("VOXI","https://www.voxi.co.uk/","MVNO")]
_bb = "".join(f'<li><a href="{u}">{n}</a></li>' for n,u in BB)
_nt = "".join(f'<tr><td><a href="{u}">{n}</a></td><td>{k}</td></tr>' for n,u,k in NETS)
BBDEALS = [("BT","Full Fibre 300","https://www.bt.com/broadband","£30.99 a month, rising to £34.99 in March 2027 and £38.99 in March 2028; 24-month contract; £0 activation fee"),
 ("Community Fibre","300 Mbps Full Fibre (London)","https://communityfibre.co.uk/","£19 a month, £22 from April 2027, £25 from April 2028; average 350 Mbps download/upload; 24-month contract, new customers; offer ends 14 Oct 2026"),
 ("Plusnet","Full Fibre","https://www.plus.net/broadband/","From £24.99 a month, £28.99 from 31 March 2027, £32.99 from 31 March 2028; £9.99 one-off activation fee"),
 ("YouFibre","You 1000","https://www.youfibre.com/","£24 a month (limited-time deal); average 900 Mbps wired upload and download; no in-contract price rises"),
 ("VOXI (mobile)","75GB SIM only","https://www.voxi.co.uk/","£12 a month, plus unlimited data for social media, music and video; offer ends 26 Nov 2026")]
_dl = "".join(f'<tr><td><a href="{u}">{n}</a></td><td>{p}</td><td>{x}</td></tr>' for n,p,u,x in BBDEALS)
pages["broadband-phones.html"] = page("broadband-phones.html","Broadband &amp; phones – MoneyBySharma",
 "UK broadband and mobile explained: connection types, what speed you need, the 2027 digital landline switchover, Ofcom price-rise and switching rules, social tariffs, compensation, an A–Z of providers and dated deals.",
 ph("Broadband &amp; phones","Broadband &amp; phones","Connection types, what speed you need, your rights on price rises and switching, and an A–Z of providers. A neutral list – we don't rate or recommend anyone."), W(f'''
<div class="cols"><div>
<div class="note" style="margin-top:1.5rem"><strong>Information only – not advice.</strong> MoneyBySharma has no affiliation with, and receives no payment or commission from, any broadband, phone or comparison company. Nothing here is a recommendation. Prices and availability depend on your address and change often, so always check the current terms with the provider.</div>
<h2 id="types">Broadband connection types</h2>
<ul>
<li><strong>ADSL (copper).</strong> Uses the old copper phone line all the way to your home. This is the slowest fixed option, and it's being phased out as the network moves to fibre.</li>
<li><strong>Fibre to the cabinet (FTTC, "superfast").</strong> Fibre runs to the street cabinet, then copper runs to your home. Speeds fall the further you are from the cabinet.</li>
<li><strong>Full fibre (FTTP).</strong> Fibre goes all the way into your home. It's the fastest and most reliable widely available option, with upload speeds often matching download speeds.</li>
<li><strong>Cable.</strong> Uses a separate coaxial cable network, mainly Virgin Media's, which is being upgraded to full fibre.</li>
<li><strong>4G/5G home broadband.</strong> A router that uses the mobile network. There's no line to install, but speeds depend on the signal where you live.</li>
<li><strong>Satellite.</strong> For places with no other option. Newer low-orbit services are much faster than older satellite broadband but need a dish and clear sky.</li>
</ul>
<h2 id="speed">Speeds explained</h2>
<p>Speeds are measured in megabits per second (Mbps). The <strong>download</strong> speed affects streaming and browsing. The <strong>upload</strong> speed affects video calls, sending files and cloud backups. Your own speed depends on your line, your Wi-Fi and how many devices are in use. A wired connection is usually faster than Wi-Fi.</p>
<h3 id="calc">What speed do I need? (rough guide)</h3>
<p>Enter the most that happens <em>at the same time</em> in your home. <strong>Assumptions (our planning figures, not official numbers):</strong> HD stream 5 Mbps, 4K stream 25 Mbps, video call 3 Mbps, online gaming 3 Mbps, plus 1 Mbps per person for browsing, messages and background updates. We then add 50% headroom for peaks and Wi-Fi losses. Big downloads (such as games) just finish faster on faster connections.</p>
<form id="sp-form" class="calc fields" style="margin:.6rem 0">
<div><label for="sp-people">People in the home</label><input id="sp-people" type="number" value="3" min="1" max="12"></div>
<div><label for="sp-hd">HD streams at once</label><input id="sp-hd" type="number" value="2" min="0" max="10"></div>
<div><label for="sp-uhd">4K streams at once</label><input id="sp-uhd" type="number" value="0" min="0" max="10"></div>
<div><label for="sp-calls">Video calls at once</label><input id="sp-calls" type="number" value="1" min="0" max="10"></div>
<div><label for="sp-games">People gaming online at once</label><input id="sp-games" type="number" value="0" min="0" max="10"></div>
<div style="grid-column:1/-1" class="results" aria-live="polite"><div class="res"><span>Peak use</span><b id="sp-base">–</b></div><div class="res"><span>With 50% headroom</span><b id="sp-need">–</b></div><div class="res"><span>Roughly</span><b id="sp-band" style="font-size:1rem">–</b></div></div>
<p class="hint" style="grid-column:1/-1">This is an illustration, not a recommendation. Real needs vary by service, device and Wi-Fi coverage. Check what's available at your address before choosing.</p></form>
<h2 id="check">Checking what's available</h2>
<p>Availability depends on your exact address. You can check it with <a href="{S["ofchk"][1]}">Ofcom's broadband and mobile checker</a>, the <a href="{S["orchk"][1]}">Openreach fibre checker</a> or the <a href="{S["btwchk"][1]}">BT Wholesale availability checker</a>. These cover networks that sell through many providers. Other full fibre networks, such as Hyperoptic, Community Fibre or YouFibre, have their own postcode checkers on their websites.</p>
{src("ofchk","orchk","btwchk")}
<h2 id="digital">The digital landline switchover</h2>
<p>The old analogue phone network (the PSTN) is being switched off. Openreach says the deadline is <strong>31 January 2027</strong> and hasn't changed. Landlines move to digital services that usually run through your broadband router.</p>
<ul>
<li><strong>Your phone will need power.</strong> A digital landline won't work in a power cut unless you have a battery backup. Tell your provider if you rely on your landline, have poor mobile signal, or are vulnerable – they should offer a battery backup.</li>
<li><strong>Telecare and alarms.</strong> Personal alarms, health monitors, burglar alarms, door entry systems and some card machines can be affected. Tell your provider and your alarm or telecare supplier before you switch. Providers offer extra support for telecare users, including free engineer visits and battery backups. Openreach's "Prove Telecare" engineers test alarms on the new line before completing the upgrade.</li>
<li><strong>No broadband?</strong> Some providers offer a dedicated landline-only service for customers without broadband.</li>
<li>After 31 January 2027, Openreach says lines that haven't been upgraded may be moved to a limited, emergency-only phone service.</li>
</ul>
{src("pstn","pstnor","pstngov")}
<h2 id="prices">Mid-contract price rises</h2>
<p>Since <strong>17 January 2025</strong>, Ofcom rules have banned new phone, broadband and pay-TV contracts from including price rises linked to inflation or set as a percentage. Any rise written into the contract must be shown <strong>in pounds and pence</strong>, prominently, before you sign, along with when it will happen.</p>
<p>If your provider raises the price when the contract doesn't say by how much, or by more than the contract allows, it must give you at least 30 days' notice. You then have 30 days to leave without paying exit fees. Contracts signed before 17 January 2025 may still have inflation-linked rises.</p>
{src("ofprice25","ofprice")}
<h2 id="social">Social tariffs</h2>
<p>Social tariffs are cheaper broadband and phone packages for people on certain benefits. Some providers call them "essential" or "basic" broadband. If you or someone in your household claims Universal Credit, you can choose any of the tariffs. All the major providers also include Pension Credit, Employment and Support Allowance, Jobseeker's Allowance and Income Support. Ofcom keeps the <a href="{S["ofsocial"][1]}">full list of social tariffs</a>.</p>
{src("ofsocial")}
<h2 id="switch">Switching broadband</h2>
<ul>
<li><strong>One Touch Switch.</strong> This launched for most customers on <strong>12 September 2024</strong>. You contact only your new provider, which arranges the switch, even between different networks. You don't pay notice-period charges beyond the switch date.</li>
<li><strong>Exit fees.</strong> Leaving during your minimum term usually means an early termination charge. The amount is set out in your contract.</li>
<li><strong>The right to leave.</strong> If your price rises in a way your contract didn't set out, you can leave without exit fees within 30 days of being told.</li>
<li><strong>Automatic compensation.</strong> Providers that have signed up to Ofcom's scheme pay you as a bill credit, without you having to ask. Rates from 1 April 2026: <strong>£10.34 a day</strong> if a reported loss of service isn't fixed after two full working days, and <strong>£32.31</strong> for a missed engineer appointment (or one cancelled with less than 24 hours' notice). There's also a daily payment if a new service starts late. Rates rise each year with inflation.</li>
<li><strong>End-of-contract notices.</strong> Your provider must tell you 10 to 40 days before your contract ends. The notice gives the end date, what you'll pay afterwards and the provider's best deals. If you're out of contract, you must get the same information once a year.</li>
</ul>
{src("ots","ofprice","ofcomp","ofecn")}
<h2 id="providers">Broadband providers A–Z</h2>
<p>Each link goes to the provider's own broadband page, checked on {DCHK}. This list isn't complete, and the order says nothing about price or quality. Many smaller full fibre networks only serve some areas.</p>
<ul style="columns:2;max-width:560px;column-gap:2rem">{_bb}</ul>
<h2 id="phones">Mobile phones</h2>
<ul>
<li><strong>SIM-only.</strong> Just the airtime: calls, texts and data. Contracts are usually monthly rolling or 12–24 months. It's often the cheapest option if you already have a phone.</li>
<li><strong>Contract (handset + airtime).</strong> Includes a phone. Most UK providers now use <em>split contracts</em>: a separate device plan (credit, which may involve a credit check) and an airtime plan. Once the device is paid off, you pay only for the airtime.</li>
<li><strong>Handset finance.</strong> You buy the phone on credit from the retailer or provider, often over 24–36 months. Check the total cost and whether interest is charged. You could also buy the phone outright and pair it with a SIM-only deal.</li>
<li><strong>Networks vs MVNOs.</strong> The UK has four mobile networks with their own masts: EE, O2, Three and Vodafone (Vodafone and Three have merged). MVNOs, such as giffgaff, Tesco Mobile or SMARTY, sell services using one of those networks. Coverage depends on which network the MVNO uses.</li>
<li><strong>Roaming in the EU.</strong> Since Brexit, free EU roaming is no longer guaranteed. Some providers include it, while others charge a daily fee or set fair-use limits. Since 1 October 2024, Ofcom rules require providers to send you a free alert when you start roaming, telling you about charges and limits. Check before you travel.</li>
<li><strong>Unlocked phones.</strong> Since December 2021, UK mobile providers have been banned from selling locked handsets, so a phone bought from them should work on other networks.</li>
<li><strong>Switching with a text.</strong> Text <strong>PAC</strong> to <strong>65075</strong> to keep your number, or <strong>STAC</strong> to <strong>75075</strong> if you don't want to keep it. The code arrives within a minute and is valid for 30 days. Give it to your new provider, which must complete the switch within one working day. You don't pay notice-period charges after the switch date.</li>
</ul>
{src("ofmob","oflock","ofroam","ofroamt")}
<h3 id="networks">Networks and MVNOs A–Z</h3>
<p>Each link was checked on {DCHK}. This list isn't complete, and the order says nothing about price or quality.</p>
<div class="table-scroll"><table><caption class="sr">Mobile networks and MVNOs</caption><thead><tr><th scope="col">Provider</th><th scope="col">Type</th></tr></thead><tbody>{_nt}</tbody></table></div>
<h2 id="deals">Deals seen on providers' own pages</h2>
<p>These figures were copied from each provider's own page on <strong>{DCHK}</strong>. They're a factual snapshot, not a recommendation. Availability, speeds and prices depend on your address and eligibility. Deals change often and many end soon, so check the provider's page and contract summary for current terms.</p>
<div class="table-scroll"><table><caption class="sr">Broadband and mobile deals seen on 12 October 2026</caption><thead><tr><th scope="col">Provider (source)</th><th scope="col">Package</th><th scope="col">Price and terms as stated by the provider</th></tr></thead><tbody>{_dl}</tbody></table></div>
<p class="hint">Checked {DCHK}. Deals we couldn't confirm on a provider's own page have been left out.</p>
<p>See also: <a href="bank-accounts.html">Bank accounts</a> · <a href="energy-providers.html">Energy providers and deals</a> · <a href="jargon.html">Jargon buster</a>.</p>
</div><aside><div class="card toc"><h3>On this page</h3><a href="#types">Connection types</a><a href="#speed">Speeds</a><a href="#calc">Speed helper</a><a href="#check">Availability</a><a href="#digital">Digital landlines</a><a href="#prices">Price rises</a><a href="#social">Social tariffs</a><a href="#switch">Switching</a><a href="#providers">Broadband A–Z</a><a href="#phones">Mobile phones</a><a href="#networks">Networks A–Z</a><a href="#deals">Deals seen</a><a href="jargon.html">Jargon buster</a></div></aside></div>'''), scripts=("calc.js","calc-ui5.js"))
