# Stage-2 guides: budgeting and emergency funds (G2) and insurance basics (G8). exec'd from build.py after pages14.
# Sources checked 17 October 2026 (see gap_common.py / gap_sections.py). Information only - not advice.
_X = _pay(30000); _Xn = _pay(30000, plan="none"); _X5 = _pay(30000, plan="p5")
_net = round(_X["net"]); _n5 = _X["net"] * .5; _n3 = _X["net"] * .3; _n2 = _X["net"] * .2
_ess = 1400
pages["budgeting-emergency-fund.html"] = page("budgeting-emergency-fund.html", "Budgeting and emergency funds: a plain-English guide – MoneyBySharma",
 "How to build a simple budget from your take-home pay, the 50/30/20 rule of thumb, how much to keep as an emergency fund (three to six months' essentials) and eight common money mistakes to avoid.",
 ph("Budgeting &amp; emergency funds","Budgeting and emergency funds","Start from what actually lands in your account, plan every pound, and build a cushion for the unexpected. Information only – not advice."), W(f'''
<div class="cols"><div>
<div class="note" style="margin-top:1.5rem"><strong>Information only – not advice.</strong> This page explains common budgeting ideas using official guidance from MoneyHelper and GOV.UK. It can't know your circumstances, and the worked numbers are illustrations, not targets.</div>

<h2 id="takehome">Start with take-home pay</h2>
<p>Plan with <strong>net pay</strong> – the amount that lands in your bank account – not your salary. On the <a href="pay-tax-payslip.html#payslip">example payslip</a> (£30,000 salary, paid monthly, standard tax code, minimum workplace pension and a Plan 2 student loan) take-home is about <strong>{_gb(_X["net"])} a month</strong>. Without a student loan it would be about {_gb(_Xn["net"])}, and on Plan 5 about {_gb(_X5["net"])}. Your payslip will differ.</p>
<p>MoneyHelper's free <a href="https://www.moneyhelper.org.uk/en/everyday-money/budgeting/budget-planner" rel="noopener">Budget planner</a> lets you list your income and outgoings, see what's essential and what you could save.</p>
{sg("payslip","mhbud")}

<h2 id="steps">Four steps</h2>
<ol class="steps">
<li><strong>Start with take-home pay.</strong> Use the figure that arrives in your account.</li>
<li><strong>List the must-pays.</strong> Rent or mortgage, bills, phone, travel, debt repayments and subscriptions.</li>
<li><strong>Pay future you first.</strong> Set up a standing order to a savings account for just after payday, before you spend.</li>
<li><strong>Share out the rest.</strong> Turn what's left into a weekly spending amount and stick to it.</li></ol>

<h2 id="rule">The 50/30/20 rule of thumb</h2>
<p>A popular way to split take-home pay is <strong>50% needs, 30% wants and 20% future</strong> (savings and extra debt repayments). It is a <strong>rule of thumb, not an official rule</strong>, and it isn't from a regulator – with high rent or low pay, many people can't hit it, and that's fine. Use it as a starting point and adjust.</p>
<div class="table-scroll"><table class="wrap-th"><caption class="sr">The 50/30/20 split applied to the example take-home pay</caption><thead><tr><th scope="col">Bucket</th><th scope="col">Share</th><th scope="col">Includes</th><th scope="col">On {_gb(_X["net"],0)} a month</th></tr></thead><tbody>
<tr><th scope="row">Needs</th><td>50%</td><td>Rent, food, bills, travel</td><td>{_gb(_n5,0)}</td></tr>
<tr><th scope="row">Wants</th><td>30%</td><td>Eating out, hobbies, treats</td><td>{_gb(_n3,0)}</td></tr>
<tr><th scope="row">Future</th><td>20%</td><td>Savings and paying off debt</td><td>{_gb(_n2,0)}</td></tr></tbody></table></div>
<p class="hint">Illustration only, using the example payslip's take-home pay of {_gb(_X["net"])} rounded to the nearest pound.</p>

<h2 id="emergency">Emergency funds: how much is enough?</h2>
<p>An emergency fund is money set aside for the unexpected, such as a broken boiler, a car repair or a gap in income. MoneyHelper gives this rule of thumb: have <strong>three to six months' essential outgoings</strong> in an <strong>instant-access savings account</strong>. Essentials are things like rent or mortgage, food, heating, bills and anything else you can't live without.</p>
<div class="table-scroll"><table class="wrap-th"><caption class="sr">Emergency fund targets for example monthly essentials</caption><thead><tr><th scope="col">Monthly essentials</th><th scope="col">3 months</th><th scope="col">6 months</th></tr></thead><tbody>
<tr><th scope="row">{_gb(1000,0)}</th><td>{_gb(3000,0)}</td><td>{_gb(6000,0)}</td></tr>
<tr><th scope="row">{_gb(_ess,0)}</th><td>{_gb(_ess*3,0)}</td><td>{_gb(_ess*6,0)}</td></tr></tbody></table></div>
<p class="hint">The £1,000 row is MoneyHelper's own example; £1,400 is an illustration. Your essentials are your own figure.</p>
<ul><li><strong>Any amount helps.</strong> Don't wait until you can hit the target: save what you can, as regularly as you can. MoneyHelper says saving smaller, regular amounts is often more effective than occasional large ones, and suggests a standing order or Direct Debit.</li>
<li><strong>Priority debts first.</strong> MoneyHelper says it can be cheaper in the long run to pay off credit card debt, an unauthorised overdraft, payday loans, door-to-door lending or mortgage arrears <em>before</em> piling money into an emergency fund. See our <a href="credit-scores-debt-help.html#priority">priority debts</a> section.</li>
<li><strong>Keep it separate and accessible.</strong> An easy-access account means you can reach the money at once. See <a href="savings.html">Savings</a> for account types, and note the FSCS protects up to £120,000 per person, per banking licence ( <a href="bank-accounts.html#fscs">details</a>).</li>
<li><strong>Then think about investing.</strong> MoneyHelper suggests building the emergency fund first; see <a href="investments.html#risk">risk, spreading and protection</a>.</li></ul>
{sg("mhem","mhsi")}

<h2 id="leaks">Plug the leaks</h2>
<ul><li><strong>Forgotten subscriptions.</strong> Not used it this month? Cancel it and re-join later if you miss it.</li>
<li><strong>Little and often.</strong> A £4 coffee five days a week is £4 × 5 × 52 = <strong>£1,040 a year</strong> (illustration).</li>
<li><strong>The "it's only" trap.</strong> Delivery fees, in-app purchases and small buy now, pay later plans add up. BNPL is borrowing: see <a href="credit-scores-debt-help.html#bnpl">BNPL</a>.</li>
<li><strong>Lumpy yearly costs.</strong> Birthdays, Christmas, the MOT and annual insurance: divide the yearly total by 12 and save that amount monthly.</li></ul>

<h2 id="mistakes">Eight common money mistakes</h2>
<div class="table-scroll"><table class="wrap-th"><caption class="sr">Common money mistakes and what to do instead</caption><thead><tr><th scope="col">Mistake</th><th scope="col">Instead</th></tr></thead><tbody>
<tr><th scope="row">Budgeting with your salary</th><td>Plan with net pay. On the example payslip, £30,000 a year is about {_gb(_X["net"],0)} a month after tax, National Insurance, pension and a Plan 2 loan. Yours will differ – see the <a href="pay-tax-payslip.html">payslip guide</a>.</td></tr>
<tr><th scope="row">Opting out of the workplace pension</th><td>Think before you opt out: you usually lose your employer's contribution and the tax relief. See <a href="pensions.html#workplace">workplace pensions</a>.</td></tr>
<tr><th scope="row">Paying only the credit card minimum</th><td>Pay in full by Direct Debit if you can, or as much as you can. See <a href="credit-cards.html">credit cards</a>.</td></tr>
<tr><th scope="row">Never checking your tax code</th><td>Check it each April and after changing job. See <a href="pay-tax-payslip.html#code">tax codes</a>.</td></tr>
<tr><th scope="row">Savings sitting in a very low-interest account</th><td>Compare AER, access rules and FSCS protection; consider an ISA. See <a href="savings.html">savings</a>.</td></tr>
<tr><th scope="row">BNPL for everyday spending</th><td>Treat it as a loan. If you can't pay today, ask yourself whether you really will next month. See <a href="credit-scores-debt-help.html#bnpl">BNPL</a>.</td></tr>
<tr><th scope="row">Moving money because a caller said so</th><td>Hang up and call 159 or use the number on your card. A genuine bank won't rush you. See <a href="scams-fraud.html">scams and fraud</a>.</td></tr>
<tr><th scope="row">Ignoring debt letters</th><td>Open them. Free, confidential help is available – see <a href="credit-scores-debt-help.html#help">free debt help</a>.</td></tr></tbody></table></div>
<p class="hint">These are general pointers, not advice for your situation.</p>
<p>See also: <a href="pay-tax-payslip.html">Pay, tax and your payslip</a> · <a href="savings.html">Savings</a> · <a href="insurance-basics.html">Insurance basics</a> · <a href="jargon.html">Jargon buster</a>.</p>
</div><aside><div class="card toc"><h3>On this page</h3><a href="#takehome">Take-home pay</a><a href="#steps">Four steps</a><a href="#rule">50/30/20 rule of thumb</a><a href="#emergency">Emergency funds</a><a href="#leaks">Plug the leaks</a><a href="#mistakes">Common mistakes</a></div></aside></div>'''))

