# pages24.py – PREVIEW ONLY (branch cash-isa-preview, not for main yet): "Cash ISAs explained".
# noindex; kept out of the search index, sitemap and menus. Figures re-checked on official pages 29 Oct 2026.
PREVIEW_PAGES = {"cash-isas.html"}
_S = lambda u, t: f'<a href="{u}">{t}</a>'
_ISA = "https://www.gov.uk/individual-savings-accounts"
_JISA = "https://www.gov.uk/junior-individual-savings-accounts"
_TRANS = "https://www.gov.uk/individual-savings-accounts/transferring-your-isa"
_PSA = "https://www.gov.uk/apply-tax-free-interest-on-savings"
_FSCS = "https://www.fscs.org.uk/what-we-cover/banks-building-societies-credit-unions/deposit-limit/"
_OOTLAR = "https://www.gov.uk/government/publications/budget-2026-overview-of-tax-legislation-and-rates-ootlar/budget-2026-overview-of-tax-legislation-and-rates-ootlar"
_CHK = "Checked 29 October 2026"
pages["cash-isas.html"] = page("cash-isas.html", "Cash ISAs Explained: 2026/27 Limit, Tax & Protection (UK)",
  "How cash ISAs work in 2026/27: the £20,000 allowance, why the cash ISA limit stays £20,000 from April 2027, tax, transfers and FSCS protection.",
  ph("Cash ISAs", "Cash ISAs, explained", "What a cash ISA is, how much you can put in, how transfers work and how your money is protected. Every figure links to its official source. Information, not financial advice.") + W(f'''
<div class="card" style="margin-top:1.5rem"><span class="tag">Preview</span>
<p><strong>Draft page for review.</strong> It isn't linked from the menus or search, and search engines are asked not to index it.</p></div>

<h2 id="key">Key figures (2026/27)</h2>
<table><thead><tr><th>What</th><th>Figure</th><th>Official source</th></tr></thead><tbody>
<tr><td>Total you can save in ISAs this tax year</td><td>£20,000</td><td>{_S(_ISA, "GOV.UK – Individual Savings Accounts")} ({_CHK})</td></tr>
<tr><td>How much of that can go in a cash ISA</td><td>All of it (up to £20,000)</td><td>{_S(_ISA, "GOV.UK – Individual Savings Accounts")} ({_CHK})</td></tr>
<tr><td>Minimum age to open a cash ISA</td><td>18</td><td>{_S(_ISA, "GOV.UK – Individual Savings Accounts")} ({_CHK})</td></tr>
<tr><td>Cash ISA limit from April 2027</td><td>Stays £20,000 for savers over 18 (announced at Budget 2026)</td><td>{_S(_OOTLAR, "GOV.UK/HM Treasury – Budget 2026: overview of tax legislation and rates")} ({_CHK})</td></tr>
<tr><td>Junior ISA limit</td><td>£9,000</td><td>{_S(_JISA, "GOV.UK – Junior ISAs")} ({_CHK})</td></tr>
<tr><td>Personal Savings Allowance (interest outside ISAs)</td><td>£1,000 basic rate, £500 higher rate, £0 additional rate</td><td>{_S(_PSA, "GOV.UK – Tax on savings interest")} ({_CHK})</td></tr>
<tr><td>FSCS deposit protection</td><td>£120,000 per person, per authorised firm (from 1 December 2025)</td><td>{_S(_FSCS, "FSCS – Deposit protection limit")} ({_CHK})</td></tr>
</tbody></table>

<h2 id="what">What is a cash ISA?</h2>
<p>A cash ISA is a savings account where the interest isn't taxed. It doesn't use up your Personal Savings Allowance, so it matters most if your interest outside an ISA would go over that allowance. Cash ISAs come in easy access, notice and fixed-rate versions, just like ordinary savings accounts. See {_S("savings.html#types", "the main types of savings account")}.</p>

<h2 id="budget">What Budget 2026 changed</h2>
<p>A cut to the cash ISA limit for under-65s from April 2027 had been planned. At Budget 2026 on 28 October 2026 the government said it will keep the cash ISA limit at £20,000 for all savers over 18 from April 2027. The change is due to be made by regulations in November 2026, so check the latest position. Budget 2026 also announced higher tax rates on savings interest outside ISAs from 6 April 2027 (not law yet). See {_S("budget-2026.html#savers", "Budget 2026 for savers")}.</p>

<h2 id="transfer">Moving a cash ISA</h2>
<p>To switch providers, contact the provider you want to move to and fill in their ISA transfer form. If you take the money out yourself instead, you can't reinvest that part of your allowance again. Some providers have restrictions or charge for transfers, so check first. Source: {_S(_TRANS, "GOV.UK – Transferring your ISA")} ({_CHK}).</p>

<h2 id="protect">Is my money protected?</h2>
<p>Cash ISAs with UK-authorised banks and building societies count towards the FSCS limit of £120,000 per person, per authorised firm. Brands that share one banking licence count as one firm. See {_S("savings.html#fscs", "FSCS protection")}.</p>

<p class="hint" style="margin-top:1.5rem">Information, not financial advice. Rates and rules change, so check the official pages linked above before you decide.</p>'''))
pages["cash-isas.html"] = pages["cash-isas.html"].replace('<link rel="icon"', '<meta name="robots" content="noindex"><link rel="icon"', 1)
