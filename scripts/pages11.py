# Paper Trading Experiment ("Grok Bot Terminal" dashboard) – exec'd from build.py.
# Reads data/paper-trades.json (copy of Chase's cleaned export, refreshed by scripts/update_paper_trades.py).
# Books: "atr" and "x_buzz" (required, fields unchanged) and "meme_jup" (optional: shown as "starting" until it
# appears in the export). Every number on the page comes from the JSON; missing fields show "–", never a guess.
import re
from zoneinfo import ZoneInfo
PT_PREVIEW = False   # True: page is noindex and left out of the sitemap
PT = json.load(open("data/paper-trades.json"))
PT_START_DEFAULT = 10000.0   # each book starts with $10,000 of fake money (used only for a book not in the export yet)
E = html.escape
def _num(x):
    try: return None if x is None or isinstance(x, bool) else float(x)
    except (TypeError, ValueError): return None
def _usd(x, sign=False):
    x = _num(x)
    if x is None: return "–"
    return ("+" if sign and x > 0 else "−" if x < 0 else "") + "$" + f"{abs(x):,.2f}"
def _pct(x, sign=True):
    x = _num(x)
    if x is None: return "–"
    return ("+" if sign and x > 0 else "−" if x < 0 else "") + f"{abs(x):.2f}%"
def _px(x):
    x = _num(x)
    if x is None: return "–"
    if x >= 1: return f"{x:,.2f}"
    if x >= 0.01: return f"{x:.4f}"
    if x <= 0: return f"{x:g}"
    import math
    return f"{x:.{min(12, 3 - math.floor(math.log10(x)))}f}"
def _units(u):
    u = _num(u)
    if u is None: return "–"
    return f"{u:,.0f}" if u >= 1000 else f"{u:,.4g}"
def _cls(v): v = _num(v) or 0; return "pt-neg" if v < 0 else "pt-pos" if v > 0 else ""
def _day(s):
    """'2026-10-23' or '2026-10-23 13:18' -> '23 Oct 2026' / '23 Oct 2026, 13:18'."""
    if not s: return "–"
    s = str(s)
    try:
        dt = datetime.date.fromisoformat(s[:10]).strftime("%-d %b %Y")
    except ValueError: return E(s)
    t = s[11:16] if len(s) >= 16 and s[13] == ":" else ""
    return dt + (", " + t if t else "")
_ts = datetime.datetime.fromisoformat(PT["as_of"])
if _ts.tzinfo: _ts = _ts.astimezone(ZoneInfo("Europe/London"))
PT_ASOF = _ts.strftime("%-d %B %Y, %H:%M") + " UK time"
PT_PLACEHOLDER = bool(PT.get("placeholder"))

BOOKS = [  # key, label, short tag, how it picks (static description of the book's rule)
 ("atr", "IA-ATR signals", "ATR", "Opens a position when a chart-based model using Average True Range (a measure of how much a price typically moves) gives a BUY signal; closes on its SELL signal, stop or target."),
 ("x_buzz", "X buzz", "X BUZZ", None),
 ("meme_jup", "Solana meme coins", "MEME", "Paper-only book of Solana meme coins priced from Jupiter's public price data. No wallet and no real orders."),
]
def _book_desc(key, default):
    b = PT.get(key) or {}
    if key == "x_buzz":
        s = b.get("description") or ""
        s = s.split(": ", 1)[1] if ": " in s else s
        return s or "Opens positions in tickers that are trending bullishly on X."
    return default
def _since(key):
    """The export's own `started` text for a book (e.g. '12 Oct 2026'); '' when missing, so callers show just the name."""
    b = PT.get(key)
    v = b.get("started") if isinstance(b, dict) else None
    return v.strip() if isinstance(v, str) and v.strip() else ""
def _since_html(key):
    s = _since(key)
    return f' <span class="tm-since" style="font-weight:400;white-space:nowrap;opacity:.8">(since {E(s)})</span>' if s else ""
def _when(o, date_key, text_key, time_key):
    """A trade's start/close date: the export's own text field (`started`/`closed`) if given, else the ISO date; plus the UK time when recorded."""
    t = o.get(text_key)
    if isinstance(t, str) and t.strip():
        tm = str(o.get(time_key) or "")
        return E(t.strip()) + (", " + tm[11:16] if len(tm) >= 16 and tm[13] == ":" else "")
    return _day(o.get(time_key) or o.get(date_key))
