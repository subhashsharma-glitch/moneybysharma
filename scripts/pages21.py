# Budget 2026: what it means for you. Published 28 Oct 2026 (approved by Subhash).
# Every figure comes from /workspace/budget-2026/report.md (Budget 28 Oct 2026), checked 28 Oct 2026.
# In the sitemap and search index; linked from a homepage banner (not in the nav).
def _bs(*keys):
    return '<p class="src">Sources (checked 28 October 2026): ' + "; ".join(f'<a href="{S[k][1]}" rel="noopener">{S[k][0]}</a>' for k in keys) + ".</p>"
NLY = '<span class="b26-tag">Not law yet</span>'
PLAN = '<span class="b26-tag b26-plan">A plan</span>'
B26_CSS = '''<style>
.b26-tag{display:inline-block;font-size:.72rem;font-weight:700;letter-spacing:.02em;text-transform:uppercase;background:#fff1e0;color:#8a4a0f;border:1px solid #f0c48f;border-radius:999px;padding:.05rem .5rem;margin-left:.3rem;vertical-align:middle;white-space:nowrap}
.b26-plan{background:#e7f2ef;color:#0f4c45;border-color:#b9d8d0}
.b26-60{background:#e7f2ef;border-left:4px solid #0f4c45;border-radius:10px;padding:1rem 1.2rem;margin:1rem 0}
.b26-60 ul{margin:.3rem 0 0;padding-left:1.2rem}.b26-60 li{margin:.25rem 0}
.b26-sum td,.b26-sum th{vertical-align:top}
.b26-calc{background:#fff;border:1px solid #d7e3df;border-radius:10px;padding:1rem 1.1rem;margin:1rem 0}
.b26-calc h3{margin-top:0}.b26-calc ol{padding-left:1.2rem;margin:.4rem 0}.b26-calc li{margin:.3rem 0}
.b26-tl{list-style:none;margin:1rem 0;padding:0;border-left:3px solid #0f4c45}
.b26-tl li{position:relative;padding:.1rem 0 .9rem 1.1rem}
.b26-tl li::before{content:"";position:absolute;left:-8px;top:.45rem;width:13px;height:13px;border-radius:50%;background:#d9822b;border:2px solid #fff}
.b26-tl b{display:block;font-family:Georgia,serif;color:#0f4c45}
.b26-more{margin:.6rem 0 0;font-weight:600}
main h2[id]{scroll-margin-top:90px}
</style>'''
_b26_body = ph("Budget 2026", "Budget 2026: what it means for you",
 "What the Budget on 28 October 2026 changes for workers, savers, investors, first-time buyers, pensioners, households and drivers, and what stays the same. Information, not financial advice.") + W(f'''{B26_CSS}
<div class="cols"><div>
<p class="hint">Budget delivered on Wednesday 28 October 2026. Every figure on this page links to its source and was checked on 28 October 2026. Many measures still need to be passed by Parliament: we mark those <span class="b26-tag">Not law yet</span>, and aims or plans without firm rules <span class="b26-tag b26-plan">A plan</span>.</p>

<h2 id="sixty">In 60 seconds</h2>
<div class="b26-60"><ul>
<li><strong>Cash ISAs stay at £20,000</strong> for everyone aged 18+. The planned cut from April 2027 has been scrapped.</li>
<li><strong>Tax on savings interest outside ISAs rises to 24% / 44% / 49%</strong> from 6 April 2027. {NLY}</li>
<li><strong>Minimum wage rises to £13.21 an hour</strong> (age 21+) from 1 April 2027.</li>
<li><strong>The trading allowance triples to £3,000</strong> from 6 April 2027. {NLY}</li>
<li><strong>Full new State Pension: £13,036.40 a year</strong> from April 2027, plus a new Pension Tax Allowance. {NLY}</li>
<li><strong>£100 Household Energy Payment</strong> for council tax bands A–D in England from January 2027, and 0% VAT on household electricity extended to 30 June 2027.</li>
<li><strong>First-time buyers:</strong> a lower 20% Lifetime ISA charge on homes over £450,000 from 29 October 2026, and a new First Time Buyer ISA planned for April 2029.</li>
<li><strong>Income tax and the main National Insurance thresholds stay frozen, and the rates don't change.</strong> Two smaller NI limits rise from 2027-28: the lower earnings limit to £133 a week and the small profits threshold to £7,355.</li>
</ul><p style="margin:.6rem 0 0"><strong>Information, not financial advice.</strong> How this affects you depends on your own circumstances.</p></div>

<h3>What's changed and what hasn't</h3>
<table class="b26-sum"><caption class="sr">Budget 2026: changed versus unchanged</caption><thead><tr><th scope="col">Area</th><th scope="col">What's changed</th><th scope="col">What hasn't</th></tr></thead><tbody>
<tr><th scope="row">Income tax</th><td>No change</td><td>Thresholds confirmed frozen to 2030-31: £12,570 Personal Allowance; 20% / 40% / 45%; higher rate from £50,271; additional rate above £125,140</td></tr>
<tr><th scope="row">National Insurance</th><td>From 2027-28: lower earnings limit £133 a week, small profits threshold £7,355, voluntary Class 2 / Class 3 £3.80 / £19.05 a week</td><td>Employee rates 8% / 2%; primary threshold £242 and upper earnings limit £967 a week</td></tr>
<tr><th scope="row">Savings</th><td>Savings income tax 24% / 44% / 49% from 6 April 2027 (not law yet)</td><td>Personal Savings Allowance £1,000 / £500 / £0; £5,000 starting rate for savings</td></tr>
<tr><th scope="row">ISAs</th><td>Planned cash ISA cut scrapped; Lifetime ISA charge 20% on homes over £450,000; First Time Buyer ISA planned for April 2029</td><td>£20,000 ISA allowance; Junior ISA £9,000</td></tr>
<tr><th scope="row">Investing</th><td>Business asset disposal relief limit £1m to £500,000 from 6 April 2027; new 10% CGT founders' relief (both not law yet)</td><td>CGT 18% / 24%, £3,000 annual exempt amount; dividend tax 10.75% / 35.75% / 39.35%, £500 allowance</td></tr>
<tr><th scope="row">Pensions</th><td>State Pension £13,036.40 a year from April 2027; Pension Tax Allowance (not law yet); triple lock changes from April 2030 (a plan)</td><td>Annual allowance £60,000; MPAA £10,000; lump sum allowance £268,275</td></tr>
<tr><th scope="row">Pay</th><td>Minimum wage £13.21 / £11.27 / £8.31 from 1 April 2027; trading allowance £3,000 from 6 April 2027 (not law yet)</td><td>Salary sacrifice £2,000 NI cap from April 2029, as announced in 2025</td></tr>
<tr><th scope="row">Home and energy</th><td>£100 energy payment (England, bands A–D); 0% electricity VAT to 30 June 2027; gas standing charges to go (a plan)</td><td>Stamp duty residential rates; the £1,723 price cap for October to December 2026</td></tr>
<tr><th scope="row">Inheritance tax</th><td>Only technical tweaks</td><td>£325,000 nil-rate band; £175,000 residence nil-rate band; pensions still come into IHT from April 2027</td></tr>
</tbody></table>
{_bs("b26a","b26o","b26b")}

<h2 id="workers">Workers and the self-employed</h2>
<ul>
<li><strong>Income tax and NI:</strong> rates don't change, and the main thresholds stay frozen, including the NI primary threshold (£242 a week) and upper earnings limit (£967 a week). HM Treasury confirms income tax thresholds stay frozen to 2030-31. Two smaller NI limits rise from 2027-28: the lower earnings limit to £133 a week and the small profits threshold to £7,355. See <a href="pay-tax-payslip.html#tax">Pay, tax and your payslip</a>.</li>
<li><strong>Minimum wage from 1 April 2027:</strong> £13.21 an hour aged 21+ (up 3.9%), £11.27 aged 18–20, and £8.31 aged 16–17 and apprentices. See <a href="pay-tax-payslip.html#minwage">minimum wage rates</a>.</li>
<li><strong>Side income:</strong> the trading allowance triples from £1,000 to £3,000 from 6 April 2027, and the Self Assessment reporting threshold for side income also becomes £3,000. {NLY} See <a href="pay-tax-payslip.html#side">side income</a>.</li>
<li><strong>Self-employed NI in 2027-28:</strong> small profits threshold £7,355; voluntary Class 2 £3.80 a week and Class 3 £19.05 a week.</li>
<li><strong>Business mileage:</strong> the tax-free rate for business miles above 10,000 a year rises from 25p to 35p from 6 April 2027.</li>
</ul>
{_bs("b26a","b26o","b26b")}

<h2 id="savers">Savers</h2>
<ul>
<li><strong>Cash ISAs stay at £20,000.</strong> The plan to limit under-65s to £12,000 a year in cash ISAs from April 2027 won't go ahead. Transfers from stocks and shares ISAs to cash ISAs are still allowed. This is due to be done by regulations laid in November 2026. See <a href="savings.html#tax">Savings: tax and ISAs</a>.</li>
<li><strong>Savings income tax rises from 6 April 2027</strong> to 24% (basic rate), 44% (higher rate) and 49% (additional rate). That's 2 percentage points above the 22% / 42% / 47% set in November 2025. {NLY} It's in Finance Bill 2026-27.</li>
<li><strong>Unchanged:</strong> Personal Savings Allowance £1,000 (basic rate), £500 (higher rate), £0 (additional rate); starting rate for savings £5,000.</li>
<li><strong>Interest inside an ISA isn't taxed,</strong> so the higher savings rates don't apply to money held in one.</li>
</ul>
<div class="b26-calc"><h3>Worked example: tax on £1,200 of interest in 2027/28</h3>
<p><strong>Illustrative person, not a real case:</strong> £30,000 in a savings account outside an ISA, earning an assumed 4% a year (£1,200 of interest), all taxed in 2027/28. We assume the £5,000 starting rate for savings doesn't apply because their other income is too high. The 4% rate is an assumption for the example, not a rate on offer.</p>
<ol>
<li><strong>As a basic-rate taxpayer:</strong> £1,200 interest − £1,000 Personal Savings Allowance = £200 taxable. £200 × 24% = <strong>£48</strong> tax. (At the 22% rate set before the Budget: £200 × 22% = £44, so <strong>£4 more</strong>.)</li>
<li><strong>As a higher-rate taxpayer:</strong> £1,200 − £500 allowance = £700 taxable. £700 × 44% = <strong>£308</strong> tax. (At 42%: £700 × 42% = £294, so <strong>£14 more</strong>.)</li>
<li><strong>As an additional-rate taxpayer:</strong> no allowance, so £1,200 × 49% = <strong>£588</strong>. (At 47%: £564, so <strong>£24 more</strong>.)</li>
<li><strong>In a cash ISA:</strong> £0 tax on the same interest.</li>
</ol>
<p class="hint" style="margin:.4rem 0 0">The 24% / 44% / 49% rates are not law yet. For gilts, the <a href="gilts.html#calc">gilt vs savings calculator</a> now includes these rates.</p></div>
{_bs("b26o","b26a","b26mse")}

<h2 id="investors">Investors</h2>
<ul>
<li><strong>No charge on cash in stocks and shares ISAs:</strong> the planned 22% charge on cash interest held inside stocks and shares ISAs has been scrapped, along with the other rules meant to stop people getting around the cash ISA cut.</li>
<li><strong>New incentive for first-time investors</strong> in stocks and shares ISAs: the government will work with industry on it. The design isn't set yet. {PLAN}</li>
<li><strong>Unchanged:</strong> capital gains tax 18% / 24% with a £3,000 annual exempt amount; dividend tax 10.75% / 35.75% / 39.35% with a £500 allowance.</li>
<li><strong>For business owners:</strong> the business asset disposal relief limit falls from £1 million to £500,000 from 6 April 2027, and there's a new 10% CGT founders' relief. {NLY}</li>
</ul>
<p>See <a href="investments.html#isa">Investments: ISAs</a>. With investments your capital is at risk.</p>
{_bs("b26o","b26a","b26w")}

<h2 id="buyers">First-time buyers</h2>
<ul>
<li><strong>Lifetime ISA, from 29 October 2026:</strong> if you use your LISA to buy a first home costing over £450,000, the withdrawal charge is 20% instead of 25%. Other unauthorised withdrawals still pay 25%. The regulations were laid on 28 October 2026.</li>
<li><strong>First Time Buyer ISA from April 2029:</strong> it replaces the Lifetime ISA for new savers. Up to £4,000 a year, with a 25% bonus on the final balance, paid when you withdraw it to buy a home costing up to £450,000. Existing Lifetime ISAs carry on. {NLY} It needs new legislation before it starts.</li>
<li><strong>"Your First Home" scheme (England):</strong> 20% government equity loans with a five-year interest-free period, for about 70,000 buyers. Income caps: £110,000 outside London and £140,000 in London. {PLAN}</li>
</ul>
<p>See <a href="investments.html#isa">Lifetime ISAs</a> and <a href="mortgages.html">Mortgages</a>.</p>
{_bs("b26o","b26b")}

<h2 id="pensions">Pensioners and pension savers</h2>
<ul>
<li><strong>State Pension from April 2027:</strong> the full new State Pension rises 3.9% under the triple lock to <strong>£13,036.40 a year</strong>, about £488 a year more. DWP hasn't yet published the weekly rate. See <a href="pensions.html#state">State Pension</a>.</li>
<li><strong>Pension Tax Allowance, 6 April 2027 to 5 April 2030:</strong> people over State Pension age whose total income is up to £13,037 pay no income tax. It tapers away for incomes between £13,037 and £13,319. {NLY}</li>
<li><strong>Triple lock:</strong> the full triple lock stays until April 2029. From April 2030, the pension will rise by the highest of 2.5%, inflation, or the amount needed to keep its value against earnings at its April 2029 level. {PLAN}</li>
<li><strong>Unchanged:</strong> pensions still come into inheritance tax from April 2027 (only technical tweaks); annual allowance £60,000; MPAA £10,000; lump sum allowance £268,275; salary sacrifice £2,000 NI cap from April 2029.</li>
</ul>
{_bs("b26pta","b26bbc","b26b","b26a","b26o")}

<h2 id="home">Homeowners and energy</h2>
<ul>
<li><strong>£100 Household Energy Payment:</strong> for households in council tax bands A–D in England, paid into bank accounts from January 2027. The devolved governments get funding to do the same.</li>
<li><strong>0% VAT on household electricity</strong> extended to 30 June 2027 (it was due to end on 31 March 2027). HM Treasury expects this to take about £50 off the April 2027 price cap. The regulations are due in early 2027.</li>
<li><strong>Gas standing charges:</strong> Ofgem has been asked to abolish them and move the cost to unit rates, aiming for the end of 2027. The average gas standing charge is £108 a year. {PLAN}</li>
<li><strong>Hydrogen levy</strong> on gas bills scrapped.</li>
<li><strong>Energy-saving materials:</strong> VAT relief returns to 5% from 1 April 2027 as planned, and heat batteries are added to the relief.</li>
<li><strong>High Value Council Tax Surcharge</strong> on homes worth £2 million or more, from April 2028. {NLY}</li>
<li><strong>Unchanged:</strong> stamp duty residential rates; the £1,723 price cap for a typical household for October to December 2026.</li>
</ul>
<p>See <a href="energy.html#budget2026">Energy: Budget 2026 changes</a>.</p>
{_bs("b26p","b26b","b26o","b26a")}

<h2 id="families">Families and students</h2>
<ul>
<li><strong>Child Benefit:</strong> only an admin change. Overpayments can be offset against the High Income Child Benefit Charge.</li>
<li><strong>Student loans:</strong> no change to repayment thresholds. The Budget scorecard lists Plan 2 and Plan 3 interest capped at 6% from 1 September 2026 to 31 August 2027. See <a href="students.html#plan2">Plan 2 loans</a>.</li>
<li><strong>Young workers:</strong> minimum wage £11.27 an hour aged 18–20 and £8.31 aged 16–17 and apprentices, from 1 April 2027.</li>
<li><strong>Junior ISA:</strong> unchanged at £9,000 a year.</li>
</ul>
{_bs("b26o","b26b","b26a")}

<h2 id="drivers">Drivers</h2>
<ul>
<li><strong>Fuel duty:</strong> the 5p cut is extended to 30 June 2027, followed by an RPI-linked rise on 1 July 2027.</li>
<li><strong>Electric cars:</strong> pay-per-mile eVED (3p a mile for electric cars, 1.5p for plug-in hybrids) from 1 April 2028 is going into Finance Bill 2026-27. {NLY} See <a href="electric-cars.html#ved">Electric cars: tax</a>.</li>
<li><strong>Business mileage:</strong> 35p a mile above 10,000 business miles from 6 April 2027 (was 25p).</li>
</ul>
{_bs("b26o")}

<h2 id="dates">Key dates</h2>
<ol class="b26-tl">
<li><b>29 October 2026</b>Lifetime ISA charge 20% on first homes over £450,000.</li>
<li><b>November 2026</b>Regulations due to keep the £20,000 cash ISA limit for everyone.</li>
<li><b>January 2027</b>£100 Household Energy Payment starts (England, bands A–D).</li>
<li><b>1 April 2027</b>Minimum wage £13.21 / £11.27 / £8.31. VAT on energy-saving materials back to 5%, with heat batteries added.</li>
<li><b>April 2027</b>Full new State Pension £13,036.40 a year. Pensions come into inheritance tax (already planned; unchanged by the Budget).</li>
<li><b>6 April 2027</b>Savings tax 24% / 44% / 49%, trading allowance £3,000, Pension Tax Allowance, 35p mileage rate above 10,000 miles, business asset disposal relief limit £500,000 (Finance Bill items not law yet).</li>
<li><b>30 June / 1 July 2027</b>0% electricity VAT and the 5p fuel duty cut end on 30 June; fuel duty RPI rise on 1 July.</li>
<li><b>31 August 2027</b>End of the 6% Plan 2 / Plan 3 interest cap period listed in the Budget.</li>
<li><b>End of 2027</b>Aim for gas standing charges to be abolished.</li>
<li><b>April 2028</b>eVED pay-per-mile for electric cars (1 April) and the High Value Council Tax Surcharge.</li>
<li><b>April 2029</b>First Time Buyer ISA opens; salary sacrifice £2,000 NI cap; full triple lock runs to here.</li>
<li><b>April 2030</b>Adjusted triple lock starts; the Pension Tax Allowance ends on 5 April 2030.</li>
</ol>

<h2 id="notlaw">What's not law yet</h2>
<p>A Budget announces plans. Most still have to be passed by Parliament or set out in regulations, and details can change.</p>
<ul>
<li><strong>In Finance Bill 2026-27 (not law until it gets Royal Assent):</strong> savings income tax 24% / 44% / 49%; Pension Tax Allowance; trading allowance £3,000; High Value Council Tax Surcharge; eVED; founders' relief and business asset disposal relief changes.</li>
<li><strong>Due in regulations:</strong> keeping the £20,000 cash ISA limit (November 2026); 0% VAT on electricity to 30 June 2027 (early 2027).</li>
<li><strong>Needs new laws before launch:</strong> the First Time Buyer ISA (April 2029).</li>
<li><strong>Plans or aims without firm rules yet:</strong> abolishing gas standing charges (Ofgem, aiming for end of 2027); triple lock changes from April 2030; a new incentive for first-time stocks and shares ISA investors; the "Your First Home" scheme.</li>
<li><strong>Already in force:</strong> the 20% Lifetime ISA charge on homes over £450,000, from 29 October 2026.</li>
</ul>

<h2 id="sources">Sources</h2>
<p>All checked on 28 October 2026.</p>
<ul>{"".join(f'<li><a href="{S[k][1]}" rel="noopener">{S[k][0]}</a></li>' for k in ("b26o","b26a","b26b","b26p","b26pta","b26bbc","b26mse","b26w"))}</ul>
<p class="hint">Figures for the current tax year are on our <a href="money-matters-cheat-sheet.html">Money Matters cheat sheet</a>. Terms explained in the <a href="jargon.html">jargon buster</a>. This page is general information, not financial advice.</p>
</div><aside><div class="card toc"><h3>On this page</h3><a href="#sixty">In 60 seconds</a><a href="#workers">Workers</a><a href="#savers">Savers</a><a href="#investors">Investors</a><a href="#buyers">First-time buyers</a><a href="#pensions">Pensions</a><a href="#home">Homes and energy</a><a href="#families">Families and students</a><a href="#drivers">Drivers</a><a href="#dates">Key dates</a><a href="#notlaw">What's not law yet</a><a href="#sources">Sources</a></div></aside></div>''')
pages["budget-2026.html"] = page("budget-2026.html", "Budget 2026: what it means for you – MoneyBySharma",
 "What the UK Budget on 28 October 2026 changes for workers, savers, investors, first-time buyers, pensioners, households and drivers, with key dates and what's not law yet. Information, not advice.",
 _b26_body)
