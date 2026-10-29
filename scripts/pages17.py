# Feedback page (exec'd from build.py after pages16). The form posts (AJAX, no redirect) to FormSubmit (formsubmit.co), the same free
# third-party service the YA Transit site uses, which emails each message to the contact address already published on this site.
# On failure assets/feedback.js shows the direct address plus a mailto/copy fallback. Target = plain-address endpoint until the address is
# activated; FormSubmit then issues a random alias that can replace it (set FB_ENDPOINT below).
import re as _re, html as _h, json as _json
FB_EMAIL = "hello@moneybysharma.co.uk"   # the contact address already used in the footer and on the privacy/about pages
FB_ENDPOINT = "https://formsubmit.co/ajax/" + FB_EMAIL   # after activation FormSubmit emails a random alias: use "https://formsubmit.co/ajax/<alias>" here instead
# Short list of site areas (value, label). Files map to the nearest area so ?page=<file> links still preselect something sensible.
_AREAS = [("home", "Home page"),
          ("savings", "Savings & bank accounts"),
          ("invest", "Investments & pensions"),
          ("credit", "Credit, debt & borrowing"),
          ("guides", "Guides & jargon"),
          ("tools", "Tools & Garmin Fitness Insights"),
          ("deals", "Deals & savings"),
          ("other", "Whole site / something else")]
_MAP = {"index.html": "home", "search.html": "home", "404.html": "home",
        "savings.html": "savings", "bank-accounts.html": "savings",
        "investments.html": "invest", "pensions.html": "invest", "gilts.html": "invest",
        "credit-cards.html": "credit", "credit-scores-debt-help.html": "credit", "mortgages.html": "credit",
        "pay-tax-payslip.html": "guides", "budgeting-emergency-fund.html": "guides", "students.html": "guides", "insurance-basics.html": "guides",
        "scams-fraud.html": "guides", "energy.html": "guides", "energy-providers.html": "guides", "broadband-phones.html": "guides",
        "electric-cars.html": "guides", "how-money-works.html": "guides", "cash-vs-inflation.html": "guides", "jargon.html": "guides", "resources.html": "guides",
        "money-matters-cheat-sheet.html": "guides", "explained-simply-money-matters.html": "guides",
        "about.html": "other", "disclaimer.html": "other", "privacy.html": "other", "feedback.html": "other",
        "tools.html": "tools", "tools/garmin-insights/": "tools", "tools/garmin-insights/index.html": "tools", "paper-trading.html": "tools", "calculators": "tools",
        "deals.html": "deals"}