def _present(key):
    b = PT.get(key)
    return isinstance(b, dict) and isinstance(b.get("totals"), dict)

def _equity(b):
    """(equity, basis) from the export: equity at market if given, else equity at cost, else cash + cost basis."""
    t = b.get("totals") or {}
    if _num(t.get("equity_at_market_usd")) is not None: return _num(t["equity_at_market_usd"]), "market"
    if _num(t.get("equity_at_cost_usd")) is not None: return _num(t["equity_at_cost_usd"]), "cost"
    c = _num(b.get("cash"))
    if c is None: return None, None
    return c + sum(_num(o.get("cost_basis")) or 0 for o in b.get("open_positions") or []), "cost"
def _at_entry(o): return bool(re.search(r"\bentry\b", o.get("price_source") or "", re.I))
def _marked(key, b):
    """When open positions were last priced, in words."""
    ops = b.get("open_positions") or []
    if key == "meme_jup":
        ts = sorted({o.get("latest_price_time_uk") for o in ops if o.get("latest_price_time_uk")})
        if not ts: ts = (b.get("totals") or {}).get("marked_as_of") or []
        ts = ts if isinstance(ts, list) else [ts]
        return ("Jupiter price at " + _day(ts[-1]) + " UK") if ts else ""
    closes = sorted({o["latest_price_date"] for o in ops if o.get("latest_price_date") and not _at_entry(o)})
    if not closes:
        m = (b.get("totals") or {}).get("marked_as_of") or []
        closes = m if isinstance(m, list) else [m]
    return ("last close " + ", ".join(_day(x) for x in closes if x)) if closes else ""

# ---------- normalised activity log: the export's own "log" arrays if present, else derived from trades ----------
def _book_log(key, tag, b):
    out = []
    lg = b.get("log")
    if isinstance(lg, list) and lg:
        for e in lg:
            if not isinstance(e, dict): continue
            out.append({"t": str(e.get("time_uk") or e.get("ts_uk") or "")[:16], "book": tag, "stage": e.get("stage") or e.get("agent") or "Logger",
                        "action": e.get("action") or e.get("event") or "", "ticker": e.get("ticker") or e.get("symbol"), "reason": e.get("reason") or ""})
        return out
    for o in (b.get("open_positions") or []) + (b.get("closed_trades") or []):
        if not o.get("entry_date"): continue
        out.append({"t": str(o.get("entry_time_uk") or o["entry_date"])[:16], "book": tag, "stage": "Executor", "action": "Paper buy", "ticker": o.get("ticker"),
                    "reason": o.get("entry_reason") or f"Opened under the {tag.lower()} book's rule: {_units(o.get('units'))} units at ${_px(o.get('entry_price'))} (cost {_usd(o.get('cost_basis'))})."})
    for c in b.get("closed_trades") or []:
        if not c.get("exit_date"): continue
        out.append({"t": str(c.get("exit_time_uk") or c["exit_date"])[:16], "book": tag, "stage": "Executor", "action": "Paper sell", "ticker": c.get("ticker"),
                    "reason": f"Closed at ${_px(c.get('exit_price'))}, P&L {_usd(c.get('pnl_usd'), True)}: " + (c.get("exit_reason") or "reason not recorded")})
    return out
PT_LOG = []
for _k, _l, _tag, _ in BOOKS:
    if _present(_k): PT_LOG += _book_log(_k, _tag, PT[_k])
PT_LOG.sort(key=lambda e: e["t"], reverse=True)
PT_LOG_N = 40

