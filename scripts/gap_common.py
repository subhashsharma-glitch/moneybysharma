# Shared pieces for the "Money Matters PDF gap" pages (exec'd early from build.py).
# Sources here were checked on 17 October 2026.
import math
CG = "17 October 2026"
SG = {
 "ni": ("GOV.UK – National Insurance: how much you pay", "https://www.gov.uk/national-insurance/how-much-you-pay"),
 "nirates": ("GOV.UK – National Insurance rates and categories", "https://www.gov.uk/national-insurance-rates-letters"),
 "niemp": ("GOV.UK – Rates and thresholds for employers 2026 to 2027", "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027"),
 "nise": ("GOV.UK – Self-employed National Insurance rates", "https://www.gov.uk/self-employed-national-insurance-rates"),
 "trading": ("GOV.UK – Tax-free allowances on property and trading income", "https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income"),
 "taxcode": ("GOV.UK – Tax codes: what your tax code means", "https://www.gov.uk/tax-codes/what-your-tax-code-means"),
 "payslip": ("GOV.UK – Payslips: employee rights", "https://www.gov.uk/payslips"),
 "p45": ("GOV.UK – Your P45, P60 and P11D forms", "https://www.gov.uk/paye-forms-p45-p60-p11d"),
 "nmw": ("GOV.UK – National Minimum Wage and National Living Wage rates", "https://www.gov.uk/national-minimum-wage-rates"),
 "itrates": ("GOV.UK – Income Tax rates and Personal Allowances", "https://www.gov.uk/income-tax-rates"),
 "slrepay": ("GOV.UK – Repaying your student loan: how much you repay", "https://www.gov.uk/repaying-your-student-loan/what-you-pay"),
 "slemp": ("GOV.UK – 2026 to 2027: Student and Postgraduate Loan deduction tables", "https://www.gov.uk/government/publications/sl3-student-loan-deduction-tables/2026-to-2027-student-and-postgraduate-loan-deduction-tables"),
 "sa": ("GOV.UK – Self Assessment tax returns", "https://www.gov.uk/self-assessment-tax-returns"),
 "reportfraud": ("Report Fraud (police) – report cyber crime and fraud", "https://www.reportfraud.police.uk/"),
 "s159": ("Stop Scams UK – Stop, hang up, call 159", "https://stopscamsuk.org.uk/campaign/get-help-now/"),
 "phish": ("GOV.UK – Report suspicious emails, texts and websites", "https://www.gov.uk/report-suspicious-emails-websites-phishing"),
 "fcascam": ("FCA – Protect yourself from scams", "https://www.fca.org.uk/consumers/protect-yourself-scams"),
 "fcacheck": ("FCA – How to check a firm or individual is authorised", "https://www.fca.org.uk/consumers/how-check-firm-individual-authorised"),
 "fcapen": ("FCA – Pension scams", "https://www.fca.org.uk/scamsmart/how-avoid-pension-scams"),
 "fcamule": ("FCA – Money transfer scams", "https://www.fca.org.uk/consumers/money-transfer-scams"),
 "ncamule": ("National Crime Agency – Money mules", "https://www.nationalcrimeagency.gov.uk/moneymuling"),
 "psrapp": ("Payment Systems Regulator – APP fraud reimbursement protections", "https://www.psr.org.uk/information-for-consumers/app-fraud-reimbursement-protections/"),
 "psrroad": ("Payment Systems Regulator – APP scams policy roadmap", "https://www.psr.org.uk/our-work/app-scams/app-scams-policy-roadmap/"),
 "stfraud": ("Stop! Think Fraud (GOV.UK campaign)", "https://stopthinkfraud.campaign.gov.uk/"),
}
S.update(SG)
def sg(*keys):
    return '<p class="src">Sources (checked ' + CG + '): ' + "; ".join(f'<a href="{S[k][1]}" rel="noopener">{S[k][0]}</a>' for k in keys) + ".</p>"