_map_json = _h.escape(_json.dumps(_MAP, separators=(",", ":")), quote=True)
_opts = '<option value="">Not sure / skip</option>' + "".join(f'<option value="{k}">{_h.escape(v)}</option>' for k, v in _AREAS)
_types = [("dislike", "Something I don't like"), ("topic", "A topic I'd like covered"), ("suggestion", "A suggestion or improvement"), ("mistake", "A mistake or out-of-date information")]
_topts = '<option value="" disabled selected>Choose one…</option>' + "".join(f'<option value="{k}">{_h.escape(v)}</option>' for k, v in _types)
pages["feedback.html"] = page("feedback.html", "Feedback – tell me what to improve – MoneyBySharma",
 "Send feedback about MoneyBySharma: something you don't like, a topic you'd like covered, a suggestion or a mistake. Sent to the site owner through FormSubmit.",
 ph("Feedback", "Tell me what you think", "What's missing, what's confusing, what could be better? I'd like to hear it – short or long, it all helps."),
 W(f'''
<div class="fb-wrap">
<div class="fb-form-col">
<form id="fb-form" class="fb-form" novalidate data-endpoint="{_h.escape(FB_ENDPOINT)}" data-email="{FB_EMAIL}">
<input type="hidden" name="_subject" value="MoneyBySharma feedback">
<input type="hidden" name="_captcha" value="false">
<input type="hidden" name="_template" value="table">
<div class="hp-field" aria-hidden="true"><label for="fb-hp">Leave this field empty</label><input type="text" id="fb-hp" name="_honey" tabindex="-1" autocomplete="off"></div>
<div class="fb-field"><label for="fb-type">What is it about? <span class="req">(required)</span></label><select id="fb-type" name="type" required aria-describedby="fb-type-err">{_topts}</select><p class="fb-err" id="fb-type-err" hidden>Please choose what your message is about.</p></div>
<div class="fb-field"><label for="fb-page">Which part of the site is it about? <span class="opt">(optional)</span></label><select id="fb-page" name="page" data-map="{_map_json}">{_opts}</select></div>
<div class="fb-field"><label for="fb-msg">Your message <span class="req">(required)</span></label><textarea id="fb-msg" name="message" rows="7" maxlength="1500" required aria-describedby="fb-msg-hint fb-msg-err" placeholder="For example: “I couldn't find…”, “Please explain…”, “This figure looks out of date…”"></textarea>
<p class="hint" id="fb-msg-hint"><span id="fb-count">0</span> / 1,500 characters. Please don't include bank details, account numbers or other sensitive information.</p><p class="fb-err" id="fb-msg-err" hidden>Please write a short message.</p></div>
<div class="fb-field"><label for="fb-email">Your email address <span class="opt">(optional – only if you'd like a reply)</span></label><input id="fb-email" name="email" type="email" inputmode="email" autocomplete="email" maxlength="200" placeholder="you@example.com" aria-describedby="fb-email-hint fb-email-err"><p class="hint" id="fb-email-hint">Leave this blank if you don't need an answer.</p><p class="fb-err" id="fb-email-err" hidden>That doesn't look like an email address – check it or leave it blank.</p></div>
<div class="fb-actions"><button class="btn" type="submit" id="fb-send">Send feedback</button><span class="hint">Sent through FormSubmit, a third-party form service – see <a href="#fb-privacy">how it's handled</a>.</span></div>
</form>
<div id="fb-done" class="note fb-after fb-ok" role="status" tabindex="-1" hidden>
<p><strong>Thank you – your message has been sent.</strong></p>
<p>I read the messages I receive and use them to improve the site. If you gave an email address and asked a question, I may reply.</p>
<p><button class="btn ghost-dark" type="button" id="fb-again">Send another message</button></p>
</div>
<div id="fb-fail" class="note fb-after fb-bad" role="alert" tabindex="-1" hidden>
<p><strong>Sorry – that didn't send.</strong> Your message is still in the form above, so nothing is lost.</p>
<p>You can email it to <a href="mailto:{FB_EMAIL}">{FB_EMAIL}</a> yourself:</p>
<p><a class="btn" id="fb-mailto" href="mailto:{FB_EMAIL}">Open in my email app</a> <button class="btn ghost-dark" type="button" id="fb-copy">Copy my message</button> <span class="hint" id="fb-copied" role="status"></span></p>
<textarea id="fb-copy-src" class="sr" readonly tabindex="-1" aria-hidden="true"></textarea>
</div>
<noscript><p class="note">This form needs JavaScript. Without it, you can email <a href="mailto:{FB_EMAIL}?subject=MoneyBySharma%20feedback">{FB_EMAIL}</a> directly.</p></noscript>
</div>
<aside class="fb-side" aria-label="About feedback">
<div class="card"><h2 style="margin-top:0">How this works</h2>
<p>When you press Send, your message goes through <a href="https://formsubmit.co/">FormSubmit</a>, a free third-party form service, which emails it to me at <a href="mailto:{FB_EMAIL}">{FB_EMAIL}</a>. You stay on this page.</p>
<h3 id="fb-privacy">Privacy</h3><p>What is sent: your message, the type, the part of the site you chose, and your email address only if you give one. I use it to improve the site, and your email address only to reply to you. I never sell it. Because FormSubmit handles the sending, it has its own <a href="https://formsubmit.co/privacy.pdf">privacy policy</a>. See our <a href="privacy.html#s-feedback">privacy page</a>.</p>
<h3>Please note</h3><p>I can't give personal financial advice or look at individual accounts. For tax or investment decisions, speak to an FCA-authorised adviser. See the <a href="disclaimer.html">disclaimer</a>.</p></div>
</aside></div>'''), scripts=("feedback.js",))
