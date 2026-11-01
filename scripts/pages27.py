# homepage "This month in money" key-dates box + seasonal festive banner, exec'd from build.py after pages20.
# Data: data/key-dates.json (items with date/start/end/source/checked) and data/festive.json (festivals with start/end).
# Both are filtered at build time (no-JS fallback) and again synchronously in the browser by Europe/London date, by an inline
# script placed straight after the markup, so nothing below moves after first paint (no layout shift).
# Preview: ?festive=diwali forces a festival on; ?date=2026-11-08 pretends today is that date.
import json as _j, os as _os, datetime as _dt, html as _ht
from zoneinfo import ZoneInfo as _ZI
_KD = _j.load(open("data/key-dates.json"))["items"]
_FX = _j.load(open("data/festive.json"))["festivals"]
_TODAY = _dt.datetime.now(_ZI("Europe/London")).date().isoformat()
_ICONS = {
 "diya": '<svg class="fx-ico" viewBox="0 0 48 32" aria-hidden="true" focusable="false"><path class="fx-flame" d="M24 2c3 5 5 8 5 11a5 5 0 0 1-10 0c0-3 2-6 5-11z"/><path class="fx-bowl" d="M6 18h36c-1 7-8 12-18 12S7 25 6 18z"/></svg>',
 "star": '<svg class="fx-ico" viewBox="0 0 32 32" aria-hidden="true" focusable="false"><path class="fx-bowl" d="M16 2l4 9 10 1-7.5 6.5L25 29l-9-5.5L7 29l2.5-10.5L2 12l10-1z"/></svg>',
 "spark": '<svg class="fx-ico" viewBox="0 0 32 32" aria-hidden="true" focusable="false"><path class="fx-bowl" d="M16 1l3 12 12 3-12 3-3 12-3-12-12-3 12-3z"/></svg>',
 "moon": '<svg class="fx-ico" viewBox="0 0 32 32" aria-hidden="true" focusable="false"><path class="fx-bowl" d="M21 3a13 13 0 1 0 8 21A11 11 0 0 1 21 3z"/></svg>'}
_JS_TODAY = ('function(){var q=(location.search.match(/[?&]date=(\\d{4}-\\d\\d-\\d\\d)/)||[])[1];if(q)return q;'
             'try{return new Intl.DateTimeFormat("en-CA",{timeZone:"Europe/London",year:"numeric",month:"2-digit",day:"2-digit"}).format(new Date())}'
             'catch(e){return new Date().toISOString().slice(0,10)}}')
def _e(s): return _ht.escape(s or "", quote=True)
def _file(p):
    p = (p or "").strip().lstrip("/")
    if not p: return None
    fn = p if p.endswith(".html") else p + ".html"
    return fn if (fn in pages or _os.path.exists(fn)) else None
def _fmt(iso): d = _dt.date.fromisoformat(iso); return d.strftime("%a ") + str(d.day) + d.strftime(" %b")
# ---------- festive banner ----------
_fx_items = "".join(
  f'<div class="fx fx-{_e(f["id"])}" data-id="{_e(f["id"])}" data-s="{f["start"]}" data-e="{f["end"]}"{"" if f["start"] <= _TODAY <= f["end"] else " hidden"}>'
  f'<div class="wrap fx-in">{_ICONS.get(f.get("icon"), _ICONS["spark"])}<p><b>{_e(f["greeting"])}</b> <span>{_e(f["line"])}</span></p></div></div>'
  for f in _FX)
FX_HTML = ('<div id="fx" class="fx-wrap">' + _fx_items + '</div><script>(function(){var t=(' + _JS_TODAY + ')(),'
  'f=(location.search.match(/[?&]festive=([a-z-]+)/)||[])[1],on=0;'
  '[].forEach.call(document.querySelectorAll("#fx .fx"),function(el){var s=f?el.getAttribute("data-id")===f:(t>=el.getAttribute("data-s")&&t<=el.getAttribute("data-e"));'
  'if(s&&!on){el.hidden=false;on=1}else el.hidden=true})})();</script>')
# ---------- key dates box ----------
_rows = []
for it in sorted(_KD, key=lambda x: x["date"]):
    fn = _file(it.get("page"))
    t = _e(it["title"]); t = f'<a href="{fn}">{t}</a>' if fn else t
    note = f'<span class="kd-n">{_e(it["note"])}</span>' if it.get("note") else ""
    hid = "" if it["start"] <= _TODAY <= it["end"] else " hidden"
    _rows.append(f'<li data-s="{it["start"]}" data-e="{it["end"]}"{hid}><time datetime="{it["date"]}">{_fmt(it["date"])}</time>'
                 f'<span class="kd-t">{t}{note}</span></li>')
_checked = max(it["checked"] for it in _KD)
KD_HTML = (f'<div class="wrap"><section class="card kd" aria-labelledby="kd-h"><h2 id="kd-h">This month in money</h2>'
  f'<ul class="kd-list">{"".join(_rows)}</ul><p class="kd-empty" hidden>No key money dates in the next few weeks.</p>'
  f'<p class="kd-src">Dates from the Bank of England, Ofgem and GOV.UK, checked {_dt.date.fromisoformat(_checked).day} {_dt.date.fromisoformat(_checked):%b %Y}. They can change, so check the source before acting.</p></section></div>'
  '<script>(function(){var t=(' + _JS_TODAY + ')(),n=0,b=document.querySelector(".kd");if(!b)return;'
  '[].forEach.call(b.querySelectorAll(".kd-list li"),function(li){var s=t>=li.getAttribute("data-s")&&t<=li.getAttribute("data-e")&&n<5;li.hidden=!s;if(s)n++});'
  'b.querySelector(".kd-empty").hidden=n>0})();</script>')
_mk = '<section class="numbers"'
assert pages["index.html"].count(_mk) == 1, "home page marker for the key-dates box not found"
pages["index.html"] = pages["index.html"].replace(_mk, KD_HTML + _mk)
_mk2 = '<main id="main">'
assert pages["index.html"].count(_mk2) == 1, "home page <main> not found"
pages["index.html"] = pages["index.html"].replace(_mk2, _mk2 + FX_HTML)
print("key dates:", sum(1 for it in _KD if it["start"] <= _TODAY <= it["end"]), "showing of", len(_KD), "| festive today:", [f["id"] for f in _FX if f["start"] <= _TODAY <= f["end"]] or "none")