GAP_JARGON = [
 ("Rule of 72", "A rule of thumb: divide 72 by a yearly growth rate to estimate how many years it takes money to double. At 4% it gives about 18 years. It's an estimate, not an exact figure, and ignores tax, fees and changing rates."),
 ("Simple interest", "Interest paid only on the original amount, not on interest already added. £1,000 at 4% simple interest earns £40 a year."),
 ("Phishing", "A scam message, email, text or call pretending to be from a trusted organisation to steal your details or money. Forward scam texts to 7726 and scam emails to report@phishing.gov.uk."),
 ("Money mule", "Someone who lets criminals move money through their bank account, sometimes for a payment. It's a crime and can mean up to 14 years in prison."),
 ("Authorised push payment (APP) scam", "When you're tricked into sending a bank transfer to a fraudster. Since 7 October 2024, banks must usually reimburse eligible UK Faster Payments and CHAPS victims up to £85,000 per claim."),
 ("Confirmation of Payee", "An account name-checking service shown before some bank transfers, designed to help make sure you're paying the right person or business. Pay attention to any warning."),
 ("National Insurance", "A tax on earnings and self-employed profits that also builds your entitlement to the State Pension and some benefits. For most employees in 2026/27 it's 8% of pay between £1,048 and £4,189 a month, then 2% above."),
 ("Tax code", "Letters and numbers HMRC gives your employer to work out how much tax-free pay you get. 1257L is the standard code for most people with one job: the 1257 stands for the £12,570 Personal Allowance."),
 ("P45 / P60", "A P45 is the form you get when you leave a job. A P60 is your end-of-year summary of pay and tax from an employer, due by 31 May."),
 ("National Living Wage", "The legal minimum hourly pay for workers aged 21 and over: £12.71 from 1 April 2026."),
 ("Self Assessment", "The way you report income that isn't taxed through your payslip, such as self-employed profits, by filing a tax return with HMRC."),
 ("Trading allowance", "£1,000 a year of tax-free income from self-employment or casual work. It's one allowance across all your side income. Above £1,000 you usually need to tell HMRC."),
 ("Payslip", "The statement your employer must give you on or before payday. It shows gross pay, deductions that vary (such as tax and National Insurance) and net pay."),
 ("PAYE", "Pay As You Earn: the system your employer uses to take Income Tax and National Insurance from your pay before you receive it."),
 ("APR", "Annual percentage rate: a yearly rate of the cost of borrowing, including interest and certain compulsory charges, so you can compare credit. See also representative APR."),
 ("Representative APR", "The rate a lender expects to offer to at least 51% of the people accepted for a product after an advert. Up to 49% can be offered a higher rate, so your own APR may differ."),
 ("Payday loan (high-cost short-term credit)", "A small, short-term loan with a high cost. FCA rules cap interest and fees at 0.8% a day of the amount borrowed, default charges at £15, and total charges at 100% of the amount borrowed."),
 ("Loan shark", "An illegal moneylender, often charging very high interest. Report one anonymously: Stop Loan Sharks (England) 0300 555 2222; Wales 0300 123 3311; Scotland 0800 074 0878; Northern Ireland Consumerline 0300 123 6262."),
 ("Buy now, pay later (BNPL)", "Splitting a purchase into instalments. Interest-free \"deferred payment credit\" from a lender that is a different business from the seller has been regulated by the FCA since 15 July 2026, and Section 75 now applies to those agreements."),
 ("Direct Debit Guarantee", "Protection for every Direct Debit: if the organisation or your bank makes an error, you're entitled to a full and immediate refund from your bank or building society."),
 ("Emergency fund", "Money kept in an instant-access account for the unexpected. MoneyHelper's rule of thumb is three to six months' essential outgoings."),
 ("Excess", "The amount you pay yourself when you make an insurance claim. A voluntary excess can lower your premium but means you get less back when you claim."),
 ("Premium", "What you pay for insurance cover, monthly or yearly."),
 ("Third-party insurance", "The legal minimum motor insurance in the UK. It covers injury or damage you cause to others, but not damage to your own vehicle."),
 ("Pension Tracing Service", "A free GOV.UK service for finding contact details of a lost workplace or personal pension. It needs an employer or provider name and won't tell you whether you have a pension or its value."),
 ("Plan 2 student loan", "A student loan for English students who started between 1 September 2012 and 31 July 2023 (and Welsh students from 1 September 2012). You repay 9% of income over £29,385, and any balance is written off after 30 years."),
 ("Diversification", "Spreading your money across different investments to lower the risk that one going wrong hurts you badly. It reduces risk but doesn't remove it."),
 ("Cooling-off period", "A short window to cancel after buying. For example, you can usually cancel an online purchase within 14 days of receiving it, and MoneyHelper says you have 30 days to cancel life or income protection insurance for a full refund."),
]

