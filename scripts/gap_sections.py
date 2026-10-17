# Stage-2 gap content (G5 borrowing, G6 Plan 2, G10 risk, G4 ways to pay, G7 pensions extras). exec'd from build.py after gap_common.py.
# All sources checked on 17 October 2026 (CG). Information only - not advice.
import math as _gm
SG.update({
 "apr": ("FCA Handbook glossary – representative APR", "https://handbook.fca.org.uk/glossary/G3354"),
 "od": ("FCA – Changes to overdraft charges (from April 2020)", "https://www.fca.org.uk/data/changes-overdraft-charges"),
 "od2": ("FCA Handbook – CONC 5C.2: charges for overdrafts to be interest rates", "https://handbook.fca.org.uk/handbook/conc5c/conc5cs2"),
 "hcstc": ("FCA Handbook – CONC 5A: cost cap for high-cost short-term credit", "https://handbook.fca.org.uk/handbook/conc5a"),
 "hcstc2": ("FCA – High-cost short-term credit (price cap kept after 2026 review)", "https://www.fca.org.uk/firms/high-cost-credit-consumer-credit/high-cost-short-term-credit"),
 "loansh": ("GOV.UK – Report a loan shark", "https://www.gov.uk/report-loan-shark"),
 "bnpl": ("FCA – Buy Now Pay Later", "https://www.fca.org.uk/consumers/buy-now-pay-later"),
 "mh75": ("MoneyHelper – Section 75 and chargeback protection", "https://www.moneyhelper.org.uk/en/everyday-money/credit/how-youre-protected-when-you-pay-by-card"),
 "ddg": ("Direct Debit scheme – The Direct Debit Guarantee", "https://www.directdebit.co.uk/direct-debit-explained/direct-debit-guarantee/"),
 "cra22": ("legislation.gov.uk – Consumer Rights Act 2015, section 22 (30-day short-term right to reject)", "https://www.legislation.gov.uk/ukpga/2015/15/section/22/enacted"),
 "govret": ("GOV.UK – Accepting returns and giving refunds: the law (14-day cancellation for online, phone and mail orders)", "https://www.gov.uk/accepting-returns-and-giving-refunds"),
 "lisa2": ("GOV.UK – Withdrawing money from your Lifetime ISA", "https://www.gov.uk/lifetime-isa/withdrawing-money-from-your-lifetime-isa"),
 "fscsinv": ("FSCS – Investments: compensation limits", "https://www.fscs.org.uk/what-we-cover/investments/"),
 "fscsins": ("FSCS – Insurance protection and compensation", "https://www.fscs.org.uk/what-we-cover/insurance/"),
 "fscscrypto": ("FSCS – Cryptoassets: are they covered, and what's the risk?", "https://www.fscs.org.uk/news/protection/cryptocurrencies-risk-cover/"),
 "mhem": ("MoneyHelper – Emergency savings: how much is enough?", "https://www.moneyhelper.org.uk/en/savings/types-of-savings/emergency-savings-how-much-is-enough"),
 "mhbud": ("MoneyHelper – Budget planner", "https://www.moneyhelper.org.uk/en/everyday-money/budgeting/budget-planner"),
 "mhsi": ("MoneyHelper – What's the difference between saving and investing?", "https://www.moneyhelper.org.uk/en/savings/how-to-save/should-i-save-or-invest"),
 "vehins": ("GOV.UK – Vehicle insurance", "https://www.gov.uk/vehicle-insurance"),
 "mhcar": ("MoneyHelper – Car insurance: what you need to know", "https://www.moneyhelper.org.uk/en/everyday-money/insurance/car-insurance-what-you-need-to-know"),
 "mhrent": ("MoneyHelper – Do I need insurance when renting?", "https://www.moneyhelper.org.uk/en/blog/insurance/i-m-renting-my-home-do-i-need-insurance"),
 "mhlife": ("MoneyHelper – What is life insurance?", "https://www.moneyhelper.org.uk/en/everyday-money/insurance/what-is-life-insurance"),
 "mhip": ("MoneyHelper – What is income protection insurance?", "https://www.moneyhelper.org.uk/en/everyday-money/insurance/what-is-income-protection-insurance"),
 "ghic": ("NHS – Apply for a UK Global Health Insurance Card (GHIC)", "https://www.nhs.uk/using-the-nhs/healthcare-abroad/apply-for-a-free-uk-global-health-insurance-card-ghic/"),
 "fti": ("GOV.UK – Foreign travel insurance", "https://www.gov.uk/guidance/foreign-travel-insurance"),
 "pts": ("GOV.UK – Find pension contact details (Pension Tracing Service)", "https://www.gov.uk/find-pension-contact-details"),
 "spf": ("GOV.UK – Check your State Pension forecast", "https://www.gov.uk/check-state-pension"),
 "slplan": ("GOV.UK – Which student loan repayment plan you're on", "https://www.gov.uk/repaying-your-student-loan/which-repayment-plan-you-are-on"),
 "slwo": ("GOV.UK – When your student loan gets written off or cancelled", "https://www.gov.uk/repaying-your-student-loan/when-your-student-loan-gets-written-off-or-cancelled"),
 "slstart": ("GOV.UK – When you start repaying your student loan", "https://www.gov.uk/repaying-your-student-loan/when-you-start-repaying"),
 "sl2freeze": ("UK Parliament written question (3 Feb 2026, via TheyWorkForYou) – Plan 2 threshold stays at £29,385 up to April 2030", "https://www.theyworkforyou.com/wrans/?id=2026-01-23.108031.h"),
 "sl2thr": ("GOV.UK / Student Loans Company – Plan 2 and Plan 3 thresholds from April 2026 (26 Nov 2025)", "https://www.gov.uk/government/news/student-loans-interest-and-repayment-threshold-announcement-for-plan-2-and-plan-3-loans"),
 "bs": ("Insolvency Service (GOV.UK) – Debt Respite Scheme (Breathing Space) guidance", "https://www.gov.uk/government/publications/debt-respite-scheme-breathing-space-guidance/debt-respite-scheme-breathing-space-guidance-for-creditors"),
 "foscheck": ("Financial Ombudsman Service – how to complain", "https://www.financial-ombudsman.org.uk/consumers/how-to-complain"),
})
S.update(SG)
def _gb(x, dp=2): return f"£{x:,.{dp}f}"

