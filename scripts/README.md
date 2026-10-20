
## Weekly annuity reference-rate refresh

`annuities.html` estimates use `data/annuity-rates.json`, copied from Hargreaves Lansdown's published table
(https://www.hl.co.uk/retirement/annuities/best-buy-rates, updated weekly). To refresh (e.g. every Monday):

    python3 scripts/update_annuity_rates.py --dry-run   # check it parses and see the figures
    python3 scripts/update_annuity_rates.py             # update JSON (quote date + checked date) and rebuild
    git diff --stat && git commit -am "Annuity reference rates: HL quotes dated <date>" && git push

The script never invents values: if the page can't be fetched or parsed (missing date, missing row, changed
columns, out-of-range figure, older date than stored) it exits 1 and changes nothing. It doesn't commit or push.
Provider cards keep their own hand-checked date (`AN_PCHK` in scripts/pages18.py); update it only after re-checking those pages.