# ---------- G3: How interest grows (Savings) ----------
def _gbp(x, dp=2): return f"£{x:,.{dp}f}"
def grow_section():
    yrs = [0, 2, 4, 6, 8, 10]
    simple = [1000 + 40 * y for y in yrs]
    comp = [1000 * 1.04 ** y for y in yrs]
    rows = "".join(f"<tr><th scope=\"row\">{y}</th><td>{_gbp(s,0)}</td><td>{_gbp(c)}</td></tr>" for y, s, c in zip(yrs, simple, comp))
    # SVG chart (no inline styles; colours are attributes)
    W, H, L, B, T, R = 480, 230, 56, 34, 14, 16
    def X(y): return L + (W - L - R) * y / 10
    def Y(v): return T + (H - T - B) * (1 - (v - 1000) / 500)
    pts = lambda f: " ".join(f"{X(y):.1f},{Y(f(y)):.1f}" for y in range(0, 11))
    grid = "".join(f'<line x1="{L}" x2="{W-R}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="#dfe5e2"/><text x="{L-8}" y="{Y(v)+4:.1f}" text-anchor="end" font-size="11" fill="#4a5a57">£{v:,}</text>' for v in (1000, 1250, 1500))
    xl = "".join(f'<text x="{X(y):.1f}" y="{H-14}" text-anchor="middle" font-size="11" fill="#4a5a57">{y}</text>' for y in yrs)
    chart = (f'<figure class="grow-fig"><svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="gt gd" width="100%">'
             f'<title id="gt">£1,000 at 4% a year for 10 years: simple and compound interest</title>'
             f'<desc id="gd">Simple interest reaches {_gbp(simple[-1],0)} after 10 years. Compound interest reaches {_gbp(comp[-1])}.</desc>{grid}{xl}'
             f'<text x="{(L+W-R)/2}" y="{H-1}" text-anchor="middle" font-size="11" fill="#4a5a57">years</text>'
             f'<polyline points="{pts(lambda y: 1000+40*y)}" fill="none" stroke="#8a9a96" stroke-width="3"/>'
             f'<polyline points="{pts(lambda y: 1000*1.04**y)}" fill="none" stroke="#d9822b" stroke-width="3"/>'
             f'<text x="{X(10)-6:.1f}" y="{Y(1400)+30:.1f}" text-anchor="end" font-size="12" fill="#4a5a57">Simple: {_gbp(1400,0)}</text>'
             f'<text x="{X(10)-6:.1f}" y="{Y(comp[-1])-8:.1f}" text-anchor="end" font-size="12" fill="#8a4b00">Compound: {_gbp(comp[-1],0)}</text></svg>'
             f'<figcaption class="hint">Illustration only: £1,000 at 4% a year, interest added once a year, no tax, no withdrawals, rate unchanged. Grey = simple, orange = compound.</figcaption></figure>')
    aer = ((1 + 0.04 / 12) ** 12 - 1) * 100
    r72 = []
    for r in (2, 3, 4, 5, 6, 8, 10, 12):
        r72.append(f'<tr><th scope="row">{r}%</th><td>{72/r:.1f}</td><td>{math.log(2)/math.log(1+r/100):.1f}</td></tr>')
    infl = f"{72/3:.0f}", f"{math.log(2)/math.log(1.03):.1f}"
    return f'''<h2 id="grow">How interest grows: simple, compound and the Rule of 72</h2>
<p><strong>Simple interest</strong> is paid only on the money you first put in. <strong>Compound interest</strong> is paid on that money <em>and</em> on the interest already added, so growth builds on itself. Savings accounts normally pay compound interest, and so do many debts.</p>
{chart}
<div class="table-scroll"><table class="wrap-th"><caption class="sr">£1,000 at 4% a year (illustration)</caption><thead><tr><th scope="col">Years</th><th scope="col">Simple interest</th><th scope="col">Compound interest</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="hint">Simple: £40 a year. Compound: interest added yearly. Worked from the standard formula: £1,000 × 1.04<sup>years</sup>. After 10 years that is {_gbp(comp[-1])}, against £1,400 with simple interest. It ignores tax and assumes the rate never changes, which is unusual for a real account.</p>
<h3>AER and how often interest is added</h3>
<p>The more often interest is added, the more it earns on itself. The <strong>AER</strong> (Annual Equivalent Rate) puts every account on the same footing: it is what the rate would be if interest were added once a year. For example, 4% a year paid monthly works out at an AER of about <strong>{aer:.2f}%</strong> ((1 + 0.04 ÷ 12)<sup>12</sup> − 1). That is why AER is the figure to compare between accounts.</p>
<h3>The Rule of 72</h3>
<p>The <strong>Rule of 72</strong> is a quick way to estimate how long money takes to double: <strong>divide 72 by the yearly rate</strong>. It is a mental shortcut, not an exact figure.</p>
<ul><li>At 4% a year: 72 ÷ 4 = about <strong>18 years</strong> to double.</li><li>At 8% a year: 72 ÷ 8 = about <strong>9 years</strong> to double.</li></ul>
<div class="table-scroll"><table class="wrap-th"><caption class="sr">Rule of 72 against the exact answer</caption><thead><tr><th scope="col">Rate a year</th><th scope="col">Rule of 72 (years)</th><th scope="col">Exact (years)</th></tr></thead><tbody>{"".join(r72)}</tbody></table></div>
<p class="hint">Exact = ln 2 ÷ ln(1 + rate). The two columns are close but not identical. The rule ignores tax, charges, inflation and any change in the rate, so treat it as a rough guide. It works the other way too: if prices rose by an example 3% a year, the rule gives about {infl[0]} years for prices to double (exact {infl[1]}). That's an illustration, not a forecast. See <a href="how-money-works.html#s8">what inflation does to cash</a>.</p>
<section class="calc" id="grow-calc" aria-labelledby="grow-h"><h3 id="grow-h" style="margin-top:0">Interest growth calculator</h3>
<form id="gr-form" class="fields" novalidate><div><label for="gr-amt">Amount (£)</label><input id="gr-amt" type="number" value="1000" min="0" step="100" inputmode="decimal"></div>
<div><label for="gr-rate">Interest rate (% a year)</label><input id="gr-rate" type="number" value="4" min="0" max="100" step="0.1" inputmode="decimal"></div>
<div><label for="gr-years">Years</label><input id="gr-years" type="number" value="10" min="1" max="60" step="1" inputmode="numeric"></div>
<div><label for="gr-freq">Interest is added</label><select id="gr-freq"><option value="1">Once a year</option><option value="12">Monthly</option></select></div>
<div style="grid-column:1/-1" class="results" aria-live="polite"><div class="res"><span>With simple interest</span><b id="gr-simple">–</b></div><div class="res"><span>With compound interest</span><b id="gr-comp">–</b></div><div class="res"><span>Equivalent AER</span><b id="gr-aer">–</b></div>
<div class="res"><span>Rule of 72 estimate to double</span><b id="gr-r72">–</b></div><div class="res"><span>Exact time to double</span><b id="gr-exact">–</b></div></div>
<p class="hint" style="grid-column:1/-1">Illustration only: a fixed rate, no tax, no withdrawals or extra deposits, before any inflation. Real accounts can change their rate. Not a forecast.</p></form></section>'''
GROW = grow_section()