# ---------------- G5: borrowing section for Credit scores & debt help ----------------
_pd = 100 * 0.008 * 30
G5 = f'''<h2 id="borrowing">What borrowing costs: the ladder, APR, payday loans and BNPL</h2>
<p>Not all borrowing costs the same, and the price you're offered depends on your credit record. This is a <strong>rough order of cost, not a ranking of products</strong>: always compare the APR and the total you'd repay, and check the lender is authorised on the <a href="https://www.fca.org.uk/consumers/how-check-firm-individual-authorised" rel="noopener">FCA Register</a>.</p>
<div class="table-scroll"><table class="wrap-th"><caption class="sr">The borrowing ladder, from usually cheaper to usually dearer</caption><thead><tr><th scope="col">Step</th><th scope="col">What it is</th><th scope="col">What to know</th></tr></thead><tbody>
<tr><th scope="row">1. Credit union or a 0% deal</th><td>A member-owned lender, or a card or loan with no interest for a set period.</td><td>Often lower-cost if you repay on schedule – but the rate you get depends on your record, and a 0% deal usually ends. Check the rate after it ends.</td></tr>
<tr><th scope="row">2. Personal loan</th><td>A fixed amount, repaid in fixed payments over a set time.</td><td>You know the total you'll repay up front. The rate on offer is personal to you (see APR below).</td></tr>
<tr><th scope="row">3. Credit card</th><td>A revolving limit you can spend up to.</td><td>No interest on purchases if you clear the balance in full by the due date; costly if you don't. See our <a href="credit-cards.html">credit cards guide</a>.</td></tr>
<tr><th scope="row">4. Overdraft</th><td>Borrowing through your current account.</td><td>Since 6 April 2020 UK banks must charge overdrafts as one annual interest rate, not daily or monthly fees. Intended for short gaps, not as a long-term loan.</td></tr>
<tr><th scope="row">5. Payday loan</th><td>High-cost short-term credit (HCSTC).</td><td>Legal, but capped – and still very costly. See below.</td></tr>
<tr><th scope="row">6. Loan shark</th><td>An illegal lender.</td><td>Not regulated, and you can report them anonymously. See below.</td></tr></tbody></table></div>
<p class="hint">The ordering is a general guide; individual deals vary. The credit-union and 0% descriptions are general explanations rather than a quoted figure.</p>
{sg("od","od2")}

<h3 id="apr">APR and "representative APR"</h3>
<p><strong>APR</strong> (annual percentage rate) is a yearly rate of the cost of borrowing, including interest and certain compulsory charges, so you can compare credit. A <strong>representative APR</strong> is the rate a lender must reasonably expect to give to <strong>at least 51%</strong> of the people who are accepted for that product after seeing the advert. That means up to 49% can be offered a <em>higher</em> rate. Your own APR depends on your credit record and circumstances, and the lender must tell you before you sign.</p>
{sg("apr")}

<h3 id="payday">Payday loans and the price cap</h3>
<p>Payday loans are called high-cost short-term credit. FCA rules in force since 2 January 2015 cap what a lender can charge:</p>
<ul><li><strong>0.8% a day</strong> of the amount borrowed, for interest and fees combined.</li>
<li><strong>£15</strong> maximum in total for default (late-payment) charges.</li>
<li><strong>100%</strong> total cost cap: interest and fees together can never exceed the amount you borrowed, so £100 borrowed can't cost more than £100 in charges (you'd repay at most £200).</li></ul>
<p><strong>Illustration:</strong> at the cap, borrowing £100 for 30 days could cost up to {_gb(_pd,0)} in interest and fees (£100 × 0.8% × 30 days) – before any default charges. That is the <em>most</em> the cap allows, not a typical or recommended price. In September 2026 the FCA decided to keep the cap at its current level after its 2026 review.</p>
{sg("hcstc","hcstc2")}

<h3 id="sharks">Loan sharks: who to call</h3>
<p>Loan sharks are illegal moneylenders who often charge very high interest rates. If you've borrowed from one, or you've spotted one, you can report them anonymously. The numbers differ by nation:</p>
<div class="table-scroll"><table class="contacts"><caption class="sr">Where to report a loan shark</caption><thead><tr><th scope="col">Where you live</th><th scope="col">Who to contact</th></tr></thead><tbody>
<tr><th scope="row">England</th><td>Stop Loan Sharks (Illegal Money Lending Team): <strong>0300 555 2222</strong> (24 hours) · text <strong>07860 022 116</strong></td></tr>
<tr><th scope="row">Wales</th><td>Stop Loan Sharks Wales: <strong>0300 123 3311</strong> (24 hours)</td></tr>
<tr><th scope="row">Scotland</th><td>Trading Standards Scotland: <strong>0800 074 0878</strong> (24 hours)</td></tr>
<tr><th scope="row">Northern Ireland</th><td>Trading Standards Consumerline: <strong>0300 123 6262</strong></td></tr></tbody></table></div>
<p>You can check whether a lender is authorised on the FCA Register, or call the FCA consumer helpline on <strong>0800 111 6768</strong> (Monday to Friday 8am–6pm, Saturday 9am–1pm).</p>
{sg("loansh")}

<h3 id="bnpl">Buy now, pay later (BNPL)</h3>
<p>The FCA began regulating interest-free <strong>deferred payment credit</strong> (the most common form of BNPL: repayable in 12 or fewer instalments over 12 months or less) on <strong>15 July 2026</strong>. It is regulated when the lender and the seller are <em>different businesses</em>; a plan provided by the retailer itself is not, and agreements taken out before 15 July 2026 stay unregulated.</p>
<ul><li>Lenders must be authorised by the FCA, or be in its temporary permissions regime, and must check you can afford to repay before you take out an agreement.</li>
<li>They must give you key information first, including repayment dates, amounts and any late fee, and must contact you if you miss a payment and offer support if you're struggling.</li>
<li>You can complain to the lender, then to the Financial Ombudsman Service. For agreements covered by the new rules, Section 75 of the Consumer Credit Act now applies, the same protection as a credit card (see <a href="bank-accounts.html#ways">ways to pay and your protections</a>).</li></ul>
<p>BNPL is still borrowing: missed payments can have consequences, and the FCA notes there are two types – one that charges interest and one that doesn't.</p>
{sg("bnpl","mh75")}
<p>If borrowing is getting on top of you, jump to <a href="#help">free debt help</a>, <a href="#priority">priority debts</a> and <a href="#breathing">Breathing Space</a>.</p>
'''

