# Daily tip, quiz and myth-or-fact on the home page. Data: data/daily-features.json.
# Inserted after "Today's key numbers" (which pages28 may have moved). Preview flag lives in the JSON.
import json as _j31, html as _ht31, re as _re31
_DF = _j31.load(open("data/daily-features.json"))
assert len(_DF.get("tips") or []) >= 30, "need about 30 tips"
assert len(_DF.get("quiz") or []) >= 20, "need about 20 quiz questions"
assert len(_DF.get("myths") or []) >= 20, "need about 20 myth-or-fact items"
for _q in _DF["quiz"]:
    assert len(_q["options"]) == 4 and _q["answer"] in range(4), _q.get("id")
for _m in _DF["myths"]:
    assert _m["verdict"] in ("myth", "fact"), _m.get("id")
_raw31 = _j31.dumps(_DF, ensure_ascii=False, separators=(",", ":"))
if "</script" in _raw31.lower():
    raise SystemExit("daily-features.json contains </script")
_DAILY_HTML = (
    '<section class="daily" id="daily" aria-labelledby="daily-h">'
    '<noscript><div class="wrap"><div class="card"><span class="tag">Money tip of the day</span>'
    "<h3>" + _ht31.escape(_DF["tips"][0]["title"]) + "</h3><p>" + _ht31.escape(_DF["tips"][0]["body"]) + "</p>"
    '<p class="hint">Turn on JavaScript to see the daily quiz and myth-or-fact card. '
    + _ht31.escape(_DF.get("disclaimer") or "Information, not financial advice.") +
    "</p></div></div></noscript>"
    '<script type="application/json" id="mbs-daily-data">' + _raw31 + "</script>"
    "</section>"
)
_h31 = pages["index.html"]
_m31 = _re31.search(r'<section class="numbers" aria-labelledby="kn">.*?</section>', _h31, flags=_re31.S)
assert _m31 and _h31.count('id="daily"') == 0, "home page marker for daily features not found or already inserted"
pages["index.html"] = _h31[:_m31.end()] + _DAILY_HTML + _h31[_m31.end():]
# Privacy: the daily quiz can keep a streak in the browser only.
_pr = pages["privacy.html"]
_pr_add = (
    '<h2 id="s-daily-quiz-streak">Daily quiz streak</h2><p>The optional money quiz on the '
    '<a href="index.html#daily">home page</a> can save a streak in your browser '
    "(the date you last answered, whether you got it right, and how many days in a row). "
    "It stays on your device and is never sent to us. You can clear it by deleting this site's "
    "data in your browser settings. If you don't use the quiz, nothing is stored.</p>\n"
)
assert "s-daily-quiz-streak" not in _pr
# Insert after the Calculators paragraph
_pr_m = _re31.search(r"<h2>Calculators</h2><p>.*?</p>\n", _pr)
if not _pr_m:
    _pr_m = _re31.search(r"<h2 id=\"s-calculators\">Calculators</h2><p>.*?</p>\n", _pr)
assert _pr_m, "privacy calculators section not found"
pages["privacy.html"] = _pr[:_pr_m.end()] + _pr_add + _pr[_pr_m.end():]
# Nudge the short intro so local storage is acknowledged, without changing the no-cookies line.
pages["privacy.html"] = pages["privacy.html"].replace(
    "The only thing it sends anywhere is an email sign-up, and only if you press Subscribe.",
    "The only thing it sends anywhere is an email sign-up, and only if you press Subscribe. A home-page quiz can keep a streak in your browser; that is not sent to us.",
    1,
)
print("daily features: %d tips, %d quiz, %d myth/fact (preview=%s)" % (
    len(_DF["tips"]), len(_DF["quiz"]), len(_DF["myths"]), _DF.get("preview")))