# ---------- equity headline ----------
def _eq_card(key, label, tag):
    if not _present(key):
        return (f'<div class="tm-eq tm-wait"><div class="tm-k">{E(tag)}</div><div class="tm-n">{E(label)}{_since_html(key)}</div>'
                f'<div class="tm-v">{_usd(PT_START_DEFAULT)}</div><div class="tm-s">Starting equity · starting — first trades coming soon</div></div>')
    b = PT[key]; t = b["totals"]; eq, basis = _equity(b); st = _num(b.get("start_cash"))
    ch = (eq - st) if eq is not None and st is not None else None
    chp = (ch / st * 100) if ch is not None and st else None
    mk = _marked(key, b)
    sub = f'{t.get("open_count", len(b.get("open_positions") or []))} open · {t.get("closed_count", len(b.get("closed_trades") or []))} closed' + (f" · {E(mk)}" if mk and basis == "market" else " · open positions at cost" if basis == "cost" and b.get("open_positions") else "")
    return (f'<div class="tm-eq"><div class="tm-k">{E(tag)}</div><div class="tm-n">{E(label)}{_since_html(key)}</div><div class="tm-v">{_usd(eq)}</div>'
            f'<div class="tm-c {_cls(ch)}">{_usd(ch, True)} ({_pct(chp)}) vs {_usd(st)} start</div><div class="tm-s">{sub}</div></div>')
_eqs = [(_equity(PT[k])[0], _num(PT[k].get("start_cash"))) if _present(k) else (PT_START_DEFAULT, PT_START_DEFAULT) for k, *_ in BOOKS]
PT_TOTAL_EQ = sum(e for e, _ in _eqs if e is not None); PT_TOTAL_START = sum(s for _, s in _eqs if s is not None)

# ---------- agent panels: role is a fixed description, status is derived from the export ----------
_meme = PT.get("meme_jup") if _present("meme_jup") else None
_scan = (_meme or {}).get("last_scan") or (_meme or {}).get("last_run") or None
def _cnt(stage=None, action=None):
    return sum(1 for e in PT_LOG if (stage is None or e["stage"] == stage) and (action is None or e["action"] == action))
def _agents():
    a = []
    if isinstance(_scan, dict) and _scan.get("coins_scanned") is not None:
        s = f'Last meme scan {_day(_scan.get("time_uk"))} UK: {_scan["coins_scanned"]:,} coins checked, {_scan.get("momentum_candidates", "–")} momentum candidates.'
    else:
        s = "ATR and X buzz candidates come from their own signals; the meme scanner is starting, first scan results coming soon."
    a.append(("Scanner", "Finds candidates for each book: model signals, X buzz, or Solana coins with momentum.", s))
    if isinstance(_scan, dict) and _scan.get("rug_check_rejections") is not None:
        s = f'Last scan: {_scan["rug_check_rejections"]} coin{"s" if _scan["rug_check_rejections"] != 1 else ""} rejected as too risky.'
    else:
        s = "Used by the meme book only; starting, first checks coming soon."
    a.append(("Rug check", "Filters out risky meme coins (low liquidity, very new, concentrated holders, unrenounced mint) before any paper buy.", s))
    sz = [f'{_usd(PT[k]["position_size"]).replace(".00", "")} ({tag.lower().replace("x buzz", "X buzz").replace("atr", "ATR")})' for k, _, tag, _ in BOOKS if _present(k) and _num(PT[k].get("position_size"))]
    a.append(("Sizer", "Puts a fixed dollar amount into each new paper position, the same for every trade in a book.",
              ("Fixed size per trade: " + ", ".join(sz) + ".") if sz else "Fixed size per trade."))
    buys = sum(len(PT[k].get("open_positions") or []) + len(PT[k].get("closed_trades") or []) for k, *_ in BOOKS if _present(k))
    sells = sum(len(PT[k].get("closed_trades") or []) for k, *_ in BOOKS if _present(k))
    last = next((e for e in PT_LOG if e["action"] in ("Paper buy", "Paper sell")), None)
    s = f"{buys} paper buys and {sells} paper sells recorded" + (f'; latest: {E(last["action"].lower())} {E(last["ticker"] or "")}, {_day(last["t"])}.' if last else ".")
    a.append(("Executor", "Records paper fills at the quoted price. Fake money: no broker, no wallet, no real orders.", s))
    a.append(("Logger", "Writes every action down with a plain-English reason, including coins it didn't buy.",
              f"{len(PT_LOG)} actions in the log ({sum(1 for e in PT_LOG if e['action'] == 'Rejected')} rug-check rejections listed separately), newest {_day(PT_LOG[0]['t'])}." if PT_LOG else "No actions logged yet."))
    s = f"Combined paper equity {_usd(PT_TOTAL_EQ)} against {_usd(PT_TOTAL_START)} of fake starting cash."
    a.append(("Equity", "Marks open positions to the latest recorded prices and adds up cash plus positions for each book.", s))
    return "".join(f'<div class="tm-ag"><div class="tm-agh"><span class="tm-dot" aria-hidden="true"></span>{E(n)}</div><p class="tm-role">{E(r)}</p><p class="tm-st"><span class="tm-pr" aria-hidden="true">&gt;</span> {s}</p></div>' for n, r, s in a)

