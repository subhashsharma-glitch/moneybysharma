# PREVIEW: postcode checker + network address checkers + Ofcom-accredited comparison sites on broadband-phones.html.
# Data: data/broadband/pc/<DISTRICT>.json + data/broadband/meta.json, built by scripts/build_broadband_data.py from
# Ofcom Connected Nations open data (OGL). Mobile coverage: Ofcom publishes it only down to local authority level, so the
# page looks up the council area for the postcode with postcodes.io (open data, no key) and shows that area's figures.
import json as _j29
_M29 = _j29.load(open("data/broadband/meta.json"))["release"]
_c = _M29["checked"]; import datetime as _d29; _cd = _d29.date.fromisoformat(_c); _CHK = f"{_cd.day} {_cd:%B %Y}"
def _x(url, text): return f'<a href="{url}">{text}</a>'   # external links get new-tab + hint from the SEO pass (pages23)
_NETS = [
 ("Openreach", "https://www.openreach.com/fibre-checker", "The UK's biggest network. Its lines are used by BT, EE, Sky, TalkTalk, Plusnet, Vodafone, NOW, Zen and many others, so this check covers most providers."),
 ("BT Wholesale checker", "https://www.broadbandchecker.btwholesale.com/", "A more detailed look at the speeds the Openreach network can give a specific line."),
 ("Virgin Media", "https://www.virginmedia.com/broadband/postcode-checker", "Its own cable and full fibre network, used mainly by Virgin Media itself."),
 ("CityFibre", "https://cityfibre.com/", "A full fibre network in many towns and cities. You buy through providers that use it, such as Vodafone, TalkTalk or Zen."),
 ("Hyperoptic", "https://www.hyperoptic.com/", "Full fibre, mostly in blocks of flats and new-build developments."),
 ("Community Fibre", "https://communityfibre.co.uk/", "Full fibre in London."),
 ("Gigaclear", "https://www.gigaclear.com/", "Full fibre in rural areas, mainly in the south and middle of England."),
 ("YouFibre", "https://www.youfibre.com/check-availability/", "Full fibre provider in parts of England and Scotland."),
 ("Trooli", "https://www.trooli.com/check-availability", "Full fibre in parts of southern and eastern England."),
 ("KCOM", "https://www.kcom.com/home/", "The network for Hull and parts of East Yorkshire, where Openreach does not run the local lines."),
]
_PCW = [
 ("broadbandchoices.co.uk", "https://www.broadbandchoices.co.uk/", "broadband, mobile, landline and pay-TV"),
 ("MoneySuperMarket", "https://www.moneysupermarket.com/broadband/", "broadband, mobile, landline and pay-TV"),
 ("Broadband Genie", "https://www.broadbandgenie.co.uk/", "broadband, landline and pay-TV"),
 ("broadbanddeals.co.uk", "https://broadbanddeals.co.uk/", "broadband, landline and pay-TV"),
 ("CompareDial", "https://www.comparedial.com/", "mobile"),
 ("Green Smartphones", "https://greensmartphones.com/", "mobile"),
 ("SIM Only Finder", "https://www.simonlyfinder.co.uk/", "mobile"),
]
_nets = "".join(f'<li><strong>{_x(u, n)}</strong> – {d}</li>' for n, u, d in _NETS)
_pcw = "".join(f'<li>{_x(u, n)} – {d}</li>' for n, u, d in _PCW)
BB_PC = f'''<style>
.pc-box .pc-row{{display:flex;gap:.6rem;flex-wrap:wrap;align-items:flex-end}}.pc-box .pc-row>div{{flex:1 1 12rem}}
.pc-box input{{text-transform:uppercase}}.pc-out{{margin-top:1rem}}.pc-out h3{{font-family:var(--serif);color:var(--teal);margin:.2rem 0 .6rem}}
.pc-tbl{{width:100%;border-collapse:collapse;font-size:.95rem}}.pc-tbl th,.pc-tbl td{{text-align:left;padding:.45rem .4rem;border-top:1px solid var(--line);vertical-align:top}}
.pc-tbl td.n{{text-align:right;font-weight:700;color:var(--teal);white-space:nowrap;font-variant-numeric:tabular-nums}}
.pc-bar{{display:flex;height:.7rem;border-radius:99px;overflow:hidden;background:var(--line);margin:.3rem 0 .2rem}}.pc-bar i{{display:block;height:100%}}
.pc-key{{display:flex;flex-wrap:wrap;gap:.2rem .9rem;font-size:.82rem;color:var(--muted);list-style:none;padding:0;margin:.3rem 0 0}}.pc-key b{{display:inline-block;width:.7rem;height:.7rem;border-radius:2px;margin-right:.3rem;vertical-align:-1px}}
.pc-err{{color:#9b2c1d;font-weight:600}}.pc-src{{font-size:.85rem;color:var(--muted);margin:.7rem 0 0}}
.pc-grid{{display:grid;gap:1rem;grid-template-columns:minmax(0,1fr)}}.pc-grid>div{{min-width:0}}.pc-tbl th{{white-space:normal;font-weight:600;background:none;color:inherit}}@media(min-width:760px){{.pc-grid{{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}}}}
</style>
<h2 id="postcode">Check your postcode</h2>
<p>Enter a postcode to see what Ofcom's latest data says about broadband speeds there, and mobile coverage in the local council area. This shows what the networks report for the postcode as a whole. Your own address may differ, so check with the networks below before you sign up.</p>
<form id="pc-form" class="calc pc-box" novalidate><div class="pc-row"><div><label for="pc-in">Postcode</label>
<input id="pc-in" name="postcode" autocomplete="postal-code" inputmode="text" maxlength="9" placeholder="e.g. YO1 7HH" aria-describedby="pc-help"></div>
<button class="btn" type="submit">Check</button></div>
<p id="pc-help" class="pc-src">Broadband figures load from this site. To find your council area for the mobile figures, your postcode is sent to <a href="https://postcodes.io/">postcodes.io</a> (an open postcode lookup). Nothing is stored.</p>
<div id="pc-out" class="pc-out" aria-live="polite"></div></form>
<p class="src">Source: {_x(_M29["url"], "Ofcom Connected Nations")} ({_M29["name"]}), data dated {_M29["dataDate"]}, checked {_CHK}. Contains Ofcom data licensed under the Open Government Licence. Ofcom only publishes mobile coverage down to council level, and not for each operator, so for coverage from EE, O2, Three or Vodafone at your address use {_x("https://checker.ofcom.org.uk/", "Ofcom's own checker")}.</p>
<script>(function(){{
var f=document.getElementById("pc-form"),inp=document.getElementById("pc-in"),out=document.getElementById("pc-out"),meta=null;
var OC="https:/"+"/checker.ofcom.org.uk/";var K={_j29.dumps(_j29.load(open("data/broadband/meta.json"))["cols"])};
var BANDS=[["b0","Under 2 Mbit/s","#9b2c1d"],["b2","2 to 5","#c9592b"],["b5","5 to 10","#d9822b"],["b10","10 to 30","#e8b04f"],["b30","30 to 300","#5a9b8f"],["b300","300 or more","#0f4c45"]];
function esc(s){{return String(s).replace(/[&<>"]/g,function(c){{return{{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}}[c]}})}}
function pct(v){{return v==null?"no data":(Math.round(v*10)/10)+"%"}}
function norm(s){{s=s.toUpperCase().replace(/[^A-Z0-9]/g,"");if(!/^[A-Z]{{1,2}}[0-9][A-Z0-9]?[0-9][A-Z]{{2}}$/.test(s))return null;return [s.slice(0,-3),s.slice(-3)]}}
function getMeta(){{return meta?Promise.resolve(meta):fetch("data/broadband/meta.json").then(function(r){{return r.json()}}).then(function(m){{meta=m;return m}})}}
function row(l,v){{return "<tr><th scope=\\"row\\">"+l+"</th><td class=\\"n\\">"+pct(v)+"</td></tr>"}}
function fixed(pc,d){{
 var sum=BANDS.reduce(function(a,b){{return a+(d[b[0]]||0)}},0);
 if(sum===0) return "<h3>Broadband in "+esc(pc)+"</h3><p>Ofcom's data has no speed figures for this postcode. It may have no homes or businesses, or be new. Try a nearby postcode or the network checkers below.</p>";
 var top=d.gig>0?"Gigabit-capable (1,000 Mbit/s or more)":d.b300>0?"300 Mbit/s or more":d.b30>0?"30 to 300 Mbit/s":d.b10>0?"10 to 30 Mbit/s":d.b5>0?"5 to 10 Mbit/s":d.b2>0?"2 to 5 Mbit/s":"Under 2 Mbit/s";
 var bar=BANDS.map(function(b){{return d[b[0]]?"<i style=\\"width:"+d[b[0]]+"%;background:"+b[2]+"\\" title=\\""+b[1]+": "+d[b[0]]+"%\\"></i>":""}}).join("");
 var key=BANDS.map(function(b){{return "<li><b style=\\"background:"+b[2]+"\\"></b>"+b[1]+": "+pct(d[b[0]]||0)+"</li>"}}).join("");
 return "<h3>Broadband in "+esc(pc)+"</h3><p><strong>Fastest speed available to at least some premises:</strong> "+top+".</p>"+
  "<"+"table class=\\"pc-tbl\\"><caption class=\\"sr\\">Share of premises in "+esc(pc)+" that can get each type of broadband</caption><tbody>"+
  row("Superfast (30 Mbit/s or more)",d.sf)+row("Ultrafast (300 Mbit/s or more)",d.uf)+row("Gigabit-capable (full fibre or upgraded cable)",d.gig)+
  row("Fibre to the cabinet or better (NGA)",d.nga)+row("Decent broadband (10 Mbit/s) from fixed wireless",d.fwa)+
  row("Can't get decent broadband (10 Mbit/s) from a fixed line or fixed wireless",d.nodec)+"</tbody></"+"table>"+
  "<p class=\\"pc-src\\" style=\\"margin-top:.9rem\\"><strong>Top download speed available, by share of premises</strong></p><div class=\\"pc-bar\\" aria-hidden=\\"true\\">"+bar+"</div><ul class=\\"pc-key\\">"+key+"</ul>";
}}
function mobile(m){{
 if(!m) return "<h3>Mobile coverage</h3><p>We couldn't match this postcode to a council area in Ofcom's mobile data. Use <a href=\\""+OC+"\\" target=\\"_blank\\" rel=\\"noopener noreferrer\\">Ofcom's checker<span class=\\"sr sr-nt\\"> (opens in new tab)</span></a> instead.</p>";
 return "<h3>Mobile coverage in "+esc(m.n)+"</h3><p class=\\"pc-src\\" style=\\"margin-top:0\\">Council-area figures (premises), not just your postcode.</p><"+"table class=\\"pc-tbl\\"><caption class=\\"sr\\">Mobile coverage in "+esc(m.n)+"</caption><tbody>"+
  row("4G indoors, from at least one operator",m.in4g_any)+row("4G indoors, from all four operators",m.in4g_all)+
  row("4G outdoors, from all four operators",m.out4g_all)+row("5G outdoors, from at least one operator",m.out5g_any)+"</tbody></"+"table>";
}}
f.addEventListener("submit",function(e){{e.preventDefault();var p=norm(inp.value);
 if(!p){{out.innerHTML="<p class=\\"pc-err\\">Please enter a full UK postcode, like YO1 7HH.</p>";inp.setAttribute("aria-invalid","true");inp.focus();return}}
 inp.removeAttribute("aria-invalid");var pc=p[0]+" "+p[1];inp.value=pc;out.innerHTML="<p>Checking "+esc(pc)+"…</p>";
 var mob=fetch("https://api.postcodes.io/postcodes/"+encodeURIComponent(p[0]+p[1])).then(function(r){{return r.ok?r.json():null}}).catch(function(){{return null}});
 Promise.all([getMeta(),fetch("data/broadband/pc/"+p[0]+".json").then(function(r){{return r.ok?r.json():null}}).catch(function(){{return null}}),mob]).then(function(a){{
  var m=a[0],sh=a[1],pj=a[2],i=sh&&sh.p[p[1]];
  if(i==null){{out.innerHTML="<p class=\\"pc-err\\">"+esc(pc)+" isn't in Ofcom's January 2026 postcode data. Check it's typed correctly. New postcodes may not be included yet.</p>";return}}
  var d={{}};K.forEach(function(k,j){{d[k]=sh.v[i][j]}});
  var la=pj&&pj.result&&pj.result.codes?m.mobileLaua[pj.result.codes.admin_district]:null;
  out.innerHTML="<div class=\\"pc-grid\\"><div>"+fixed(pc,d)+"</div><div>"+mobile(la)+"</div></div>";
 }}).catch(function(){{out.innerHTML="<p class=\\"pc-err\\">Sorry, the data didn't load. Please try again.</p>"}});
}});
var q=(location.search.match(/[?&]pc=([^&]+)/)||[])[1];if(q){{inp.value=decodeURIComponent(q).replace(/\\+/g," ");f.requestSubmit?f.requestSubmit():f.dispatchEvent(new Event("submit"))}}
}})();</script>
<h3 id="bb-networks">Check your address with each network</h3>
<p>Most providers sell over one of a few networks. Each network's own checker shows whether your exact address can connect. Not every network covers every area. This list is in no particular order and is not a recommendation.</p>
<ul>{_nets}</ul>
<h3 id="bb-compare">Ofcom-accredited price comparison sites</h3>
<p>Ofcom audits some comparison sites to check that their prices are accurate, up to date and clearly shown. These are the sites on {_x("https://www.ofcom.org.uk/phones-and-broadband/saving-money/price-comparison", "Ofcom's accredited list")} (last updated by Ofcom on 17 July 2026). Comparison sites usually earn commission from providers. MoneySharma has no link with any of them.</p>
<ul>{_pcw}</ul>
<p class="src">Network and comparison links checked {_CHK}.</p>
'''
BB_PC = BB_PC.replace("MoneySharma has", "MoneyBySharma has")
_k = '<h2 id="digital">'
assert pages["broadband-phones.html"].count(_k) == 1, "broadband page marker not found"
pages["broadband-phones.html"] = pages["broadband-phones.html"].replace(_k, BB_PC + _k)
