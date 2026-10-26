"""SEO head tags (Open Graph, Twitter, JSON-LD) shared by build.py and for patching built pages."""
import html, json
BASE = "https://moneybysharma.co.uk/"
IMG = BASE + "assets/og-image.png"
# X/Twitter uses the compact "summary" card with a square logo, so link previews take less of the post.
X_IMG = BASE + "assets/og-square.png"
X_ALT = "MoneyBySharma logo"
ORG = {"@context": "https://schema.org", "@type": "Organization", "@id": BASE + "#organization",
       "name": "MoneyBySharma", "url": BASE, "email": "hello@moneybysharma.co.uk",
       "logo": BASE + "assets/favicon.svg", "founder": {"@type": "Person", "name": "Subhash Sharma"}}
SITE = {"@context": "https://schema.org", "@type": "WebSite", "@id": BASE + "#website",
        "name": "MoneyBySharma", "url": BASE, "inLanguage": "en-GB",
        "description": "Plain-English UK personal-finance information: savings, ISAs, pensions, mortgages and gilts, with simple calculators.",
        "publisher": {"@id": BASE + "#organization"}}

def seo_meta(fn, title, desc):
    url = BASE + ("" if fn == "index.html" else fn)
    t, d = html.escape(html.unescape(title)), html.escape(html.unescape(desc))
    out = (f'<meta property="og:type" content="website"><meta property="og:site_name" content="MoneyBySharma">'
           f'<meta property="og:title" content="{t}"><meta property="og:description" content="{d}">'
           f'<meta property="og:url" content="{url}"><meta property="og:image" content="{IMG}">'
           f'<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:locale" content="en_GB">\n'
           f'<meta name="twitter:card" content="summary"><meta name="twitter:site" content="@moneybysharma"><meta name="twitter:creator" content="@moneybysharma"><meta name="twitter:title" content="{t}">'
           f'<meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{X_IMG}"><meta name="twitter:image:alt" content="{X_ALT}">\n')
    if fn == "index.html":
        out += '<script type="application/ld+json">' + json.dumps([SITE, ORG], ensure_ascii=False) + '</script>\n'
    return out

import re as _re
_A = _re.compile(r'<a\b([^>]*?)\bhref="(https?://[^"]+)"([^>]*)>(.*?)</a>', _re.S)
def ext_links(h):
    """Make external http(s) links open in a new tab, with an accessible hint. Returns (html, count)."""
    n = 0
    def f(m):
        nonlocal n
        pre, url, post, inner = m.groups()
        host = _re.sub(r'^https?://([^/:?#]+).*$', r'\1', url).lower()
        if host == "moneybysharma.co.uk" or host.endswith(".moneybysharma.co.uk"): return m.group(0)
        attrs = _re.sub(r'\s(rel|target)="[^"]*"', '', pre + post)
        n += 1
        return f'<a{attrs} href="{url}" target="_blank" rel="noopener noreferrer">{inner}<span class="sr sr-nt"> (opens in new tab)</span></a>'
    return _A.sub(f, h), n

def write_sitemap(files, lastmod):
    order = sorted(files, key=lambda f: (f != "index.html", f))
    urls = "".join(f'  <url><loc>{BASE}{"" if f=="index.html" else f}</loc><lastmod>{lastmod}</lastmod></url>\n' for f in order)
    open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')
    open("robots.txt", "w").write("User-agent: *\nAllow: /\n\nSitemap: " + BASE + "sitemap.xml\n")

if __name__ == "__main__":  # patch already-built pages in place
    import glob, os, re
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for p in sorted(glob.glob(os.path.join(root, "*.html"))):
        s = open(p, encoding="utf-8").read()
        if 'og:title' in s: continue
        fn = os.path.basename(p)
        title = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
        desc = re.search(r'<meta name="description" content="(.*?)">', s).group(1)
        s = re.sub(r'(<link rel="canonical" href="[^"]*">\n)', lambda m: m.group(1) + seo_meta(fn, title, desc), s, count=1)
        open(p, "w", encoding="utf-8").write(s)
        print("patched", fn)