# ---------------- G6: Plan 2 block for Students ----------------
def _p2(inc_m): return _gm.floor((inc_m - 2448) * 0.09)
_p2e = _p2(3000)
G6 = f'''<h2 id="plan2">Repaying: Plan 2 (started 2012–2023)</h2>
<p>Plan 2 is for students from <strong>England who started a course between 1 September 2012 and 31 July 2023</strong>, and students from <strong>Wales who started on or after 1 September 2012</strong>. Repayments depend on income, not on how much you owe.</p>
<div class="grid g2">
<div class="card"><h3>Plan 2 thresholds</h3><ul><li><strong>£29,385</strong> a year</li><li><strong>£2,448</strong> a month</li><li><strong>£565</strong> a week</li></ul><p class="hint" style="margin:.4rem 0 0">You repay <strong>9%</strong> of income over the threshold.</p></div>
<div class="card"><h3>How long and what changes</h3><ul><li>Any balance left is written off <strong>30 years</strong> after the April you were first due to repay.</li><li>The threshold stays at <strong>£29,385 up to April 2030</strong>, then rises each year with the Retail Price Index (RPI), according to a Department for Education written answer. The announcements refer to English Plan 2 loans, so if you're from Wales, check with Student Finance Wales.</li></ul></div>
</div>
<h3>Interest on Plan 2</h3>
<p>Plan 2 interest is a <strong>variable rate</strong>. While you study it is RPI plus 3%. After you leave your course it depends on your income:</p>
<div class="table-scroll"><table class="wrap-th"><caption class="sr">Plan 2 interest rate by annual income (2026/27)</caption><thead><tr><th scope="col">Annual income</th><th scope="col">Interest rate</th></tr></thead><tbody>
<tr><th scope="row">£29,385 or less</th><td>4.1%</td></tr>
<tr><th scope="row">£29,386 to £52,884</th><td>4.1% plus up to 1.9% (rising with income)</td></tr>
<tr><th scope="row">£52,885 or more</th><td>6%</td></tr></tbody></table></div>
<p class="note" role="note"><strong>The 6% limit is described as "currently" in place.</strong> GOV.UK says the rate is usually RPI plus up to 3% but there is <em>currently</em> a cap of 6%. Treat the cap as something that could change and check the <a href="https://www.gov.uk/repaying-your-student-loan/what-you-pay" rel="noopener">official page</a> for today's rates.</p>
<p><strong>Example (illustration, worked from the GOV.UK figures):</strong> pay of £3,000 a month is £552 over the £2,448 monthly threshold. 9% of £552 is £49.68, and GOV.UK's own examples round down, so about <strong>£{_p2e} a month</strong> is repaid through payroll.</p>
<div class="table-scroll"><table class="wrap-th"><caption class="sr">Plan 2 compared with Plan 5</caption><thead><tr><th scope="col"></th><th scope="col">Plan 2</th><th scope="col">Plan 5</th></tr></thead><tbody>
<tr><th scope="row">Who</th><td>England: started 1 Sep 2012 – 31 Jul 2023. Wales: from 1 Sep 2012</td><td>England: started on or after 1 Aug 2023</td></tr>
<tr><th scope="row">You repay</th><td>9% of income over £29,385</td><td>9% of income over £25,000</td></tr>
<tr><th scope="row">Interest now</th><td>4.1% to 6%, by income</td><td>4.1%</td></tr>
<tr><th scope="row">Written off after</th><td>30 years</td><td>40 years</td></tr></tbody></table></div>
<p>Student loans don't appear on your credit report, but lenders may take them into account when checking affordability, for example for a mortgage.</p>
{sg("slrepay","sl2thr","sl2freeze","slplan","slwo","slstart")}
'''

