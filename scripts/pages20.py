# Weekly topics (@moneybysharma on X), exec'd from build.py after pages19.
# Data: data/weekly-topics.json -> {"weeks": [{"week", "monday" (ISO date), "topic", "page" (site path, e.g. "/savings")}]}
# Builds weekly-topics.html and adds a compact "This week's topic" block to the home page.
# A topic whose page doesn't exist in this build shows "Page coming soon" with no link (never a 404).
# The current week is highlighted at build time (fallback without JavaScript) and again in the browser by Europe/London date.
import json as _j, os as _os, datetime as _dt, html as _ht
from zoneinfo import ZoneInfo as _ZI
WT = _j.load(open("data/weekly-topics.json"))
WT_WEEKS = sorted(WT["weeks"], key=lambda w: w["monday"])
def _wt_file(p):
    """'/how-money-works' or 'how-money-works.html' -> 'how-money-works.html' if that page exists in this build, else None."""
    p = (p or "").strip().lstrip("/").split("#")[0]
    if not p: return None
    fn = p if p.endswith(".html") or p.endswith("/") else p + ".html"
    return fn if (fn in pages or _os.path.exists(fn)) and fn != "404.html" else None
for w in WT_WEEKS: w["file"] = _wt_file(w.get("page"))
WT_SOON = [w for w in WT_WEEKS if not w["file"]]
WT_TODAY = _dt.datetime.now(_ZI("Europe/London")).date()
def _wt_cur(today):
    for w in WT_WEEKS:
        m = _dt.date.fromisoformat(w["monday"])
        if m <= today < m + _dt.timedelta(days=7): return w
    return None
WT_CUR = _wt_cur(WT_TODAY)
def _wt_mon(iso, year=True): return _dt.date.fromisoformat(iso).strftime("%-d %b %Y" if year else "%-d %b")
XSVG = '<svg class="x-ic" width="14" height="14" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>'
WT_X = f'<p class="x-invite">{XSVG}<span>Follow <a href="https://x.com/moneybysharma" target="_blank" rel="noopener">@moneybysharma on X</a> for the weekly topic, posted each Monday.</span></p>'
def _wt_link(w, cls=""):
    t = _ht.escape(w["topic"])
    return f'<a{f" class={cls}" if cls else ""} href="{w["file"]}">{t}</a>' if w["file"] else f'{t} <span class="wt-soon">Page coming soon</span>'
# browser-side data for the highlight script (only what it needs)
WT_JS_DATA = _j.dumps([{"w": w["week"], "m": w["monday"], "t": w["topic"], "f": w["file"]} for w in WT_WEEKS], ensure_ascii=False).replace("</", "<\\/")
WT_JS_FN = r'''function(){var d=new Intl.DateTimeFormat("en-CA",{timeZone:"Europe/London",year:"numeric",month:"2-digit",day:"2-digit"}).formatToParts(new Date()),o={};d.forEach(function(p){o[p.type]=p.value});var t=o.year+"-"+o.month+"-"+o.day,c=null;W.forEach(function(w){var e=new Date(w.m+"T12:00:00Z");e.setUTCDate(e.getUTCDate()+7);if(w.m<=t&&t<e.toISOString().slice(0,10))c=w});return {today:t,cur:c}}'''
def _wt_esc_js(): return "function(s){return String(s).replace(/[&<>\"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;'}[c]})}"
def _wt_now_html(w):
    if not w:
        first = WT_WEEKS[0]
        if WT_TODAY < _dt.date.fromisoformat(first["monday"]): return f'<span class="wt-k">Starting {_wt_mon(first["monday"])}</span><b class="wt-t">{_wt_link(first)}</b>'
        return '<span class="wt-k">This week</span><b class="wt-t">No topic scheduled this week. See the list of past topics below.</b>'
    return f'<span class="wt-k">This week · Week {w["week"]}, from Monday {_wt_mon(w["monday"])}</span><b class="wt-t">{_wt_link(w)}</b>'
# ---------- the page ----------
_rows = "".join(
    f'<li class="wt-row{" wt-now" if WT_CUR is w else (" wt-past" if _dt.date.fromisoformat(w["monday"]) + _dt.timedelta(days=7) <= WT_TODAY else "")}" data-mon="{w["monday"]}">'
    f'<span class="wt-n">Week {w["week"]}</span><span class="wt-d">Week starting <time datetime="{w["monday"]}">Mon {_wt_mon(w["monday"])}</time></span>'
    f'<span class="wt-topic">{_wt_link(w)}</span><span class="wt-badge" aria-hidden="{"false" if WT_CUR is w else "true"}">This week</span></li>' for w in WT_WEEKS)