def _log_li(e):
    tk = f' <b>{E(str(e["ticker"]))}</b>' if e.get("ticker") else ""
    act = E(str(e["action"]))
    ac = "tm-buy" if act == "Paper buy" else "tm-sell" if act == "Paper sell" else "tm-rej" if act in ("Rejected", "Skipped") else ""
    return f'<li><span class="tm-t">[{_day(e["t"])}]</span> <span class="tm-b">{E(e["book"])}</span> <span class="tm-g">{E(str(e["stage"]))}</span> <span class="{ac}">{act}</span>{tk}<span class="tm-r">{E(str(e["reason"]))}</span></li>'
def _log_html():
    """Main log: every action except rug-check rejections, which can flood it; those go in a collapsible list."""
    if not PT_LOG: return '<p class="tm-empty">No actions logged yet.</p>'
    main = [e for e in PT_LOG if e["action"] != "Rejected"]; rej = [e for e in PT_LOG if e["action"] == "Rejected"]
    out = ('<ol class="tm-log">' + "".join(_log_li(e) for e in main[:PT_LOG_N]) + '</ol>') if main else '<p class="tm-empty">No actions other than rejections logged yet.</p>'
    out += f'<p class="tm-foot">Showing the latest {min(PT_LOG_N, len(main))} of {len(main)} actions (excluding rejections) in this export.</p>'
    if rej:
        out += (f'<details class="tm-rejs"><summary>Coins rejected by the rug check ({len(rej)} in this export)</summary>'
                '<ol class="tm-log">' + "".join(_log_li(e) for e in rej) + '</ol></details>')
    return out

