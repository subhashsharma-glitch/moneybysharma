"""Build assets/search-index.json from the generated pages (no external services).
Entry format: [url, title, page name, type, text]   type: 0 page, 1 section, 2 jargon term, 3 file
Also gives every <h2> in <main> an id (if it has none) so sections can be linked to."""
import html, json, re
from html.parser import HTMLParser
SKIP_PAGES = {"404.html", "search.html", "budget-2026.html"}  # budget-2026: preview, kept out of search
SEC_CAP, PAGE_CAP = 600, 700
def clean(s): return re.sub(r"\s+", " ", html.unescape(s)).strip()
def slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", clean(re.sub(r"<[^>]+>", "", s)).lower()).strip("-")
    return s[:50] or "section"
class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.in_main = False; self.skip = 0; self.h = None; self.buf = []
        self.h1 = ""; self.secs = []; self.cur = None; self.page_h = []
    def handle_starttag(self, tag, a):
        a = dict(a)
        if tag == "main": self.in_main = True
        if not self.in_main: return
        if tag in ("script", "style", "svg"): self.skip += 1
        if tag in ("h1", "h2", "h3"): self.h = (tag, a.get("id")); self.buf = []
    def handle_endtag(self, tag):
        if tag == "main": self.in_main = False
        if not self.in_main: return
        if tag in ("script", "style", "svg"): self.skip = max(0, self.skip - 1)
        if tag in ("h1", "h2", "h3") and self.h and self.h[0] == tag:
            t = clean("".join(self.buf)); kind, hid = self.h; self.h = None
            if kind == "h1": self.h1 = t
            elif kind == "h2":
                self.cur = {"t": t, "id": hid, "text": [], "h3": []}; self.secs.append(self.cur); self.page_h.append(t)
            elif kind == "h3":
                self.page_h.append(t)
                if self.cur: self.cur["h3"].append(t)
            self.buf = []
    def handle_data(self, d):
        if not self.in_main or self.skip: return
        if self.h: self.buf.append(d); return
        if self.cur is not None: self.cur["text"].append(d)
        else: self.lead = getattr(self, "lead", "") + " " + d
def build_search(pages, extra=(), out="assets/search-index.json"):
    entries = []; names = {}
    for fn, h in pages.items():
        if fn in SKIP_PAGES: continue
        # give h2s ids so sections are linkable
        m = re.search(r"<main.*?</main>", h, re.S)
        if m:
            seen = set(re.findall(r'id="([^"]+)"', h))
            def fix(mm):
                tag = mm.group(0)
                if " id=" in tag: return tag
                inner = mm.group(2); i = base = "s-" + slug(inner); n = 2
                while i in seen: i = f"{base}-{n}"; n += 1
                seen.add(i); return f'<h2 id="{i}"{mm.group(1)}>{inner}</h2>'
            new = re.sub(r"<h2([^>]*)>(.*?)</h2>", fix, m.group(0), flags=re.S)
            h = h.replace(m.group(0), new); pages[fn] = h
        p = P(); p.feed(h)
        title = re.search(r"<title>(.*?)</title>", h, re.S).group(1)
        name = clean(re.sub(r" – MoneyBySharma$", "", title)); names[fn] = name
        desc = re.search(r'<meta name="description" content="(.*?)">', h).group(1)
        url = "" if fn == "index.html" else fn
        entries.append([url, p.h1 or name, name, 0, clean(desc + " " + " ".join(p.page_h))[:PAGE_CAP * 2]])
        if fn == "jargon.html":
            for mm in re.finditer(r'<dt id="(t-\d+)"[^>]*>(.*?)</dt><dd>(.*?)</dd>', h, re.S):
                entries.append([f"jargon.html#{mm.group(1)}", clean(re.sub(r"<[^>]+>", "", mm.group(2))), "Jargon buster", 2, clean(re.sub(r"<[^>]+>", "", mm.group(3)))])
            continue
        for s in p.secs:
            txt = clean(" ".join(s["text"]))
            if len(txt) < 40 and not s["h3"]: continue
            body = clean(" ".join(s["h3"]) + " " + txt)[:SEC_CAP]
            entries.append([f"{url}#{s['id']}" if s["id"] else url, s["t"], name, 1, body])
    for e in extra: entries.append(list(e))
    data = json.dumps({"e": entries}, ensure_ascii=False, separators=(",", ":"))
    open(out, "w").write(data)
    return entries, len(data.encode())
