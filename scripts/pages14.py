# Gap pages from the Money Matters PDF audit: scams (G9) and pay/tax/payslip (G1). exec'd from build.py.
# Sources checked 17 October 2026 (see gap_common.py).
import math as _m
def _pay(sal, pct=5.0, scheme="ras", plan="p2"):
    SLT = {"none": 0, "p1": 2241.66, "p2": 2448.75, "p4": 2816.25, "p5": 2083.33, "pg": 1750}; SLR = {"pg": .06}
    m = sal / 12; qual = max(0, min(sal, 50270) - 6240); empg = pct / 100 * qual / 12; pen = empg * 12
    ani = sal - (pen if scheme == "net" else 0); pa = max(0, 12570 - max(0, ani - 100000) / 2); ti = max(0, ani - pa)
    tax = (.2 * min(ti, 37700) + .4 * max(0, min(ti, 125140) - 37700) + .45 * max(0, ti - 125140)) / 12
    ni = .08 * (min(max(m, 1048), 4189) - 1048) + .02 * max(0, m - 4189)
    sl = _m.floor((m - SLT[plan]) * SLR.get(plan, .09)) if plan != "none" and m > SLT[plan] else 0
    pd = empg if scheme == "net" else empg * .8
    return dict(m=m, tax=tax, ni=ni, sl=sl, pen=pd, net=m - tax - ni - sl - pd, ptot=empg + .03 * qual / 12)
EX = _pay(30000)
def _g(x): return f"£{x:,.2f}"

