
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

## Paper Trading Experiment (paper-trading.html)

`paper-trading.html` is the "Paper Trading Experiment" page: a Grok Bot Terminal-style dashboard (equity per book,
agent panels, activity log) followed by open positions and closed trades for each book. It is built by
`scripts/pages11.py` from `data/paper-trades.json`, a copy of Chase's cleaned export
(`/workspace/paper-trading/public/paper-trades.json`, written by `export_public.py`). To refresh:

    python3 scripts/update_paper_trades.py --push   # validate, rebuild in a clean origin/main checkout, commit, push

Books and fields:
- `atr` (IA-ATR signals) and `x_buzz` (X buzz) are required; their fields and strict checks are unchanged.
- `meme_jup` (Solana meme coins, Jupiter prices, paper only) is optional. Until it appears the page shows the book as
  "starting — first trades coming soon" at $10,000; once present it is picked up automatically. Used fields:
  `start_cash`, `cash`, `position_size`, `start_date`, `open_positions[]` (`ticker`, `name`, `entry_time_uk`/`entry_date`,
  `entry_price`, `units`, `cost_basis`, `latest_price`, `latest_price_time_uk`, `price_source`,
  `market_value_after_exit_cost_usd`/`market_value_usd`, `unrealised_pnl_usd`, `unrealised_pnl_pct`),
  `closed_trades[]` (`ticker`, `entry_*`, `exit_*`, `units`, `pnl_usd`, `pnl_pct`, `exit_reason`), `totals`
  (`equity_at_market_usd`, `realised_pnl_usd`, `unrealised_pnl_usd`, `total_pnl_pct`, counts), `last_scan` (or `last_run`:
  `time_uk`, `coins_scanned`, `momentum_candidates`, `rug_check_rejections`) and `notes`.
- Each book may carry a `log` array (`time_uk`, `stage`, `action`, `ticker`, `reason`); the activity log merges them,
  newest first. A book without `log` gets entries derived from its trades. Missing fields show "–"; extra fields are ignored.
Agent panel status lines are derived from these fields; nothing is estimated.
