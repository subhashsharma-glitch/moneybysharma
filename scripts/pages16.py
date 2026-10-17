# Deals & savings page (exec'd from build.py after pages15). Content comes from data/deals.json (entries carry their own checked
# date and official link; refreshed by scripts/update_deals.py). Information only - not advice. No affiliate links, no promo codes.
import json as _json, html as _html
DL = _json.load(open("data/deals.json"))
_today = datetime.date.today().isoformat()
SG.update({
 "unitprice": ("GOV.UK – Unit pricing: information for consumers", "https://www.gov.uk/government/publications/unit-pricing-information-for-consumers/unit-pricing-information-for-consumers"),
 "everydayfix": ("GOV.UK – PM starts roll out of 'everyday fixes' on the cost of living (9 August 2026)", "https://www.gov.uk/government/news/pm-starts-roll-out-of-everyday-fixes-on-the-cost-of-living-ending-rip-off-discounts-and-subscription-traps"),
 "cmaredlines": ("GOV.UK – Shoppers urged to call out online rip-offs as CMA unveils 'red lines' (29 March 2023)", "https://www.gov.uk/government/news/shoppers-urged-to-call-out-online-rip-offs-as-cma-unveils-red-lines"),
 "nectarterms": ("Sainsbury's – Nectar Prices terms (retailer's own terms)", "https://help.sainsburys.co.uk/help/terms-and-conditions/nectarprice"),
 "clubcardfaq": ("Tesco – Your Clubcard Prices (retailer's own help page)", "https://www.tesco.com/help/pages/clubcard-faqs/clubcard-prices/your-clubcard-prices"),
})
S.update(SG)
def _e(s): return _html.escape(s, quote=False)
def _live(e):  # hide anything whose own end date has passed
    return not (e.get("expires") and e["expires"] < _today)
def _pts(lst):
    out = []
    for p in lst:
        if isinstance(p, dict):
            if p.get("until") and p["until"] < _today: continue
            out.append(p["t"])
        else: out.append(p)
    return out
def _links(e):
    return "".join(f'<li><a href="{u}" rel="noopener">{_e(t)}</a></li>' for t, u in e["links"])
def _meta(e):
    bits = [f"Checked on {d(e['checked'])}"]
    if e.get("expires"): bits.append(f"offer ends {d(e['expires'])}")
    return f'<p class="dl-meta">{" · ".join(bits)}</p>'
def _card(e):
    linkonly = e.get("status") in ("link-only", "review")
    tag = f'<div class="dl-tags"><span class="tag">{_e(e["tag"])}</span>' + (' <span class="tag tag-muted">Link only</span>' if linkonly else "") + "</div>"
    body = f'<p>{_e(e["summary"])}</p>'
    if not linkonly:
        pts = _pts(e.get("points", []))
        if pts: body += "<ul>" + "".join(f"<li>{_e(p)}</li>" for p in pts) + "</ul>"
    else:
        body += '<p class="hint">No figures are shown for this entry: please check the official page.</p>'
    return f'<div class="card dl-card" id="{e["id"]}">{tag}<h3>{_e(e["name"])}</h3>{body}<ul class="dl-links">{_links(e)}</ul>{_meta(e)}</div>'
def _plan_card(e):
    linkonly = e.get("status") in ("link-only", "review")
    head = f'<div class="dl-tags"><span class="tag">{_e(e["tag"])}</span>' + (' <span class="tag tag-muted">Link only</span>' if linkonly else "") + "</div>"
    if linkonly: body = f'<p>{_e(e["summary"])}</p><p class="hint">No figures are shown for this entry: please check the official page.</p>'
    else:
        rows = "".join(f'<tr><th scope="row">{_e(p)}</th><td>{_e(v)}</td></tr>' for p, v in e["plans"])
        body = f'<div class="table-scroll"><table class="wrap-th dl-plans"><caption class="sr">{_e(e["name"])}: plans and published prices</caption><thead><tr><th scope="col">Plan</th><th scope="col">Published price</th></tr></thead><tbody>{rows}</tbody></table></div>'
        for o in _pts(e.get("offers", [])): body += f'<p class="dl-offer">{_e(o)}</p>'
        if e.get("note"): body += f'<p class="hint">{_e(e["note"])}</p>'
    return f'<div class="card dl-card" id="{e["id"]}">{head}<h3>{_e(e["name"])}</h3>{body}<ul class="dl-links">{_links(e)}</ul>{_meta(e)}</div>'