# ---------------- G9: Scams and fraud ----------------
pages["scams-fraud.html"] = page("scams-fraud.html", "Scams and fraud: warning signs, who to call and your protections – MoneyBySharma",
 "How to spot common UK money scams, the numbers to call and report to (159, 7726, Report Fraud), and what protections exist if you're tricked into a bank transfer.",
 ph("Scams &amp; fraud","Scams and fraud","The warning signs, what to do straight away, who to report to, and the protections that exist if you're tricked into paying. Information only – not advice."), W(f'''
<div class="cols"><div>
<div class="note" style="margin-top:1.5rem"><strong>Information only – not advice.</strong> This page summarises guidance from the FCA, the police-run Report Fraud service, the Payment Systems Regulator and others. It can't tell you whether a particular message or offer is genuine. Links to official pages are at the bottom of each section.</div>
<div class="note" role="note" style="border-left-color:#b3261e"><strong>Just paid or shared your details?</strong> Contact your bank straight away on a number you trust – the one on the back of your card or on your statement, or call <strong>159</strong> (works if your bank and phone network have joined; if it doesn't connect, use the card number). Then report it (see <a href="#report">who to report to</a>).</div>

<h2 id="flags">Warning signs</h2>
<p>Scams can be hard to spot: fraudsters can be convincing and knowledgeable, with websites and materials that look identical to the real thing. The FCA suggests asking yourself these questions about any unexpected contact. A "yes" to any of them is a reason to stop and check.</p>
<ul><li><strong>Is it unexpected?</strong> Scammers often call out of the blue, or use email, text, post, social media or even visit in person.</li>
<li><strong>Are you being rushed?</strong> A bonus, discount or "limited time" is a common way to hurry you.</li>
<li><strong>Does it sound too good to be true?</strong> High returns are a typical lure.</li>
<li><strong>Are you told it's exclusive or secret?</strong> "You've been specially chosen" is a warning sign.</li>
<li><strong>Are they flattering you or building a friendship?</strong></li>
<li><strong>Are you feeling worried or excited?</strong> Scammers try to work on your emotions.</li>
<li><strong>Do they speak with authority?</strong> Claiming to be authorised, and sounding knowledgeable, proves nothing.</li></ul>
<p>The FCA also says: don't give out bank or card details unless you're certain who you're dealing with, don't share passwords with anyone, and don't download software or an app from a source you don't trust, as scammers may be able to take control of your device. A genuine bank or business won't mind waiting if you want time to think.</p>
{sg("fcascam","stfraud")}

<h2 id="steps">Stop, check, report</h2>
<div class="steps3"><div><h3>1. Stop</h3><p>Don't reply, click links, open attachments or pay. If a call or message pressures you, hang up or ignore it.</p></div>
<div><h3>2. Check</h3><p>Hang up and ring your bank on a number you trust, or <strong>159</strong>. For any firm offering a financial product, look it up on the <a href="https://www.fca.org.uk/consumers/fca-firm-checker" rel="noopener">FCA Firm Checker</a> and use the contact details listed there, not the ones you were given.</p></div>
<div><h3>3. Report</h3><p>Tell your bank, then report the scam (numbers below). Reporting helps others, and your bank may need the details.</p></div></div>
<p><strong>About 159.</strong> It is run by Stop Scams UK. It connects you to your bank's genuine customer service line if your bank is signed up – a long list of banks and building societies has joined, but not every bank is on it. 159 will <em>never</em> call you: anyone ringing and saying they're from 159 is a scammer. Check Stop Scams UK's page for the current list of banks.</p>
{sg("s159","fcacheck")}

<h2 id="common">Common scams</h2>
<div class="table-scroll"><table class="wrap-th"><caption class="sr">Common scams and what to do</caption><thead><tr><th scope="col">Scam</th><th scope="col">How it often works</th><th scope="col">What official sources say</th></tr></thead><tbody>
<tr><th scope="row">Fake bank or "fraud team" call</th><td>Someone claims to be your bank (or police, HMRC) and says your money is at risk, then asks you to move it or share codes.</td><td>Hang up and call your bank on a trusted number or 159. Contact your bank immediately if you've paid or shared details.</td></tr>
<tr><th scope="row">Phishing texts and emails</th><td>A message pretending to be a bank, delivery firm or government body with a link to a fake site.</td><td>Forward scam texts to <strong>7726</strong> (free) and suspicious emails to <strong>report@phishing.gov.uk</strong>.</td></tr>
<tr><th scope="row">Investment and crypto scams</th><td>Promises of high or guaranteed returns, often through social media or a "friend" you've only met online.</td><td>Check the firm on the FCA Firm Checker. The FCA also warns that products it doesn't regulate come with no protection if something goes wrong.</td></tr>
<tr><th scope="row">Pension scams</th><td>Cold calls or "free pension reviews", offers to release money before age 55, or unusual overseas investments.</td><td>See <a href="#pensions">pension scams</a> below.</td></tr>
<tr><th scope="row">Upfront fee scams</th><td>You're asked to pay a fee in advance after an offer of a loan, a job or a prize.</td><td>The FCA says if you pay a fee in advance you will probably never hear from the fraudsters again.</td></tr>
<tr><th scope="row">Screen-sharing and remote access</th><td>You're talked into installing software that lets someone see or control your device.</td><td>Don't give access to your device to anyone you don't trust (FCA).</td></tr>
<tr><th scope="row">Money mule offers</th><td>"Easy money" for letting someone use your account.</td><td>See <a href="#mules">money mules</a> below.</td></tr></tbody></table></div>
{sg("fcascam","fcamule","phish")}

<h2 id="report">Who to report to</h2>
<div class="table-scroll"><table class="contacts"><caption class="sr">Where to report scams</caption><thead><tr><th scope="col">What</th><th scope="col">Where</th></tr></thead><tbody>
<tr><th scope="row">You've paid or shared details</th><td>Your bank, straight away – card/statement number, or <strong>159</strong></td></tr>
<tr><th scope="row">Fraud or cyber crime (England, Wales, Northern Ireland)</th><td><a href="https://www.reportfraud.police.uk/" rel="noopener">Report Fraud</a>: <strong>0300 123 2040</strong></td></tr>
<tr><th scope="row">Fraud in Scotland</th><td>Police Scotland: <strong>101</strong></td></tr>
<tr><th scope="row">Scam text message</th><td>Forward it to <strong>7726</strong> (free). Your mobile provider can investigate and block the sender.</td></tr>
<tr><th scope="row">Scam email</th><td>Forward to <strong>report@phishing.gov.uk</strong> (National Cyber Security Centre)</td></tr>
<tr><th scope="row">A firm that may be impersonating a regulated firm, or a financial scam</th><td>FCA consumer helpline: <strong>0800 111 6768</strong></td></tr>
<tr><th scope="row">Emergency or in immediate danger</th><td><strong>999</strong></td></tr></tbody></table></div>
{sg("reportfraud","phish","fcascam","ncamule")}

<h2 id="app">Tricked into a bank transfer: what protection exists?</h2>
<p>If you were tricked into sending money by bank transfer – an <strong>authorised push payment (APP) scam</strong> – the Payment Systems Regulator's rules usually require your bank to reimburse you, if the payment was a UK Faster Payments or CHAPS transfer made on or after <strong>7 October 2024</strong>. In summary:</p>
<ul><li><strong>Limit:</strong> up to <strong>£85,000 per claim</strong>. Firms may choose to pay more. If you lose more than that and aren't reimbursed, you can raise the case with the Financial Ombudsman Service.</li>
<li><strong>Time to report:</strong> as soon as possible and within <strong>13 months</strong> of the payment.</li>
<li><strong>Speed:</strong> you can expect an answer within 5 business days of claiming. If the firm needs more time to gather information, it must reach an outcome within 35 business days.</li>
<li><strong>Excess:</strong> firms may apply an optional excess of up to £100 (not to vulnerable customers).</li>
<li><strong>Who's covered:</strong> individuals, microenterprises and charities, for payments between UK accounts. Credit unions, municipal banks and National Savings banks aren't part of the arrangements.</li>
<li><strong>Not covered:</strong> you won't be reimbursed if you were complicit in the fraud or grossly negligent (a high bar, which doesn't apply to vulnerable customers). Card, cash and cheque payments have their own protections, and civil disputes (for example goods that never arrived from a genuine seller) are handled differently.</li></ul>
<div class="flag"><strong>May change:</strong> the PSR's independent review reported in July 2026 and it has said it will consult on changes from December 2026, including the treatment of some investment scams and the 13-month reporting limit. The £85,000 limit and the other details above were the published position on {CG}. Check the official page for the current rules.</div>
{sg("psrapp","psrroad","stfraud")}

<h2 id="pensions">Pension scams</h2>
<p>The FCA's warning signs include a guaranteed better return on your pension savings, high-pressure sales tactics, unusual and unregulated investments, complicated structures, and several firms each taking a fee.</p>
<ul><li><strong>Cold calls about your pension are illegal</strong> and probably a scam. The FCA says the safest thing is to hang up. Ignore offers by email or text. You can report pension cold calls to the Information Commissioner's Office (ICO).</li>
<li><strong>Offers to release money before age 55</strong> ("pension liberation" or "pension loans") are almost certainly scams. The FCA says you could also face a tax bill of 55% on what you withdraw. The normal minimum pension age is 55, rising to 57 from 2028 (see <a href="pensions.html">Pensions</a>).</li>
<li><strong>"Free pension reviews"</strong> from people who contact you unexpectedly are likely to be scams. Professional advice isn't free, and some scammers claim to act for the FCA or MoneyHelper.</li>
<li>If you want advice, use someone authorised by the FCA, and never take advice from a company that contacted you out of the blue.</li></ul>
{sg("fcapen")}

<h2 id="mules">Money mules</h2>
<p>A <strong>money mule</strong> is someone who moves criminal money for others – by letting them use your bank account, buying or selling cryptocurrency for them, or withdrawing cash to hand over – sometimes for a payment. The National Crime Agency says students are often targeted with "quick money" offers through social media job posts, direct approaches and gaming chats.</p>
<p>It is a crime. Consequences listed by the NCA include up to <strong>14 years in prison</strong>, bank accounts closed, and difficulty getting loans, phone contracts, credit cards or mortgages later. The FCA adds that you may also find it hard to access banking services or credit in future. If someone asks to "borrow" your account, ask someone you trust first, and report recruiters to the police on 101 or anonymously to Crimestoppers (0800 555 111).</p>
{sg("ncamule","fcamule")}

<h2 id="id">Identity theft</h2>
<p>If someone may have used your details, tell your bank and report to Report Fraud. Checking your credit file is a good way to spot accounts you didn't open – see <a href="credit-scores-debt-help.html#file">credit files and credit scores</a> for how to check yours free, and how to put mistakes right. The FCA also says to check your bank and card statements regularly, and to be extra careful after a scam: fraudsters can target you again, for example with offers to recover your money for a fee ("recovery room" scams).</p>
{sg("fcascam","reportfraud")}
</div><aside><div class="card toc"><h3>On this page</h3><a href="#flags">Warning signs</a><a href="#steps">Stop, check, report</a><a href="#common">Common scams</a><a href="#report">Who to report to</a><a href="#app">Bank transfer protection</a><a href="#pensions">Pension scams</a><a href="#mules">Money mules</a><a href="#id">Identity theft</a><p class="hint" style="margin:.8rem 0 .2rem">Related</p><a href="bank-accounts.html">Bank accounts</a><a href="pensions.html">Pensions</a><a href="jargon.html">Jargon buster</a></div></aside></div>'''))

