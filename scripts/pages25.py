# pages25.py – installable web app (PWA). Exec'd by build.py AFTER the search index (so offline.html stays out of search)
# and before pages are written. Adds manifest / iOS / service-worker tags to every page, builds offline.html (noindex,
# not in the sitemap) and writes manifest.webmanifest + sw.js. The SW cache name is a hash of the precached shell, so it
# changes automatically whenever the CSS, JS, icons or offline page change; HTML is network-first, so a data-only rebuild
# (e.g. the 4-hourly paper-trades refresh) leaves sw.js byte-identical and needs no version bump.
import hashlib as _hl, json as _js
PWA_HEAD = ('<link rel="manifest" href="/manifest.webmanifest">'
  '<link rel="apple-touch-icon" href="/assets/icons/apple-touch-icon.png">'
  '<meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes">'
  '<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">'
  '<meta name="apple-mobile-web-app-title" content="MoneyBySharma">'
  '<script>if("serviceWorker"in navigator)addEventListener("load",function(){navigator.serviceWorker.register("/sw.js").catch(function(){})})</script>')
pages["offline.html"] = page("offline.html", "You're offline – MoneyBySharma", "You're offline. Pages you've opened before still work.",
  ph("Offline", "You're offline", "") + W('''
<div class="card" style="margin-top:1.5rem"><p>This page isn't saved on your device yet, and there's no internet connection right now.</p>
<p>Pages you've already opened on MoneyBySharma should still work. Try one of these, or reconnect and <a href="javascript:location.reload()">try again</a>:</p>
<p><a class="btn" href="/">Home</a> <a class="btn ghost" href="/savings.html">Savings</a> <a class="btn ghost" href="/budget-2026.html">Budget 2026</a></p></div>
<p class="hint">Information, not financial advice. Figures may have changed since you last opened a page, so check again when you're back online.</p>'''))
pages["offline.html"] = pages["offline.html"].replace('<link rel="canonical" href="https://moneybysharma.co.uk/offline.html">\n', '').replace('<link rel="icon"', '<meta name="robots" content="noindex"><link rel="icon"', 1)
pages["tools.html"] = pages["tools.html"].replace('<p class="hint" style="margin-top:1rem">Garmin Fitness Insights',
  '<p class="hint" id="add-to-home" style="margin-top:1rem"><strong>Tip: add MoneyBySharma to your home screen.</strong> On Android (Chrome), open the ⋮ menu and choose <em>Add to home screen</em> or <em>Install app</em>. On iPhone or iPad (Safari), tap Share, then <em>Add to Home Screen</em>. It opens like an app, and pages you have read stay available offline.</p>\n<p class="hint" style="margin-top:1rem">Garmin Fitness Insights', 1)
assert 'id="add-to-home"' in pages["tools.html"]
for _f in pages: pages[_f] = pages[_f].replace('<link rel="icon"', PWA_HEAD + '<link rel="icon"', 1)
MANIFEST = {"name": "MoneyBySharma", "short_name": "MoneyBySharma", "description": "Plain-English UK money guides and calculators.",
  "id": "/", "start_url": "/", "scope": "/", "display": "standalone", "theme_color": "#0f4c45", "background_color": "#0f4c45", "lang": "en-GB",
  "icons": [{"src": "/assets/icons/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
            {"src": "/assets/icons/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
            {"src": "/assets/icons/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}
open("manifest.webmanifest", "w").write(_js.dumps(MANIFEST, indent=1, ensure_ascii=False) + "\n")
SHELL = ["/offline.html", "/assets/style.css", "/assets/main.js", "/assets/search.js", "/assets/favicon.svg",
         "/assets/icons/icon-192.png", "/assets/icons/apple-touch-icon.png", "/manifest.webmanifest"]
_h = _hl.sha256(pages["offline.html"].encode() + PWA_HEAD.encode())
for _p in SHELL[1:]: _h.update(open(_p.lstrip("/"), "rb").read())
SW_VERSION = "mbs-" + _h.hexdigest()[:10]
open("sw.js", "w").write(open("scripts/sw_template.js").read().replace("__VERSION__", SW_VERSION).replace("__SHELL__", _js.dumps(SHELL)))
print("pwa: sw cache", SW_VERSION)
