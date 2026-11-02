# Kids Corner (exec'd from build.py after the search index). Data: data/kids-corner.json
# Pages live in sub-folders (kids-corner/, kids-corner/<id>/), so relative links from page() get a ../ prefix.
import os as _kc_os, re as _kc_re
KC = json.load(open("data/kids-corner.json"))
KC_CSS = '''<style>
.kc-hero{background:var(--teal-50);border-radius:var(--radius);padding:1.2rem 1.25rem;margin:1.5rem 0;border-left:6px solid var(--accent)}
.kc-kid{text-align:center}.kc-kid .kc-av{display:inline-flex;width:64px;height:64px;border-radius:50%;background:var(--teal);color:#fff;font-family:var(--serif);font-size:2rem;font-weight:700;align-items:center;justify-content:center;border:4px solid var(--accent)}
.kc-kid h3{margin:.6rem 0 .2rem}.kc-posts{display:grid;gap:1rem;margin:1rem 0 2rem}
.kc-post .kc-meta{font-size:.85rem;color:var(--muted)}.kc-soon{border:2px dashed var(--accent);background:var(--accent-50);text-align:center}
.kc-soon h3{color:var(--teal)}
</style>'''
def _kc_fix(h, depth):
    pre = "../" * depth
    return _kc_re.sub(r'(\s(?:href|src|action)=")(?!https?:|mailto:|#|/|data:|\.\./)([^"]*)"', lambda m: f'{m.group(1)}{pre}{m.group(2)}"', h)
def _kc_post(p, kid):
    pdf = f'<p><a class="btn" href="kids-corner/{kid["id"]}/printables/{p["pdf"]}" download>{p.get("pdf_label","Download the printable (PDF)")}</a></p>' if p.get("pdf") else ""
    if p.get("book"):
        pdf = (f'<p><a class="btn" href="kids-corner/{kid["id"]}/{p["book"]["slug"]}/">📖 Read the picture book</a></p>'
               + (f'<p class="kc-meta"><a href="kids-corner/{kid["id"]}/printables/{p["pdf"]}" download>{p.get("pdf_label","Download the printable (PDF)")}</a></p>' if p.get("pdf") else ""))
    return (f'<article class="card kc-post" id="{p["date"]}-{_kc_re.sub(r"[^a-z0-9]+","-",p["title"].lower()).strip("-")}"><span class="tag">{html.escape(p.get("kind","Post"))}</span>'
            f'<h3>{html.escape(p["title"])}</h3><p class="kc-meta">{d(p["date"])}</p><p>{html.escape(p.get("summary",""))}</p>{"" if p.get("book") else p.get("body_html","")}{pdf}</article>')
KC_SOON = '<div class="card kc-soon"><span class="tag soon">Coming soon</span><h3>{n}’s first post is on its way</h3><p>Check back soon for a drawing, a story or a mini lesson from {n}.</p></div>'
def _kc_write(fn, title, desc, body, depth):
    h = page(fn, title, desc, body, head=KC_CSS)
    h = _kc_fix(h, depth)
    _kc_os.makedirs(_kc_os.path.dirname(fn), exist_ok=True)
    open(fn + "index.html", "w").write(h)
kids_cards = "".join(f'<a class="card kc-kid" href="kids-corner/{k["id"]}/"><span class="kc-av" aria-hidden="true">{k["name"][0]}</span><h3>{k["name"]}</h3><p>Age {k["age"]} · {len(k["posts"])} post{"s" if len(k["posts"])!=1 else ""}</p><span class="btn">Visit {k["name"]}’s page</span></a>' for k in KC["kids"])
_kc_write("kids-corner/", "Kids Corner – MoneyBySharma",
 "Kids Corner: a space where the Sharma kids share what's on their mind – a drawing, a story or a mini lesson to read and download.",
 ph("Kids Corner", "Kids Corner", "A space where the Sharma kids share what’s on their mind.") + W(f'''
<div class="kc-hero"><p style="margin:0">Welcome to Kids Corner! This is where Saachi, Vedaant and Arjun share whatever is on their mind. It might be a drawing, a story or a mini lesson about something they have learned. You can read every post here, and some come with a printable PDF you can download and keep.</p></div>
<h2>Meet the kids</h2><div class="grid g3">{kids_cards}</div>
<p class="hint" style="margin:1.5rem 0 2rem">Posts are written by the kids with a grown-up’s help. Printables are free to download for personal and classroom use.</p>'''), 1)
for k in KC["kids"]:
    posts = sorted(k["posts"], key=lambda p: p["date"], reverse=True)
    lst = "".join(_kc_post(p, k) for p in posts) or KC_SOON.format(n=k["name"])
    _kc_write(f'kids-corner/{k["id"]}/', f'{k["name"]}’s page – Kids Corner – MoneyBySharma',
     f"{k['name']}'s page in Kids Corner on MoneyBySharma: drawings, stories and mini lessons, with printables to download.",
     f'<div class="page-head"><div class="wrap"><div class="crumb"><a href="index.html">Home</a> › <a href="kids-corner/">Kids Corner</a> › {k["name"]}</div><h1>{k["name"]}’s page</h1><p>Age {k["age"]} · Drawings, stories and mini lessons from {k["name"]}.</p></div></div>'
     + W(f'<h2>Latest posts</h2><div class="kc-posts">{lst}</div><p style="margin-bottom:2rem"><a href="kids-corner/">← Back to Kids Corner</a></p>'), 2)