# ---------- homepage banner ----------
B26_BANNER = '''<style>
.b26-banner{display:block;margin:1.2rem 0 .4rem;background:#e7f2ef;border:1px solid #b9d8d0;border-left:5px solid #d9822b;border-radius:12px;padding:.9rem 1.1rem;text-decoration:none;color:#1d2b29}
.b26-banner:hover{border-color:#0f4c45;border-left-color:#d9822b}
.b26-banner .b26-k{display:block;font-size:.78rem;font-weight:700;letter-spacing:.03em;text-transform:uppercase;color:#8a4a0f}
.b26-banner .b26-h{display:block;font-family:Georgia,serif;font-size:1.3rem;color:#0f4c45;margin:.15rem 0 .25rem;line-height:1.25}
.b26-banner .b26-s{display:block;line-height:1.45}
.b26-banner .b26-go{display:inline-block;margin-top:.4rem;font-weight:700;color:#0f4c45;text-decoration:underline}
</style><div class="wrap"><a class="b26-banner" href="budget-2026.html"><span class="b26-k">Budget 2026 · 28 October 2026</span><span class="b26-h">Budget 2026: what it means for you</span><span class="b26-s">Cash ISAs stay at £20,000, tax on savings outside ISAs is due to rise from April 2027, and other changes, in plain English.</span><span class="b26-go">Read the summary</span></a></div>
'''
_b26mk = '<div class="wrap"><p class="x-invite">'
assert pages["index.html"].count(_b26mk) == 1, "home page marker for the Budget 2026 banner not found"
pages["index.html"] = pages["index.html"].replace(_b26mk, B26_BANNER + _b26mk)