pages["insurance-basics.html"] = page("insurance-basics.html", "Insurance basics: premiums, excess, motor, contents, travel and life cover – MoneyBySharma",
 "Insurance explained: what premium, excess and claim mean, the legal minimum for motor insurance, contents cover for renters, why a GHIC isn't travel insurance, life and income protection, and what the FSCS covers if an insurer fails.",
 ph("Insurance basics","Insurance basics","What the words mean, which cover is a legal requirement, and what you're protected by if an insurer fails. Information only – not advice."), W(f'''
<div class="cols"><div>
<div class="note" style="margin-top:1.5rem"><strong>Information only – not advice.</strong> MoneyBySharma isn't authorised by the FCA and doesn't recommend any insurer, policy or comparison site. This page summarises guidance from GOV.UK, MoneyHelper, the NHS and the FSCS. Always read a policy's key facts and exclusions.</div>

<h2 id="words">The key words</h2>
<div class="table-scroll"><table class="wrap-th"><caption class="sr">Insurance terms in plain English</caption><thead><tr><th scope="col">Word</th><th scope="col">What it means</th></tr></thead><tbody>
<tr><th scope="row">Premium</th><td>What you pay for cover, monthly or yearly.</td></tr>
<tr><th scope="row">Claim</th><td>Asking the insurer to pay out for a loss the policy covers.</td></tr>
<tr><th scope="row">Excess</th><td>A fixed amount you pay yourself when you claim. The insurer sets a compulsory excess; you can often add a <em>voluntary</em> excess to lower the premium, but you'll get less back when you claim.</td></tr>
<tr><th scope="row">Exclusions</th><td>What a policy doesn't cover. They vary between insurers, so read the small print.</td></tr></tbody></table></div>
<p>Give your insurer accurate, up-to-date information. MoneyHelper warns that getting details wrong, or not telling the insurer about changes, might mean the policy isn't valid and claims aren't paid. If you're struggling to pay a premium, contact your insurer rather than simply cancelling: MoneyHelper says insurers must support customers in financial difficulty.</p>
{sg("mhcar","mhlife")}

<h2 id="motor">Motor insurance</h2>
<ul><li><strong>It's a legal requirement.</strong> You must have motor insurance to drive on UK roads, and <strong>third party</strong> is the legal minimum. It covers injury or damage you cause to other people, vehicles, animals or property – but not repairs to your own vehicle.</li>
<li><strong>Three levels of cover:</strong> third party; third party, fire and theft (also covers your car if it's stolen or damaged by fire); and fully comprehensive (also pays for accidental damage to your own car). MoneyHelper notes that third party isn't necessarily the cheapest – compare prices.</li>
<li><strong>No-claims bonus.</strong> A discount for each year without a claim. MoneyHelper says claiming usually costs you two years' worth, so it's worth weighing up whether a claim is worthwhile after your excess.</li>
<li><strong>Insurance applies to the vehicle, not just driving.</strong> MoneyHelper says you generally need at least third party cover for a roadworthy vehicle even if you don't drive it, unless it's officially registered off the road (SORN).</li></ul>
{sg("vehins","mhcar")}

<h2 id="contents">Contents insurance (including if you rent)</h2>
<p>Contents insurance covers your own belongings – furniture, electricals, clothes, jewellery – against loss, theft and damage. MoneyHelper says you don't need <em>buildings</em> insurance if you rent (your landlord is responsible for the structure), but your landlord won't usually cover <strong>your</strong> belongings, so contents insurance is sensible depending on your circumstances. It's optional. In a house or flat share you usually need your own policy (insurers often require a lock on your bedroom door) or a joint policy for the whole property.</p>
{sg("mhrent")}

<h2 id="travel">Travel insurance</h2>
<ul><li>GOV.UK says you should take out appropriate travel insurance before you go, covering existing health conditions and the activities you'll do. Without it you could be liable for emergency treatment costing thousands of pounds – GOV.UK gives examples such as <strong>£25,000+</strong> for a broken leg needing hospital treatment in Spain.</li>
<li><strong>A GHIC is not travel insurance.</strong> The UK Global Health Insurance Card gives access to state-provided, medically necessary healthcare in the EU, Switzerland and some other countries on the same terms as residents. It doesn't cover private healthcare, repatriation or extras such as mountain rescue.</li>
<li>Check what's covered: the full length of your trip, emergency transport, pre-existing conditions, your activities and every country you pass through. Standard policies usually don't cover airline or travel-agent failure – ATOL-protected holidays or a policy with failure cover can.</li></ul>
{sg("fti","ghic")}

<h2 id="life">Life insurance and income protection</h2>
<div class="grid g2">
<div class="card"><h3>Life insurance</h3><p>Pays a lump sum or regular payments if you die, to support dependants such as children or a partner. MoneyHelper says it can suit you if you have dependants, a partner who relies on your income, or want loved ones to be able to cover funeral costs; you might not need it if you're single or your partner earns enough. Check whether your employer offers <strong>death in service</strong> cover.</p></div>
<div class="card"><h3>Income protection</h3><p>Pays regular income (typically 50% to 65% of your income, says MoneyHelper) if illness or an accident stops you working, until you return, retire or the policy ends. There's usually a waiting period before payments start. It's different from critical illness cover, which pays one lump sum.</p></div></div>
<p>For both, MoneyHelper says you can change your mind within <strong>30 days</strong> of buying and get a full refund, and you must answer medical questions honestly.</p>
{sg("mhlife","mhip")}

<h2 id="fscs">If your insurer fails: FSCS protection</h2>
<p>If a PRA-regulated insurer fails, the FSCS may protect eligible claims. It <strong>pays 100%</strong> of claims for compulsory insurance such as third-party motor, and for categories such as employers' liability, term life, income protection and annuities; it <strong>pays 90%</strong> for others, including first-party motor, home, travel, pet and health insurance. Some types, such as goods in transit, marine and aviation, aren't eligible. Cover is subject to conditions and limits.</p>
{sg("fscsins")}
<p>If you're unhappy with how an insurer handled a claim, complain to it first, then you may be able to go to the <a href="https://www.financial-ombudsman.org.uk/consumers/how-to-complain" rel="noopener">Financial Ombudsman Service</a>.</p>
<p>See also: <a href="budgeting-emergency-fund.html">Budgeting and emergency funds</a> · <a href="jargon.html">Jargon buster</a>.</p>
</div><aside><div class="card toc"><h3>On this page</h3><a href="#words">Key words</a><a href="#motor">Motor</a><a href="#contents">Contents</a><a href="#travel">Travel</a><a href="#life">Life &amp; income</a><a href="#fscs">If an insurer fails</a></div></aside></div>'''))