# ---------- per-book detail ----------
def _book(key, label, tag, desc):
    if not _present(key):
        return (f'<section class="pt-book" id="{key}"><h2>{E(label)} book{_since_html(key)}</h2><p>{E(desc)}</p>'
                f'<div class="note pt-open"><strong>Starting — first trades coming soon.</strong> This book starts with {_usd(PT_START_DEFAULT)} of fake money. Its trades will appear here automatically once they are in the experiment log.</div></section>')
    b = PT[key]; t = b["totals"]; n = t.get("closed_count", len(b.get("closed_trades") or []))
    meme = key == "meme_jup"
    wins = t.get("win_count")
    win = f'{wins / n * 100:.0f}% ({wins} of {n})' if n and wins is not None else "– (no closed trades yet)"
    eq, basis = _equity(b); mk = _marked(key, b)
    cells = [("Starting cash", _usd(b.get("start_cash")), ""), ("Cash", _usd(b.get("cash")), ""),
             ("Closed-trade P&amp;L", _usd(t.get("realised_pnl_usd"), True), _cls(t.get("realised_pnl_usd")))]
    if basis == "market":
        cells += [("Unrealised P&amp;L (open positions)", _usd(t.get("unrealised_pnl_usd"), True), _cls(t.get("unrealised_pnl_usd"))),
                  ("Total P&amp;L, % of starting cash", _pct(t.get("total_pnl_pct")), _cls(t.get("total_pnl_pct"))),
                  ("Equity at market" + (" (after modelled 1% exit cost)" if meme and t.get("open_positions_value_after_exit_cost_usd") is not None else ""), _usd(eq), "")]
    else:
        cells += [("Equity at cost (open positions not marked)", _usd(eq), "")]
    cells += [("Open positions", str(t.get("open_count", len(b.get("open_positions") or []))), ""), ("Closed trades", str(n), ""), ("Win rate (closed trades)", win, "")]
    tot = '<div class="pt-tot">' + "".join(f'<div{" class=pt-eq" if l.startswith("Equity") else ""}><span>{l}</span><b class="{c}">{v}</b></div>' for l, v, c in cells) + '</div>'
    ops = b.get("open_positions") or []
    if ops:
        mvk = "market_value_after_exit_cost_usd" if meme and any(o.get("market_value_after_exit_cost_usd") is not None for o in ops) else "market_value_usd"
        rows = []
        for o in ops:
            when = o.get("latest_price_time_uk") or o.get("latest_price_date")
            dt = f'<span class="pt-d">{_day(when)}{" UK" if o.get("latest_price_time_uk") else ""}</span>' if when else ""
            if _at_entry(o): dt += '<span class="pt-d">Entry price (opened since last close)</span>'
            nm = f'<span class="pt-d">{E(o["name"])}</span>' if o.get("name") and o.get("name") != o.get("ticker") else ""
            rows.append(f'<tr><th scope="row">{E(str(o.get("ticker")))}{nm}</th><td>{_when(o, "entry_date", "started", "entry_time_uk")}</td><td>{_px(o.get("entry_price"))}</td><td>{_units(o.get("units"))}</td><td>{_usd(o.get("cost_basis"))}</td>'
                        f'<td>{_px(o.get("latest_price"))}{dt}</td><td>{_usd(o.get(mvk))}</td><td class="{_cls(o.get("unrealised_pnl_usd"))}">{_usd(o.get("unrealised_pnl_usd"), True)}</td><td class="{_cls(o.get("unrealised_pnl_pct"))}">{_pct(o.get("unrealised_pnl_pct"))}</td></tr>')
        mvh = "Market value after 1% exit cost ($)" if mvk != "market_value_usd" else "Market value ($)"
        srcs = sorted({o["price_source"] for o in ops if o.get("price_source") and not _at_entry(o)})
        openp = (f'<div class="table-scroll"><table class="pt pt-o"><thead><tr><th>{"Coin" if meme else "Ticker"}</th><th>Started</th><th>Entry price ($)</th><th>Units</th><th>Cost ($)</th><th>Current price ($)</th><th>{mvh}</th><th>Unrealised P&amp;L ($)</th><th>Unrealised P&amp;L (%)</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>'
                 f'<p class="hint">Current price = latest price recorded in the log' + (f' ({E(mk)})' if mk else '') + (f'; source: {E("; ".join(srcs))}' if srcs else '') + '. Prices in US dollars. Unrealised P&amp;L is a paper figure and changes with every price update.</p>')
    else:
        openp = '<p class="hint">No open positions in this book.</p>'
    cts = b.get("closed_trades") or []
    if cts:
        rows = "".join(f'<tr><th scope="row">{E(str(c.get("ticker")))}</th><td>{_when(c, "entry_date", "started", "entry_time_uk")}</td><td>{_px(c.get("entry_price"))}</td><td>{_when(c, "exit_date", "closed", "exit_time_uk")}</td><td>{_px(c.get("exit_price"))}</td><td>{_units(c.get("units"))}</td><td class="{_cls(c.get("pnl_usd"))}">{_usd(c.get("pnl_usd"), True)}</td><td class="{_cls(c.get("pnl_pct"))}">{_pct(c.get("pnl_pct"))}</td><td>{E(c.get("exit_reason") or "–")}</td></tr>'
                       for c in sorted(cts, key=lambda c: str(c.get("exit_time_uk") or c.get("exit_date") or ""), reverse=True))
        closed = f'<div class="table-scroll"><table class="pt pt-c"><thead><tr><th>{"Coin" if meme else "Ticker"}</th><th>Started</th><th>Entry price ($)</th><th>Closed</th><th>Exit price ($)</th><th>Units</th><th>P&amp;L ($)</th><th>P&amp;L (%)</th><th>Why it closed</th></tr></thead><tbody>{rows}</tbody></table></div>'
    else:
        closed = '<p class="hint">No closed trades yet in this book.</p>'
    sd = "" if _since(key) else (_day(b["start_date"]) if b.get("start_date") else "")   # the heading already shows `started`
    return (f'<section class="pt-book" id="{key}"><h2>{E(label)} book{_since_html(key)}</h2><p>{E(desc)}' + (f' Started {E(sd)}.' if sd else '') + f' Fake money, in US dollars.</p>{tot}'
            f'<h3>Open positions</h3>{openp}<h3>Closed trades</h3>{closed}</section>')