_groups = ""
_counts = {}
for g in DL["groups"]:
    es = [e for e in g["entries"] if _live(e)]; _counts[g["id"]] = len(es)
    cls = "grid g2" if g["kind"] == "table" else "grid g3"
    fn = _plan_card if g["kind"] == "table" else _card
    _groups += f'<h2 id="{g["id"]}">{_e(g["title"])}</h2><p>{_e(g["intro"])}</p><div class="{cls}">' + "".join(fn(e) for e in es) + "</div>"
    if g["id"] == "subscriptions":
        _groups += f'''<div class="note"><strong>Before you start a free trial or a subscription.</strong> Check the price after any trial or introductory period, the minimum term, how to cancel and whether it renews automatically. Put the end date in your calendar. GOV.UK announced on 9 August 2026 that new subscription rules come into force in January 2027, with clearer upfront information, regular reminders, an easier exit and a 14-day cooling-off period after a trial or long-term contract renews. Those rules are not in force yet, so today the service's own terms apply. See also <a href="bank-accounts.html#ways">how payments work and what protects you</a>.</div>'''
_jump = " · ".join(f'<a href="#{g["id"]}">{_e(g["title"])}</a>' for g in DL["groups"])
pages["deals.html"] = page("deals.html", "Deals and savings: supermarkets, cinema, subscriptions and high street – MoneyBySharma",
 "Where to find the retailers' own published loyalty prices, memberships, subscription prices and cinema offers across UK supermarkets, cinemas, streaming and music services and high-street chains, each with a checked date and a link to the official page.",
 ph("Deals &amp; savings", "Deals and savings on everyday shopping", "Loyalty prices, memberships and subscription prices, taken from the retailers' own pages, with the date each was checked. Information only – not advice."), W(f'''
<div class="note" style="margin-top:1.5rem"><strong>Information only – not advice.</strong> This page points to offers that retailers publish on their own websites. Offers, prices and terms change often, and some are time-limited, personalised or only for new customers. <strong>The retailer's own page is always the source of truth</strong>: check it before you buy or sign up. Every entry shows the date we last checked it. Where we couldn't read an official page, we show a link only. MoneyBySharma earns nothing from any link on this page, and we don't list promo codes.</div>
<p class="dl-jump"><strong>Jump to:</strong> {_jump} · <a href="#genuine">How to spot a genuine deal</a></p>

<h2 id="genuine">How to spot a genuine deal</h2>
<ul class="dl-tips">
<li><strong>Compare unit prices, not shelf prices.</strong> GOV.UK explains that unit prices (per kilo, litre or item) let you compare different pack sizes, and that the biggest pack is not always the best value. You can usually find the unit price beneath the shelf price or beside the item online.</li>
<li><strong>Test the “was” price.</strong> A discount is only as real as the price it is measured against. Look at what the item cost on earlier visits or in a price-history record, and compare the final price with other shops. GOV.UK said on 9 August 2026 that a consultation will launch this autumn on whether fake “was” prices, invented discounts and misleading recommended retail prices should be banned, because they are hard to tackle under current laws.</li>
<li><strong>Know the loyalty-price rules.</strong> Loyalty prices usually apply only if you scan or swipe each time you shop, or link your card to your online account. Sainsbury's terms say Nectar Prices can't be applied after the event, and “Your Nectar Prices” and Tesco's “Your Clubcard Prices” have to be unlocked each week before you shop. Check the shelf label for both the regular price and the member price.</li>
<li><strong>Watch for pressure tactics.</strong> The CMA has published “red lines” on misleading price-reduction and urgency claims online, such as countdown timers and “selling fast” messages that may not be true.</li>
<li><strong>Read the small print on free trials.</strong> Check what you pay once the trial or introductory price ends, the minimum term and whether it renews automatically (see subscriptions below).</li></ul>
{sg("unitprice","everydayfix","cmaredlines","nectarterms","clubcardfaq")}

{_groups}

<h2 id="student-links">Student discounts</h2>
<p>Student plans for music and video are listed in the subscriptions table above. For other student offers, see our <a href="students.html">students guide</a>, and always check the brand's own terms.</p>

<h2 id="about-data">About these entries</h2>
<p>Each entry is taken from the retailer's own page. We summarise what it says, in our own words, and we don't copy prices from comparison or voucher sites. Time-limited offers disappear from this page after the end date they were published with. If you spot something out of date, the retailer's page is right and ours needs updating. Illustrations of how a scheme works are not a recommendation to join it, and there is no “best” scheme: what suits you depends on where you shop and what you buy.</p>
<p class="hint">Last data update: {d(DL["updated"])}. Related: <a href="budgeting-emergency-fund.html">Budgeting and emergency funds</a> · <a href="scams-fraud.html">Scams and fraud</a> · <a href="students.html">Students</a> · <a href="jargon.html">Jargon buster</a></p>
'''))
DEALS_COUNTS = _counts