# ---------------- G10: Risk, spreading and protection (Investments) ----------------
def _fv(p, r, n): return p * (1 + r) ** n
_f0, _f1 = _fv(10000, .05, 30), _fv(10000, .04, 30)
G10 = f'''<h2 id="risk">Risk, spreading and protection</h2>
<p>Investing means accepting that your money can fall in value. MoneyHelper describes it this way: the value can go up or down, but there's a chance of higher rewards than from saving. Whether it suits you depends on your goals, how long you can leave the money and how much loss you could cope with.</p>
<h3>How long you can leave it</h3>
<ul><li><strong>Short-term goals (within five years):</strong> MoneyHelper says the general rule is to save in cash deposits, because markets can be down just when you need the money.</li>
<li><strong>Medium-term (five to ten years):</strong> cash can sometimes be the answer; it depends on how much risk you're willing to take.</li>
<li><strong>Long-term (ten years or more):</strong> investing may be worth considering, because inflation can seriously erode cash savings over the long run.</li></ul>
<p>MoneyHelper also suggests having <strong>three to six months' essential outgoings</strong> in an instant-access account first (see our <a href="budgeting-emergency-fund.html#emergency">emergency fund guide</a>), and that you think about investing money you don't need for <strong>five years</strong>. It adds that the only time you shouldn't save or invest is if you need to get debts under control first.</p>
{sg("mhsi","mhem")}
<h3>A rough risk ladder</h3>
<div class="table-scroll"><table class="wrap-th"><caption class="sr">A rough ladder of investment risk</caption><thead><tr><th scope="col">Type</th><th scope="col">In plain English</th><th scope="col">Risk to know about</th></tr></thead><tbody>
<tr><th scope="row">Cash savings</th><td>Money in a bank, building society or similar account.</td><td>Unlikely to fall in value, but inflation can reduce what it buys. Protected by the <a href="bank-accounts.html#fscs">FSCS deposit limit</a> (£120,000).</td></tr>
<tr><th scope="row">Bonds and gilts</th><td>Lending money to a government or company for interest.</td><td>Prices move, and companies can fail to repay. See our <a href="gilts.html">gilts guide</a>.</td></tr>
<tr><th scope="row">Funds</th><td>A pooled investment holding many shares or bonds.</td><td>Spreads the risk across many holdings, but the whole market can fall.</td></tr>
<tr><th scope="row">Single shares</th><td>Part-ownership of one company.</td><td>All your eggs in one basket: if that company struggles, you could lose a lot.</td></tr>
<tr><th scope="row">Cryptoassets</th><td>Digital tokens such as Bitcoin.</td><td>The FSCS says values can be extremely volatile and you could lose a lot, quickly.</td></tr></tbody></table></div>
<p class="hint">This is a general picture. Risk depends on the specific investment, and the order can differ within each type.</p>
<h3>Spreading your money (diversification)</h3>
<p>MoneyHelper says you can lower the level of risk you take by spreading your money across different types of investment, which is called diversification. A fund that holds many companies already does some of this for you; our <a href="#index">index funds</a> section explains more.</p>
<h3>Fees quietly add up</h3>
<p><strong>Illustration:</strong> £10,000 growing at 5% a year for 30 years becomes about {_gb(_f0,0)}. If a 1% yearly cost reduces that growth to 4%, it becomes about {_gb(_f1,0)} – roughly {_gb(_f0-_f1,0)} less. Real returns vary and can be negative; this only shows how a small yearly percentage compounds. Try your own figures in the <a href="#calc">fee calculator</a>.</p>
<h3>What protection do you have?</h3>
<ul><li><strong>Investments can fall. The FSCS does not protect you against that.</strong> It says it can't accept claims for poor investment performance.</li>
<li>If an FCA- or PRA-authorised investment firm fails, the FSCS may pay compensation of up to <strong>£85,000 per eligible person, per firm</strong> (for firms that failed after 1 April 2019), for example if there is a shortfall in the money or assets the firm held for you. The service or product must be regulated for the cover to apply.</li>
<li>This is separate from the <strong>£120,000</strong> deposit limit, which covers cash in banks and building societies.</li>
<li><strong>Cryptoassets:</strong> the FSCS said (May 2023) that the FCA does not regulate most cryptoassets, so it can't protect you if a platform that holds them fails. UK crypto rules are changing, so check the FCA's current page.</li>
<li>Check any firm on the <a href="https://www.fca.org.uk/consumers/how-check-firm-individual-authorised" rel="noopener">FCA Register</a> before you invest, and see our <a href="scams-fraud.html">scams guide</a> for investment scam warning signs.</li></ul>
{sg("fscsinv","fscscrypto","fcacheck")}
'''

