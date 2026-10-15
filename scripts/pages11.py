# Paper trading experiment (PREVIEW) – exec'd from build.py. Reads data/paper-trades.json (copy of Chase's cleaned export).
PT_PREVIEW = False   # True: page is noindex and left out of the sitemap
PT = json.load(open("data/paper-trades.json"))
_PT_FOOTNOTE_DATE = lambda iso: datetime.date.fromisoformat(iso[:10]).strftime("%-d %b %Y")
def _usd(x, sign=False):
    if x is None: return "–"
    s = f"{abs(x):,.2f}"
    return ("+" if sign and x > 0 else "−" if x < 0 else "") + "$" + s
def _pct(x, sign=True):
    if x is None: return "–"
    return ("+" if sign and x > 0 else "−" if x < 0 else "") + f"{abs(x):.2f}%"
def _px(x): return f"{x:,.2f}" if x >= 1 else f"{x:,.4f}"
def _short_reason(r):
    r = (r or "").strip()
    return "Stop-loss level reached" if r.lower().startswith("stop") else html.escape(r.split(";")[0][:90])
_ts = datetime.datetime.fromisoformat(PT["as_of"])
PT_ASOF = _ts.strftime("%-d %B %Y, %H:%M") + " UK time"
PT_PLACEHOLDER = bool(PT.get("placeholder"))
def _book(key, label, blurb):
    b = PT[key]; t = b["totals"]; n = t["closed_count"]
    win = f'{t["win_count"] / n * 100:.0f}% ({t["win_count"]} of {n})' if n else "– (no closed trades yet)"
    cls = lambda v: "pt-neg" if (v or 0) < 0 else "pt-pos" if (v or 0) > 0 else ""
    tot = (f'<div class="pt-tot"><div><span>Cash</span><b>{_usd(b["cash"])}</b></div>'
           f'<div><span>Starting cash</span><b>{_usd(b["start_cash"])}</b></div>'
           f'<div><span>Closed-trade P&amp;L</span><b class="{cls(t["realised_pnl_usd"])}">{_usd(t["realised_pnl_usd"], True)}</b></div>'
           f'<div><span>Closed-trade P&amp;L, % of starting cash</span><b class="{cls(t["realised_pnl_pct"])}">{_pct(t["realised_pnl_pct"])}</b></div>'
           f'<div><span>Closed trades</span><b>{n}</b></div>'
           f'<div><span>Open positions</span><b>{t["open_count"]}</b></div>'
           f'<div><span>Win rate (closed trades)</span><b>{win}</b></div></div>')
    if b["closed_trades"]:
        rows = "".join(f'<tr><th scope="row">{html.escape(c["ticker"])}</th><td>{_PT_FOOTNOTE_DATE(c["entry_date"])}</td><td>{_px(c["entry_price"])}</td><td>{_PT_FOOTNOTE_DATE(c["exit_date"])}</td><td>{_px(c["exit_price"])}</td><td>{c["units"]:,.4g}</td><td class="{cls(c["pnl_usd"])}">{_usd(c["pnl_usd"], True)}</td><td class="{cls(c["pnl_pct"])}">{_pct(c["pnl_pct"])}</td><td>{_short_reason(c.get("exit_reason"))}</td></tr>' for c in sorted(b["closed_trades"], key=lambda c: c["exit_date"], reverse=True))
        closed = f'<div class="table-scroll"><table class="pt"><thead><tr><th>Ticker</th><th>Entered</th><th>Entry price ($)</th><th>Exited</th><th>Exit price ($)</th><th>Units</th><th>P&amp;L ($)</th><th>P&amp;L (%)</th><th>How it closed</th></tr></thead><tbody>{rows}</tbody></table></div>'
    else:
        closed = '<p class="hint">No closed trades yet in this book.</p>'
    if b["open_positions"]:
        orow = "".join(f'<tr><th scope="row">{html.escape(o["ticker"])}</th><td>{_PT_FOOTNOTE_DATE(o["entry_date"])}</td><td>{_px(o["entry_price"])}</td><td>{o["units"]:,.4g}</td><td>{_usd(o["cost_basis"])}</td><td>Not shown</td></tr>' for o in b["open_positions"])
        openp = f'<div class="table-scroll"><table class="pt"><thead><tr><th>Ticker</th><th>Entered</th><th>Entry price ($)</th><th>Units</th><th>Cost basis ($)</th><th>Unrealised P&amp;L</th></tr></thead><tbody>{orow}</tbody></table></div>'
    else:
        openp = '<p class="hint">No open positions in this book.</p>'
    return f'''<section class="pt-book" id="{key}"><h2>{label}</h2><p>{blurb} Started {d(b["start_date"])} (first trade date). Amounts in US dollars of fake money.</p>
{tot}
<h3>Closed trades</h3><p class="hint">Closed-trade P&amp;L is the only P&amp;L counted in the totals above.</p>{closed}
<h3>Open positions</h3><div class="note pt-open"><strong>Cost basis only, not marked to market, unrealised P&amp;L not shown.</strong> These are open positions in a fake-money experiment, recorded as a log. They are not a recommendation about any investment.</div>{openp}</section>'''
_ph = '<div class="note" role="note" style="border-left-color:#b3261e"><strong>Placeholder data.</strong> The figures below are placeholders, not results from the experiment.</div>' if PT_PLACEHOLDER else ""
pages["paper-trading.html"] = page("paper-trading.html", "Paper trading experiment – MoneyBySharma",
 "A fake-money paper trading experiment with two books: closed trades, open positions at cost basis, and totals. Experiment only, not advice.",
 ph("<a href=\"tools.html\">Tools</a> › Paper trading experiment", "Paper trading experiment", "Two fake-money books, logged in public."), W(f'''
<div class="note pt-label" role="note" style="margin-top:1.5rem;border-left-color:#b3261e;font-size:1.1rem"><strong>Experiment with fake money. Not advice, not a recommendation, not a signal. Past results don't predict future ones.</strong></div>
<p><strong>Data as of {PT_ASOF}.</strong> {PT["disclaimer"]}</p>{_ph}
<h2>How the experiment works</h2>
<ul>
<li>Two separate books, each starting with $10,000 of fake money and putting $1,000 into each position it opens. No real money is used.</li>
<li><strong>ATR book:</strong> positions opened when a chart-based model (using Average True Range, a measure of how much a price typically moves) flags them.</li>
<li><strong>X buzz book:</strong> {html.escape(PT["x_buzz"]["description"].split(": ",1)[1] if ": " in PT["x_buzz"]["description"] else PT["x_buzz"]["description"])}</li>
<li><strong>This is not a live record.</strong> It is a log kept by hand and by script, updated from time to time, so it may be out of date. Prices are those recorded when each entry or exit was logged, including pre-market prices, and real trades could have filled at different prices.</li>
<li><strong>Totals cover closed trades only.</strong> Open positions are shown at cost basis, not marked to market, so unrealised gains and losses are not in any total. Start dates are the date of each book's first trade, not necessarily when it was set up.</li>
</ul>
{_book("atr", "ATR book", "A fake-money book run on an ATR-based model.")}
{_book("x_buzz", "X buzz book", "A fake-money book run on trending tickers on X.")}
<p class="src">Source: our own experiment log (fake money), exported {PT_ASOF}. Nothing here is a prediction, and no figure is a track record of real investing. See also the <a href="disclaimer.html">disclaimer</a>. Currency: US dollars (the log is kept in dollars).</p>'''))
if PT_PREVIEW:
    pages["paper-trading.html"] = pages["paper-trading.html"].replace('<link rel="icon"', '<meta name="robots" content="noindex"><link rel="icon"', 1)
