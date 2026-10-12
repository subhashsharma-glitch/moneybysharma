# MoneyBySharma

UK personal-finance **information** site (not advice). Static HTML/CSS/JS, served by GitHub Pages from `main`.

- Refresh data (Bank of England Bank Rate, DMO gilts in issue): `python3 scripts/fetch_data.py`
- Rebuild pages: `python3 scripts/build.py`
- Calculator tests: `node tests/calc.test.js`
- Savings rates: edit `data/savings-rates.json` (schema: `data/savings-rates.schema.json`). Set `"status": "live"` only when every row is real and sourced.
- `CNAME` is set to `moneybysharma.co.uk`, but the custom domain is not yet switched on in Pages settings.