# ---------------- G4: ways to pay and your protections (Bank accounts) ----------------
G4 = f'''<h2 id="ways">Ways to pay and your protections</h2>
<p>How you pay can change what help you have if something goes wrong. This table summarises the main options. It's general information: always check your own provider's terms.</p>
<div class="table-scroll"><table class="wrap-th"><caption class="sr">Ways to pay and the protections that may apply</caption><thead><tr><th scope="col">Way to pay</th><th scope="col">What it is</th><th scope="col">Protection that may apply</th></tr></thead><tbody>
<tr><th scope="row">Debit card</th><td>Spends your own money.</td><td><strong>Chargeback</strong> – a voluntary card-scheme process, not a legal right. Contact the seller first, then ask your bank within <strong>120 days</strong> (for future events, from the day the event should have happened). Section 75 does not apply.</td></tr>
<tr><th scope="row">Credit card</th><td>Spends borrowed money.</td><td><strong>Section 75</strong> – the card provider shares responsibility with the seller for a single item costing <strong>over £100 and up to £30,000</strong>, even if you only paid part (such as a deposit) on the card. Chargeback may also be available.</td></tr>
<tr><th scope="row">Buy now, pay later</th><td>Split a purchase into instalments.</td><td>Agreements from a third-party lender taken out on or after <strong>15 July 2026</strong> now have Section 75 protection, and the lender is FCA-regulated. A plan from the retailer itself, or one taken out before that date, is not covered. See <a href="credit-scores-debt-help.html#bnpl">BNPL</a>.</td></tr>
<tr><th scope="row">Direct Debit</th><td>A company collects the amount you've agreed, on its schedule.</td><td>The <strong>Direct Debit Guarantee</strong>: if the organisation or your bank makes an error, you're entitled to a full and immediate refund. It doesn't change what you owe under your contract. You can cancel a Direct Debit at any time through your bank.</td></tr>
<tr><th scope="row">Standing order</th><td>You tell your bank to send a fixed amount on a set date.</td><td>You control it, so it suits rent or moving money to savings on payday. Ask your bank how to change or stop one.</td></tr>
<tr><th scope="row">Bank transfer</th><td>Money sent straight to another account, often instantly.</td><td>Hard to undo once sent. Check the name match (Confirmation of Payee) warning. If you're <em>tricked</em> into paying a fraudster, banks must usually reimburse eligible UK Faster Payments and CHAPS payments up to £85,000 – see our <a href="scams-fraud.html#app">scams guide</a>.</td></tr></tbody></table></div>
{sg("mh75","ddg","bnpl","psrapp")}

<h3 id="rights">Your shopping rights</h3>
<ul><li><strong>Faulty goods – 30 days.</strong> You have a short-term right to reject faulty goods within 30 days (beginning the day after ownership, delivery and any required installation have all happened) and get a refund. Shorter periods can apply to goods that would reasonably perish sooner.</li>
<li><strong>Bought online, by phone or by mail – 14 days.</strong> You can usually cancel without giving a reason by telling the seller within 14 days of receiving the item; you then have another 14 days to return it and the seller must refund within 14 days of getting it back. There are exceptions, such as personalised or perishable items, sealed hygiene items and unwrapped media.</li>
<li><strong>Repairs and replacements.</strong> Within six months a seller must usually repair or replace a faulty item unless they can prove it wasn't faulty when you bought it; you can claim for up to six years (five in Scotland).</li></ul>
<p>Rights can change, so check the official pages if it matters for a purchase. If you're not happy with how a firm handles a complaint, you may be able to take it to the <a href="https://www.financial-ombudsman.org.uk/consumers/how-to-complain" rel="noopener">Financial Ombudsman Service</a> (for financial products) or ask for advice from Citizens Advice.</p>
{sg("cra22","govret")}
'''