_ph = '<div class="note" role="note" style="border-left-color:#b3261e"><strong>Placeholder data.</strong> The figures below are placeholders, not results from the experiment.</div>' if PT_PLACEHOLDER else ""
PT_DISC = ('<div class="pt-warn" role="note"><p class="pt-warn-h">Fake money. Paper trading experiment only.</p>'
           '<p>This is <strong>not financial advice</strong> and <strong>not a recommendation to buy or sell any coin or share</strong>. '
           'No real money is used and no real orders are placed. <strong>Crypto and meme coins are highly risky</strong>: prices can swing wildly or fall to zero, and many coins are scams. '
           'Past results, real or paper, don\'t predict future ones.</p></div>')
_eqcards = "".join(_eq_card(k, l, tag) for k, l, tag, _ in BOOKS)
pages["paper-trading.html"] = page("paper-trading.html", "Paper Trading Experiment – MoneyBySharma",
 "Paper Trading Experiment: three fake-money books (IA-ATR signals, X buzz and Solana meme coins) each starting at $10,000, with agent status, open positions, closed trades and a log of every action. Not advice.",
 ph("<a href=\"tools.html\">Tools</a> › Paper Trading Experiment", "Paper Trading Experiment", "Three fake-money books, each starting with $10,000, run step by step by simple software agents and logged in public."), W(f'''
{PT_DISC}
<p><strong>Data as of {PT_ASOF}.</strong> {E(PT.get("disclaimer") or "")}</p>{_ph}
<section class="tm" aria-labelledby="tm-h">
<div class="tm-bar"><span class="tm-dots" aria-hidden="true"><i></i><i></i><i></i></span><span class="tm-title" id="tm-h">Grok Bot Terminal</span><span class="tm-asof">paper mode · {PT_ASOF}</span></div>
<div class="tm-body">
<h2 class="tm-h">Equity by book</h2>
<div class="tm-eqs">{_eqcards}</div>
<p class="tm-sum">Combined paper equity <b>{_usd(PT_TOTAL_EQ)}</b> against {_usd(PT_TOTAL_START)} of fake starting cash.</p>
<h2 class="tm-h">Agents</h2>
<div class="tm-ags">{_agents()}</div>
<h2 class="tm-h" id="log">Activity log <span>(newest first, with reasons)</span></h2>
{_log_html()}
</div></section>
<h2>How the experiment works</h2>
<ul>
<li><strong>Three separate books</strong>, each starting with $10,000 of fake money. Each puts a fixed dollar amount into every position it opens. No real money, broker or wallet is involved.</li>
<li><strong>IA-ATR signals{_since_html("atr")}:</strong> {E(BOOKS[0][3])}</li>
<li><strong>X buzz{_since_html("x_buzz")}:</strong> {E(_book_desc("x_buzz", ""))}</li>
<li><strong>Solana meme coins{_since_html("meme_jup")}:</strong> {E(_meme["notes"]) if _meme and _meme.get("notes") else E(BOOKS[2][3])}</li>
<li><strong>Prices and marks.</strong> The ATR and X buzz books are marked to the last official daily close; the meme book uses the latest Jupiter price recorded by the experiment. Unrealised gains and losses are paper figures and can be out of date.</li>
<li><strong>This is not a live record.</strong> It is a log updated from time to time, so it may be behind. Real trades could have filled at different prices.</li>
</ul>
{"".join(_book(k, l, tag, _book_desc(k, desc)) for k, l, tag, desc in BOOKS)}
<p class="src">Source: our own experiment log (fake money), exported {PT_ASOF}. Nothing here is a prediction, a signal or a track record of real investing. See also the <a href="disclaimer.html">disclaimer</a>. Currency: US dollars.</p>'''))
if PT_PREVIEW:
    pages["paper-trading.html"] = pages["paper-trading.html"].replace('<link rel="icon"', '<meta name="robots" content="noindex"><link rel="icon"', 1)