WT_SCRIPT = ('<script>(function(){var W=' + WT_JS_DATA + ',r=(' + WT_JS_FN + ')(),E=' + _wt_esc_js() + ';'
 'document.querySelectorAll(".wt-row").forEach(function(li){var m=li.getAttribute("data-mon"),e=new Date(m+"T12:00:00Z");e.setUTCDate(e.getUTCDate()+7);var now=r.cur&&r.cur.m===m,past=e.toISOString().slice(0,10)<=r.today;li.classList.toggle("wt-now",!!now);li.classList.toggle("wt-past",!now&&past);var b=li.querySelector(".wt-badge");if(b)b.setAttribute("aria-hidden",now?"false":"true")});'
 'var box=document.getElementById("wt-now");if(!box)return;var c=r.cur;'
 'if(c){box.innerHTML=\'<span class="wt-k">This week · Week \'+c.w+", from Monday "+new Date(c.m+"T12:00:00Z").toLocaleDateString("en-GB",{day:"numeric",month:"short",year:"numeric",timeZone:"UTC"})+\'</span><b class="wt-t">\'+(c.f?\'<a href="\'+E(c.f)+\'">\'+E(c.t)+"</a>":E(c.t)+\' <span class="wt-soon">Page coming soon</span>\')+"</b>"}'
 'else if(r.today<W[0].m){box.innerHTML=\'<span class="wt-k">Starting \'+new Date(W[0].m+"T12:00:00Z").toLocaleDateString("en-GB",{day:"numeric",month:"short",year:"numeric",timeZone:"UTC"})+\'</span><b class="wt-t">\'+(W[0].f?\'<a href="\'+E(W[0].f)+\'">\'+E(W[0].t)+"</a>":E(W[0].t))+"</b>"}'
 'else{box.innerHTML=\'<span class="wt-k">This week</span><b class="wt-t">No topic scheduled this week. See the list of past topics below.</b>\'}})();</script>')
pages["weekly-topics.html"] = page("weekly-topics.html", "Weekly topics – MoneyBySharma",
 "The @moneybysharma weekly money topic calendar: one plain-English UK money topic each week, with a link to the guide on this site. Information only, not advice.",
 ph('Learn › Weekly topics', "Weekly topics",
    "Each week, @moneybysharma on X picks one money topic and explains it in plain English, with a link to the matching guide on this site.")
 + W(f'''<div class="card wt-hero" id="wt-now" aria-live="polite">{_wt_now_html(WT_CUR)}</div>
{WT_X}
<h2 id="calendar">Topic calendar</h2>
<p class="hint">Each week starts on the Monday shown (UK time). The current week is highlighted. Topics marked "Page coming soon" don't have a guide on this site yet.</p>
<ol class="wt-list">{_rows}</ol>
<h2 id="about-weekly-topics">About the weekly topics</h2>
<p>The topics follow a simple order: how money works, then budgeting, saving, compounding and investing, with seasonal topics where they fit (scams the week before Black Friday, credit cards before Christmas, energy bills in winter). New weeks are added to this calendar as they are planned.</p>
<p>Everything here is general information, not financial advice, and not a recommendation to buy any product. Figures on each guide link to their official sources and show when they were checked.</p>''') + WT_SCRIPT)
# ---------- compact block on the home page ----------
_home_now = (f'<span class="wt-k">This week\'s topic · Week {WT_CUR["week"]}</span><b class="wt-t">{_wt_link(WT_CUR)}</b>' if WT_CUR
  else f'<span class="wt-k">Weekly topics</span><b class="wt-t">One plain-English money topic each week.</b>')
WT_HOME = (f'<div class="wrap"><div class="card wt-home"><div id="wt-home-now">{_home_now}</div>'
 '<a class="wt-all" href="weekly-topics.html">See all weekly topics →</a></div></div>'
 '<script>(function(){var W=' + WT_JS_DATA + ',r=(' + WT_JS_FN + ')(),E=' + _wt_esc_js() + ',c=r.cur,b=document.getElementById("wt-home-now");if(!b)return;'
 'b.innerHTML=c?\'<span class="wt-k">This week\\u2019s topic · Week \'+c.w+\'</span><b class="wt-t">\'+(c.f?\'<a href="\'+E(c.f)+\'">\'+E(c.t)+"</a>":E(c.t)+\' <span class="wt-soon">Page coming soon</span>\')+"</b>":\'<span class="wt-k">Weekly topics</span><b class="wt-t">One plain-English money topic each week.</b>\'})();</script>')
_mk = '<section class="numbers"'
assert pages["index.html"].count(_mk) == 1, "home page marker for the weekly-topic block not found"
pages["index.html"] = pages["index.html"].replace(_mk, WT_HOME + _mk)
print("weekly topics:", len(WT_WEEKS), "weeks; current:", WT_CUR and WT_CUR["week"], "; coming soon:", [w["week"] for w in WT_SOON] or "none")
