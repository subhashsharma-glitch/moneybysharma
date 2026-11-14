# Thank-you page shown after a subscriber confirms their email.
# Kept out of search (this file runs after the search index). Noindex, not in the nav.
pages["email-confirmed.html"] = page(
    "email-confirmed.html",
    "You're confirmed – MoneyBySharma",
    "You've confirmed your weekly money update. Download the Explained Simply: Money Matters guide (PDF).",
    ph(
        "You're confirmed",
        "You're confirmed.",
        "Thanks for confirming. You can download the Explained Simply: Money Matters guide below. You'll also get a short email each Monday with what changed on this site.",
    )
    + W(
        "<p>This is a 15-page plain-English guide to UK money: payslips, tax, saving, borrowing, student loans, pensions and scams. Information only, not financial advice. Figures in the guide were checked on 14 November 2026 for the 2026/27 tax year.</p>\n"
        '<p><a class="btn" href="assets/explained-simply-money-matters.pdf">Download the guide (PDF)</a></p>\n'
        '<p class="hint">You can also find it, and the Money Matters cheat sheet, on the <a href="resources.html">Resources</a> page at any time.</p>\n'
        '<p class="related" style="margin:1.5rem 0 2rem"><a href="index.html">Home</a> &middot; <a href="resources.html">Resources</a> &middot; <a href="privacy.html#s-weekly-money-update-email-sign-up">Privacy</a></p>\n'
    ),
)
pages["email-confirmed.html"] = pages["email-confirmed.html"].replace(
    '<link rel="icon"', '<meta name="robots" content="noindex"><link rel="icon"', 1
)
print("email-confirmed thank-you page added")