# ---------------- G7: pensions extras ----------------
_q = 30000 - 6240
_emp_gross = .05 * _q / 12; _emp_net = _emp_gross * .8; _er = .03 * _q / 12; _tot = _emp_gross + _er
G7 = f'''<h2 id="example">A month into your workplace pension: a worked example</h2>
<p><strong>Illustration only.</strong> Take a £30,000 salary paid monthly, in a scheme paying the legal minimum on qualifying earnings (£6,240 to £50,270) with tax relief at source. Qualifying earnings are £30,000 − £6,240 = £23,760 a year.</p>
<div class="table-scroll"><table class="wrap-th"><caption class="sr">Monthly pension contributions on a £30,000 salary at the legal minimum</caption><thead><tr><th scope="col">Part</th><th scope="col">Workings</th><th scope="col">Per month</th></tr></thead><tbody>
<tr><th scope="row">You, after tax relief</th><td>4% of £23,760 ÷ 12 (what leaves your pay)</td><td>{_gb(_emp_net)}</td></tr>
<tr><th scope="row">Tax relief added</th><td>20% basic-rate relief claimed by your provider</td><td>{_gb(_emp_gross-_emp_net)}</td></tr>
<tr><th scope="row">Your employer</th><td>3% of £23,760 ÷ 12</td><td>{_gb(_er)}</td></tr>
<tr><th scope="row"><strong>Total into your pension</strong></th><td>8% of £23,760 ÷ 12</td><td><strong>{_gb(_tot)}</strong></td></tr></tbody></table></div>
<p>So about <strong>£158 a month</strong> goes into the pension, but only about <strong>£79</strong> of it comes out of your take-home pay. Your scheme may work differently (some use "net pay" tax relief or higher contributions), so check your payslip and scheme details. See the <a href="pay-tax-payslip.html#payslip">payslip guide</a> for how this appears on a payslip.</p>
{sg("fcapen")}
<p class="hint">Minimum rates and qualifying-earnings limits are those on this page's <a href="#workplace">workplace pensions</a> section (8% in total, at least 3% from the employer; £6,240 to £50,270 for 2026/27).</p>

<h2 id="tracing">Find lost pensions and check your State Pension</h2>
<ul><li><strong>Pension Tracing Service (free, GOV.UK).</strong> If you've lost track of a workplace or personal pension, use the <a href="https://www.gov.uk/find-pension-contact-details" rel="noopener">online tracing service</a> to find the scheme's contact details. You need the name of an employer or a pension provider. It <em>won't</em> tell you whether you have a pension or what it is worth – you then contact the scheme. You can also ask by phone on <strong>0800 731 0175</strong> (Monday to Friday, 10am to 3pm) or by post.</li>
<li><strong>State Pension forecast.</strong> Check how much State Pension you could get, when you can get it and whether you can increase it, on GOV.UK or in the HMRC app. You sign in with a GOV.UK account.</li>
<li><strong>Beware of scams.</strong> The tracing service is free. Cold calls or "free pension reviews", and anyone offering to release money before the minimum pension age, are classic warning signs – see our <a href="scams-fraud.html#pensions">pension scams</a> section.</li></ul>
{sg("pts","spf","fcapen")}
'''