KC_URLS = ["kids-corner/"] + [f'kids-corner/{k["id"]}/' for k in KC["kids"]]

# ---------- Picture-book readers (post["book"]) ----------
BK_CSS = """<style>
.bk{max-width:900px;margin:1.2rem auto 2rem;perspective:1800px}
.bk-stage{position:relative}
.bk-pg{background:#fff;border:1px solid var(--line);border-radius:18px;box-shadow:var(--shadow);overflow:hidden;margin-bottom:1rem;transform-origin:left center;backface-visibility:hidden}
.js .bk-pg{display:none;margin:0}.js .bk-pg.on{display:block;animation:bkIn .55s cubic-bezier(.2,.7,.2,1)}
.js .bk-pg.on.back{animation-name:bkBack}
@keyframes bkIn{from{transform:rotateY(-75deg);opacity:0}to{transform:none;opacity:1}}
@keyframes bkBack{from{transform:rotateY(75deg);opacity:0;transform-origin:right center}to{transform:none;opacity:1}}
@media(prefers-reduced-motion:reduce){.js .bk-pg.on{animation:none}}
.bk-pg img{display:block;width:100%;height:auto;aspect-ratio:16/9;object-fit:cover;background:var(--teal-50)}
.bk-tx{padding:1.1rem 1.4rem 1.4rem;border-top:6px solid var(--accent)}
.bk-tx p{font-size:1.3rem;line-height:1.55;margin:.3rem 0 .7rem;color:var(--ink)}
@media(min-width:700px){.bk-tx p{font-size:1.45rem}}
.bk-cover .bk-tx{text-align:center;background:var(--teal);color:#fff;border-top-color:var(--accent)}
.bk-cover h2{color:#fff;font-size:clamp(1.9rem,6vw,3rem);margin:.2rem 0}.bk-cover .bk-by{color:#ffd6a8;font-family:var(--serif);font-style:italic;font-size:1.25rem}
.bk-end .bk-tx{text-align:center;background:var(--teal-50)}.bk-end h2{font-size:clamp(2.2rem,8vw,3.6rem);color:var(--teal);margin:.3rem 0}
.bk-nav{display:none;align-items:center;justify-content:space-between;gap:.6rem;margin-top:1rem}.js .bk-nav{display:flex}
.bk-nav .btn{min-width:6.5rem;font-size:1.05rem}.bk-nav .btn.prev{background:var(--teal);color:#fff}
.bk-dots{display:flex;flex-wrap:wrap;justify-content:center;gap:.35rem;align-items:center}
.bk-dots button{width:13px;height:13px;border-radius:50%;border:2px solid var(--teal);background:#fff;padding:0;cursor:pointer}
.bk-dots button[aria-current=true]{background:var(--accent);border-color:var(--accent);transform:scale(1.25)}
.bk-count{font-size:.9rem;color:var(--muted);text-align:center;margin:.4rem 0 0}.bk-hint{text-align:center;font-size:.85rem;color:var(--muted)}
</style>"""
BK_JS = r"""<script>(function(){document.documentElement.classList.add('js');
var P=[].slice.call(document.querySelectorAll('.bk-pg')),i=0,dots=document.querySelector('.bk-dots'),cnt=document.querySelector('.bk-count'),pv=document.querySelector('.bk-nav .prev'),nx=document.querySelector('.bk-nav .next');
P.forEach(function(_,n){var b=document.createElement('button');b.type='button';b.setAttribute('aria-label','Go to page '+(n+1));b.onclick=function(){go(n)};dots.appendChild(b)});
function go(n,first){if(n<0||n>=P.length)return;var bk=n<i;P[i].classList.remove('on','back');i=n;P[i].classList.toggle('back',bk);P[i].classList.add('on');
[].forEach.call(dots.children,function(d,k){d.setAttribute('aria-current',k===i)});cnt.textContent=(i===0?'Cover':'Page '+i+' of '+(P.length-1));
pv.disabled=i===0;nx.disabled=i===P.length-1;if(!first){history.replaceState(null,'','#p'+i);var t=document.querySelector('.bk');if(t.getBoundingClientRect().top<0)t.scrollIntoView({behavior:'smooth'})}}
pv.onclick=function(){go(i-1)};nx.onclick=function(){go(i+1)};
document.addEventListener('keydown',function(e){if(/INPUT|TEXTAREA/.test(e.target.tagName))return;if(e.key==='ArrowRight')go(i+1);if(e.key==='ArrowLeft')go(i-1)});
var sx=null,sy=0,st=document.querySelector('.bk-stage');st.addEventListener('touchstart',function(e){sx=e.touches[0].clientX;sy=e.touches[0].clientY},{passive:true});
st.addEventListener('touchend',function(e){if(sx===null)return;var dx=e.changedTouches[0].clientX-sx,dy=e.changedTouches[0].clientY-sy;if(Math.abs(dx)>50&&Math.abs(dx)>Math.abs(dy))go(dx<0?i+1:i-1);sx=null});
var h=parseInt((location.hash.match(/^#p(\d+)$/)||[])[1]||0,10);P[0].classList.add('on');go(h<P.length?h:0,true)})();</script>"""
for k in KC["kids"]:
    for p in k["posts"]:
        b = p.get("book")
        if not b: continue
        base = f'kids-corner/{k["id"]}/'
        img = lambda f, a, w=1200, h=675, lazy=True: f'<img src="{base}{f}" alt="{html.escape(a)}" width="{w}" height="{h}"{" loading=lazy" if lazy else ""}>'
        secs = [f'<section class="bk-pg bk-cover on" aria-label="Cover">{img(b["cover"], b["cover_alt"], lazy=False)}<div class="bk-tx"><h2>{html.escape(p["title"])}</h2><p class="bk-by">{html.escape(b["credit"])}</p></div></section>']
        n = len(b["pages"])
        for j, pg in enumerate(b["pages"], 1):
            end = f'<h2 style="text-align:center">{html.escape(b["end"])}</h2>' if j == n else ""
            secs.append(f'<section class="bk-pg{" bk-end" if j==n else ""}" aria-label="Page {j}">{img(pg["img"], pg["alt"], pg["w"], pg["h"])}<div class="bk-tx">' + "".join(f"<p>{html.escape(t)}</p>" for t in pg["text"]) + end + '</div></section>')
        dl = f'<p><a class="btn" href="{base}printables/{p["pdf"]}" download>⬇ Download the picture book (PDF)</a></p>' if p.get("pdf") else ""
        secs.append(f'<section class="bk-pg bk-end" aria-label="The end"><div class="bk-tx"><h2>{html.escape(b["end"])}</h2><p>Thanks for reading {html.escape(p["title"])}! Want to keep it? Download the printable picture book.</p>{dl}<p><a href="{base}">← Back to {k["name"]}’s page</a> · <a href="kids-corner/">Kids Corner</a></p></div></section>')
        body = (f'<div class="page-head"><div class="wrap"><div class="crumb"><a href="index.html">Home</a> › <a href="kids-corner/">Kids Corner</a> › <a href="{base}">{k["name"]}</a> › {html.escape(p["title"])}</div><h1>{html.escape(p["title"])}</h1><p>A picture book by {k["name"]}. Use the buttons, your arrow keys, or swipe to turn the pages.</p></div></div>'
                + W(f'<div class="bk"><div class="bk-stage" aria-live="polite">{"".join(secs)}</div><div class="bk-nav"><button class="btn prev" type="button">← Back</button><div><div class="bk-dots" role="group" aria-label="Pages"></div><p class="bk-count"></p></div><button class="btn next" type="button">Next →</button></div><p class="bk-hint">Tip: use ← → keys or swipe.</p></div>'))
        fn = f'{base}{b["slug"]}/'
        h = page(fn, f'{p["title"]} – a picture book by {k["name"]} – Kids Corner – MoneyBySharma', f'{p["title"]}: {p["summary"]}', body, head=KC_CSS + BK_CSS + BK_JS)
        h = _kc_fix(h, 3); _kc_os.makedirs(fn, exist_ok=True); open(fn + "index.html", "w").write(h)
        KC_URLS.append(fn)