# ---------------- G1: Pay, tax and your payslip ----------------
_rows = [("Gross pay", _g(EX["m"]), ""), ("Income Tax", "−" + _g(EX["tax"]), ""), ("National Insurance", "−" + _g(EX["ni"]), ""),
         ("Pension (your share, after relief)", "−" + _g(EX["pen"]), ""), ("Student loan (Plan 2)", "−" + _g(EX["sl"]), "")]
_ex = "".join(f'<tr><th scope="row">{a}</th><td class="num">{b}</td></tr>' for a, b, c in _rows) + f'<tr class="tot"><th scope="row">Take-home pay (net)</th><td class="num">{_g(EX["net"])}</td></tr>'
pages["pay-tax-payslip.html"] = page("pay-tax-payslip.html", "Pay, tax and your payslip: tax code, National Insurance and take-home pay – MoneyBySharma",
 "How a UK payslip works in 2026/27: gross and net pay, tax codes, Income Tax bands, National Insurance, pension and student loan deductions, minimum wage, P45 and P60, with a take-home pay calculator.",
 ph("Pay, tax &amp; your payslip","Pay, tax and your payslip","What each line on a UK payslip means, how tax codes and National Insurance work, and what you take home – with an illustration you can try yourself. 2026/27, information only."), W(f'''
<div class="cols"><div>
<div class="note" style="margin-top:1.5rem"><strong>Information only – not advice or a payroll service.</strong> The calculator is an illustration using the published 2026/27 rates for England, Wales and Northern Ireland. Your payslip is the record that counts; if something looks wrong, ask your employer or HMRC.</div>

<h2 id="payslip">Reading your payslip</h2>
<p>Your employer must give you a payslip on or before payday. It must show your <strong>gross pay</strong> (before deductions), any deductions that can change from one payday to the next (such as tax and National Insurance), and your <strong>net pay</strong> (what you receive). If your pay varies with the hours you work, it must also show the hours paid for. Fixed deductions can be explained on the payslip or in a separate written statement.</p>
<table class="wrap-th"><caption class="sr">Lines on a typical payslip</caption><thead><tr><th scope="col">Line</th><th scope="col">What it means</th></tr></thead><tbody>
<tr><th scope="row">Gross pay</th><td>Your pay before anything is taken off, including bonuses and overtime.</td></tr>
<tr><th scope="row">Income Tax (PAYE)</th><td>Tax taken by your employer on HMRC's behalf, worked out from your <a href="#code">tax code</a>.</td></tr>
<tr><th scope="row">National Insurance</th><td>A separate contribution on earnings that builds State Pension and benefit entitlement – see <a href="#ni">below</a>.</td></tr>
<tr><th scope="row">Pension</th><td>Your contribution to a workplace pension, if you're in one – see <a href="#deductions">pension and student loan</a>.</td></tr>
<tr><th scope="row">Student loan</th><td>Repayments taken from pay once you earn over your plan's threshold.</td></tr>
<tr><th scope="row">Net pay</th><td>Gross pay minus all deductions: the amount paid into your bank.</td></tr></tbody></table>
{sg("payslip")}

<h2 id="code">Tax codes</h2>
<p>Your <strong>tax code</strong> tells your employer how much tax-free pay to give you. <strong>1257L</strong> is the code used for most people with one job or pension. The numbers show your tax-free amount for the year (1257 stands for the £12,570 Personal Allowance); the letter shows your situation. HMRC starts with your Personal Allowance and takes off things like untaxed income and some company benefits. GOV.UK's example: a £1,570 medical insurance benefit from an employer leaves £11,000 tax-free, giving code 1100L.</p>
<ul><li><strong>L:</strong> you're entitled to the standard Personal Allowance. <strong>S</strong> and <strong>C</strong> prefixes show Scottish and Welsh tax rates.</li>
<li><strong>BR, D0, D1:</strong> all income from that job is taxed at one rate (usually used for a second job or pension).</li>
<li><strong>0T:</strong> your Personal Allowance has been used up, or your employer doesn't have the details to give you a code.</li>
<li><strong>M1, W1, X, NONCUM</strong> are emergency tax codes: you may pay the wrong amount until HMRC has your details.</li></ul>
<p>GOV.UK says it's your responsibility to make sure you're paying the right amount of tax. It has a tool to check what your code means, and a page on what to do if you think your code is wrong. You'll be sent a P45 when you leave a job and your new employer uses it to work out your tax.</p>
{sg("taxcode")}

<h2 id="tax">Income Tax: the stairs</h2>
<p>Income Tax works like stairs: each rate applies only to the pounds <em>inside</em> its band. In England, Wales and Northern Ireland for 2026/27:</p>
<table class="wrap-th"><caption class="sr">Income Tax bands 2026/27</caption><thead><tr><th scope="col">Band</th><th scope="col">Income</th><th scope="col">Rate</th></tr></thead><tbody>
<tr><th scope="row">Personal Allowance</th><td>Up to £12,570</td><td>0%</td></tr><tr><th scope="row">Basic rate</th><td>£12,571 to £50,270</td><td>20%</td></tr>
<tr><th scope="row">Higher rate</th><td>£50,271 to £125,140</td><td>40%</td></tr><tr><th scope="row">Additional rate</th><td>Over £125,140</td><td>45%</td></tr></tbody></table>
<p>The Personal Allowance is reduced by £1 for every £2 of income over £100,000, and is zero from £125,140. <strong>Illustration:</strong> someone earning £50,270 pays (£50,270 − £12,570) × 20% = £7,540. If they earn £1,000 more, only that extra £1,000 is taxed at 40% – an extra £400 – so the bill is £7,940, not 40% of everything. Scotland has its own bands (see <a href="https://www.gov.uk/scottish-income-tax" rel="noopener">GOV.UK: Scottish Income Tax</a>). The <a href="resources.html">cheat sheet</a> has these figures in one place.</p>
{sg("itrates")}

<h2 id="ni">National Insurance</h2>
<p><strong>National Insurance (NI)</strong> is separate from Income Tax. It is how you build up entitlement to the State Pension and some benefits (see <a href="pensions.html">Pensions</a>). For most employees in 2026/27 (category letter A):</p>
<table class="wrap-th"><caption class="sr">Employee National Insurance 2026/27</caption><thead><tr><th scope="col">Your pay</th><th scope="col">Rate</th></tr></thead><tbody>
<tr><td>Up to £242 a week (£1,048 a month)</td><td>0%</td></tr><tr><td>£242.01 to £967 a week (£1,048.01 to £4,189 a month)</td><td>8%</td></tr><tr><td>Over £967 a week (over £4,189 a month)</td><td>2%</td></tr></tbody></table>
<p>Employers pay NI too, at <strong>15%</strong> on pay above £96 a week (£417 a month) for most employees. Some categories (for example, apprentices under 25, under-21s and veterans) have different employer thresholds. <strong>Self-employed people</strong> pay Class 4 NI of 6% on profits between £12,570 and £50,270 and 2% above that. They don't have to pay Class 2 if profits are £7,105 or more (it's treated as paid); below that they can choose to pay voluntary Class 2 at £3.65 a week.</p>
{sg("ni","nirates","niemp","nise")}

<h2 id="minwage">Minimum wage</h2>
<p>From <strong>1 April 2026</strong> the legal minimum hourly rates are:</p>
<table class="wrap-th"><caption class="sr">Minimum wage rates from April 2026</caption><thead><tr><th scope="col">Age</th><th scope="col">Hourly rate</th></tr></thead><tbody><tr><td>21 and over (National Living Wage)</td><td>£12.71</td></tr><tr><td>18 to 20</td><td>£10.85</td></tr><tr><td>Under 18</td><td>£8.00</td></tr><tr><td>Apprentice (aged under 19, or 19 and over in the first year of the apprenticeship)</td><td>£8.00</td></tr></tbody></table>
<p class="hint">The rates change each April. Apprentices aged 19 or over who have finished their first year get the minimum wage for their age.</p>
{sg("nmw")}

<h2 id="deductions">Pension and student loan on your payslip</h2>
<h3>Workplace pension</h3>
<p>Under automatic enrolment, if you're eligible your employer must put you in a workplace pension. The legal minimum is 8% in total of your "qualifying earnings" (the slice of pay between £6,240 and £50,270 in 2026/27), of which at least 3% comes from your employer. Many employers pay more. How your contribution is taken affects your payslip:</p>
<ul><li><strong>Relief at source:</strong> you pay from pay that's already been taxed and the provider claims 20% basic-rate relief, so £80 from you becomes £100 in the pot.</li><li><strong>Net pay arrangement:</strong> your contribution comes out <em>before</em> tax, so you get relief straight away at your rate.</li></ul>
<p>See <a href="pensions.html">Pensions</a> and <a href="investments.html#sipp">tax relief</a> for more.</p>
<h3>Student loan</h3>
<p>Repayments come out of your gross pay once it passes the threshold for your plan: <strong>9%</strong> of the amount over the threshold for Plans 1, 2, 4 and 5, or <strong>6%</strong> for a Postgraduate Loan. Employers calculate it each pay period and round down to the nearest pound.</p>
<table class="wrap-th"><caption class="sr">Student loan thresholds 2026/27</caption><thead><tr><th scope="col">Plan</th><th scope="col">Yearly</th><th scope="col">Monthly</th><th scope="col">Rate</th></tr></thead><tbody>
<tr><td>Plan 1</td><td>£26,900</td><td>£2,241</td><td>9%</td></tr><tr><td>Plan 2</td><td>£29,385</td><td>£2,448</td><td>9%</td></tr><tr><td>Plan 4 (Scotland)</td><td>£33,795</td><td>£2,816</td><td>9%</td></tr><tr><td>Plan 5</td><td>£25,000</td><td>£2,083</td><td>9%</td></tr><tr><td>Postgraduate Loan</td><td>£21,000</td><td>£1,750</td><td>6%</td></tr></tbody></table>
<p class="hint">GOV.UK's monthly figures are rounded down; employers use the exact pay-period thresholds (for example £2,448.75 for Plan 2). The amount you owe doesn't change what you repay each month.</p>
{sg("aemin","ae","slrepay","slemp")}

<h2 id="calc">Take-home pay: an illustration</h2>
<p>This is a worked example, not your payslip. <strong>Illustration:</strong> a £30,000 salary, paid monthly, with the standard 1257L code, a 5% employee pension contribution under relief at source (3% from the employer) and a Plan 2 student loan:</p>
<div class="table-scroll"><table class="pay-tbl"><caption class="sr">Monthly payslip, £30,000 salary (illustration)</caption><thead><tr><th scope="col">Line</th><th scope="col" class="num">Per month</th></tr></thead><tbody>{_ex}</tbody></table></div>
<p class="hint">Tax: (£30,000 − £12,570) × 20% ÷ 12. NI: (£2,500 − £1,048) × 8%. Pension: 5% of qualifying earnings (£30,000 − £6,240) ÷ 12 = £99.00 gross, £79.20 after 20% relief; the employer adds 3% (£59.40). Student loan: (£2,500 − £2,448.75) × 9% = £4.61, rounded down to £4.</p>
<section class="calc" id="takehome" aria-labelledby="tp-h"><h3 id="tp-h" style="margin-top:0">Take-home pay calculator</h3>
<form id="tp-form" class="fields" novalidate><div><label for="tp-sal">Yearly gross salary (£)</label><input id="tp-sal" type="number" value="30000" min="0" step="500" inputmode="decimal"></div>
<div><label for="tp-pen">Your pension contribution (% of qualifying earnings)</label><input id="tp-pen" type="number" value="5" min="0" max="100" step="0.5" inputmode="decimal"></div>
<div><label for="tp-scheme">How your pension is taken</label><select id="tp-scheme"><option value="ras">Relief at source (after tax)</option><option value="net">Net pay (before tax)</option></select></div>
<div><label for="tp-plan">Student loan</label><select id="tp-plan"><option value="none">None</option><option value="p1">Plan 1</option><option value="p2" selected>Plan 2</option><option value="p4">Plan 4</option><option value="p5">Plan 5</option><option value="pg">Postgraduate Loan</option></select></div>
<div style="grid-column:1/-1"><table class="pay-tbl" aria-live="polite"><caption class="sr">Calculated monthly payslip</caption><tbody>
<tr><th scope="row">Gross pay</th><td class="num" id="tp-gross">–</td></tr><tr><th scope="row">Income Tax</th><td class="num" id="tp-tax">–</td></tr><tr><th scope="row">National Insurance</th><td class="num" id="tp-ni">–</td></tr>
<tr><th scope="row">Pension (your share, from pay)</th><td class="num" id="tp-pen-o">–</td></tr><tr><th scope="row">Student loan</th><td class="num" id="tp-sl">–</td></tr>
<tr class="tot"><th scope="row">Take-home pay per month</th><td class="num" id="tp-net">–</td></tr></tbody></table></div>
<div style="grid-column:1/-1" class="results" aria-live="polite"><div class="res"><span>Take-home per year (×12)</span><b id="tp-year">–</b></div><div class="res"><span>Total into pension each month (you + 3% employer + relief)</span><b id="tp-ptot">–</b></div></div>
<p class="hint" style="grid-column:1/-1">Assumes: England, Wales or Northern Ireland tax bands; code 1257L with no other income, benefits or allowances; steady monthly pay for the whole year; NI category A; you're in the pension scheme and the employer pays 3% of qualifying earnings. Doesn't include higher-rate pension relief claimed through a tax return, salary sacrifice, Scottish rates or tax-year part-years. Not advice.</p></form></section>

<h2 id="forms">P45, P60 and P11D</h2>
<ul><li><strong>P45:</strong> given to you when you leave a job. It shows your pay, tax and tax code from 6 April to your leaving date. Your new employer uses it to work out your tax.</li><li><strong>P60:</strong> a summary of your pay and tax for the whole tax year (6 April to 5 April) from each employer you were working for on 5 April. Employers must provide it by 31 May.</li><li><strong>P11D:</strong> a form your employer files with HMRC if you receive taxable benefits (see <a href="electric-cars.html">company car tax</a>).</li></ul>
{sg("p45")}

<h2 id="side">Side income and Self Assessment</h2>
<p>If you earn money outside your payslip, such as freelance work, you may not pay tax on small amounts thanks to the <strong>trading allowance</strong>: <strong>£1,000</strong> of gross income a tax year from self-employment, casual services (for example babysitting or gardening) or hiring out personal equipment. It's one £1,000 allowance across all of your side income, not £1,000 per activity, and it's measured on income before expenses, not profit.</p>
<ul><li>If your gross trading income is £1,000 or less you generally don't need to tell HMRC.</li><li>If it's more than £1,000 you must register for <strong>Self Assessment</strong> by 5 October following the end of the tax year, and file a tax return. You can then either deduct the £1,000 allowance or deduct your actual expenses – not both.</li><li>Class 2 and Class 4 NI for the self-employed are usually paid through Self Assessment (see <a href="#ni">National Insurance</a>). Student loan repayments on self-employed income are worked out from your return, too.</li></ul>
<p class="hint">GOV.UK says a new online reporting tool is planned for people with side income between £1,000 and £3,000, but until it's live you still need to use Self Assessment. Check GOV.UK for the current position.</p>
{sg("trading","sa","slrepay")}
</div><aside><div class="card toc"><h3>On this page</h3><a href="#payslip">Reading your payslip</a><a href="#code">Tax codes</a><a href="#tax">Income Tax</a><a href="#ni">National Insurance</a><a href="#minwage">Minimum wage</a><a href="#deductions">Pension and student loan</a><a href="#calc">Take-home pay</a><a href="#forms">P45 and P60</a><a href="#side">Side income</a><p class="hint" style="margin:.8rem 0 .2rem">Related</p><a href="students.html">Students</a><a href="pensions.html">Pensions</a><a href="resources.html">Cheat sheet</a></div></aside></div>''', ), scripts=("calc-ui7.js",))
