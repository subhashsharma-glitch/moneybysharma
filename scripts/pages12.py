# search.html – no-overlay fallback that supports ?q= (exec'd from build.py). Not indexed, not in the sitemap.
pages["search.html"] = page("search.html", "Search – MoneyBySharma", "Search MoneyBySharma guides, tools and jargon.",
 ph("Search", "Search", "Search the guides, tools, resources and jargon buster on this site. The search runs in your browser and nothing is sent anywhere."), W('''
<form id="sp-form" class="sp-form" role="search" action="search.html" method="get"><label for="sp-q">Search MoneyBySharma</label>
<input id="sp-q" name="q" type="search" autocomplete="off" spellcheck="false" placeholder="e.g. ISA, gilt, personal allowance, credit score" aria-describedby="sp-status"><button class="btn" type="submit">Search</button></form>
<p class="hint" id="sp-status" role="status" aria-live="polite">Type a word or phrase to search the site.</p>
<ul id="sp-results" class="sp-list" aria-label="Search results"></ul>
<noscript><p class="note">Search needs JavaScript. You can browse everything from the <a href="index.html">home page</a> or the <a href="jargon.html">Jargon buster</a>.</p></noscript>'''))
pages["search.html"] = pages["search.html"].replace('<link rel="icon"', '<meta name="robots" content="noindex"><link rel="icon"', 1).replace("<body>", '<body data-search="page">', 1)
