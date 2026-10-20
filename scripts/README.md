
## Weekly annuity reference-rate refresh

`annuities.html` estimates use `data/annuity-rates.json`, copied from Hargreaves Lansdown's published table
(https://www.hl.co.uk/retirement/annuities/best-buy-rates, updated weekly). To refresh (e.g. every Monday):

    python3 scripts/update_annuity_rates.py --dry-run   # check it parses and see the figures
    python3 scripts/update_annuity_rates.py             # update JSON (quote date + checked date) and rebuild
    git diff --stat && git commit -am "Annuity reference rates: HL quotes dated <date>" && git push

The script never invents values: if the page can't be fetched or parsed (missing date, missing row, changed
columns, out-of-range figure, older date than stored) it exits 1 and changes nothing. It doesn't commit or push.
Provider cards keep their own hand-checked date (`AN_PCHK` in scripts/pages18.py); update it only after re-checking those pages.

## Annuity figures by provider (Which? article)

The "Income by provider and pot size" tables on `annuities.html` use `data/annuity-providers.json`, copied from the Which?
annuity rates article (figures from MoneyHelper's comparison tool, £100,000, ages 65 and 70):
https://www.which.co.uk/money/pensions-and-retirement/accessing-your-pensions/annuities/annuity-rates-aQGfH6W5n2rm
Which? updates it roughly monthly. To refresh:

    python3 scripts/update_annuity_providers.py --dry-run   # parse and print; writes nothing
    python3 scripts/update_annuity_providers.py             # update figures, quote date, checked date; rebuild
    git diff --stat && git commit -am "Annuity provider figures: Which? dated <date>" && git push

Same never-invent rule: if any table, column, provider, figure or date can't be parsed, it exits 1 and changes nothing.
Which?'s highest-first ordering is ignored; providers stay A to Z. Other pot sizes on the page are scaled from £100k and labelled.
