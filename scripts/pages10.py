# Students guide (exec'd from build.py). Sources checked 14 Oct 2026.
C10 = "14 October 2026"
S10 = {
 "sfnew": ("GOV.UK – Student finance: new full-time students (2026 to 2027 amounts)", "https://www.gov.uk/student-finance/new-fulltime-students"),
 "sfrepay": ("GOV.UK – Repaying your student loan: how much you repay", "https://www.gov.uk/repaying-your-student-loan/what-you-pay"),
 "sfwo": ("GOV.UK – Repaying your student loan: when it gets written off", "https://www.gov.uk/repaying-your-student-loan/when-your-student-loan-gets-written-off-or-cancelled"),
 "plan": ("GOV.UK – Repaying your student loan: which repayment plan you're on", "https://www.gov.uk/repaying-your-student-loan/which-repayment-plan-you-are-on"),
 "p5int": ("GOV.UK/SLC – How interest is calculated: Plan 5", "https://www.gov.uk/guidance/how-interest-is-calculated-plan-5"),
 "extra": ("GOV.UK – Extra money from your university or college (bursaries and hardship funds)", "https://www.gov.uk/extra-money-pay-university/university-and-college-hardship-funds"),
 "dsa": ("GOV.UK – Disabled Students' Allowance: what you'll get", "https://www.gov.uk/disabled-students-allowance-dsa/what-youll-get"),
 "sfw": ("Student Finance Wales", "https://www.studentfinancewales.co.uk/"),
 "saas": ("Student Awards Agency Scotland (SAAS)", "https://www.saas.gov.uk/"),
 "sfni": ("Student Finance NI", "https://www.studentfinanceni.co.uk/"),
 "ps1916": ("FCA – PS19/16: High-Cost Credit Review, overdrafts policy statement (rules in force 6 April 2020)", "https://www.fca.org.uk/publications/policy-statements/ps19-16-high-credit-review-overdrafts"),
 "ofmob": ("Ofcom – Switching mobile phone provider (Text to Switch)", "https://www.ofcom.org.uk/phones-and-broadband/switching-provider/switching-mobile-phone-provider"),
 "ofecn": ("Ofcom – Companies must tell customers about their best deals (end-of-contract notifications)", "https://www.ofcom.org.uk/phones-and-broadband/service-quality/companies-must-tell-customers-about-their-best-deals"),
 "ofchk": ("Ofcom – Broadband and mobile coverage checker", "https://checker.ofcom.org.uk/"),
 "rc1625": ("16-25 Railcard (official Railcards website, National Rail)", "https://www.16-25railcard.co.uk/"),
 "rc1617": ("16-17 Saver (official Railcards website, National Rail)", "https://www.16-17saver.co.uk/"),
 "nx": ("National Express – Young Persons Coachcard", "https://www.nationalexpress.com/en/offers/coachcards/young-person"),
 "tsbus": ("Transport Scotland – Under 22s free bus travel", "https://www.transport.gov.scot/concessionary-travel/young-persons-free-bus-travel-scheme/"),
 "totum": ("TOTUM (official website)", "https://www.totum.com/"),
 "unidays": ("UNiDAYS (official website)", "https://www.myunidays.com/GB/en-GB"),
 "beans": ("Student Beans (official website)", "https://www.studentbeans.com/uk"),
}
def s10(*k): return '<p class="src">Sources (checked ' + C10 + '): ' + "; ".join(f'<a href="{S10[x][1]}" rel="noopener">{S10[x][0]}</a>' for x in k) + ".</p>"
pages["students.html"] = page("students.html","Students: money guide – MoneyBySharma",
 "UK student money explained: 2026/27 tuition fee and maintenance loans, Plan 5 repayments, grants, bursaries and DSA, student overdrafts, phones and Wi-Fi, railcards, discounts and hardship funds.",
 ph("Students","Students","Student finance for 2026/27, how repayments work, bank accounts, phones, travel, discounts and help if money gets tight. Information only – not advice."), W(f'''
<div class="cols"><div>
<div class="note" style="margin-top:1.5rem"><strong>Information only – not advice.</strong> This page explains how things work. It doesn't recommend any lender, bank, network or discount scheme, and it has no affiliate links. Figures are for England unless stated; always check the official source before you decide anything.</div>

<h2 id="funding">University funding (England, 2026/27)</h2>
<p>Students from England apply to Student Finance England (SFE). There are two main loans, and you have to pay both back.</p>
<div class="table-scroll"><table><thead><tr><th>Loan</th><th>2026 to 2027 maximum</th></tr></thead><tbody>
<tr><td>Tuition Fee Loan, full-time course</td><td>Up to <strong>£9,790</strong></td></tr>
<tr><td>Tuition Fee Loan, accelerated degree</td><td>Up to <strong>£11,750</strong></td></tr>
<tr><td>Maintenance Loan, living with parents</td><td>Up to <strong>£9,118</strong></td></tr>
<tr><td>Maintenance Loan, away from parents, outside London</td><td>Up to <strong>£10,830</strong></td></tr>
<tr><td>Maintenance Loan, away from parents, in London</td><td>Up to <strong>£14,135</strong></td></tr>
<tr><td>Maintenance Loan, year of a UK course studying abroad</td><td>Up to <strong>£12,403</strong></td></tr>
</tbody></table></div>
<ul>
<li><strong>Tuition Fee Loan</strong> is paid straight to your university or college, which sets the fee.</li>
<li><strong>Maintenance Loan</strong> is paid into your bank account at the start of each term. How much you get depends on where you live and your household income, so many students get less than the maximum. From 2026/27, care leavers' household income isn't used, so they can choose the maximum.</li>
<li>You reapply every year, and must update your account if your living arrangements change.</li>
<li>GOV.UK notes that student finance is changing for courses starting on or after 1 January 2027.</li>
</ul>
{s10("sfnew")}

<h3>Wales, Scotland and Northern Ireland</h3>
<p>If you normally live elsewhere in the UK, you apply to your own nation's funding body, which has its own amounts, grants and rules. These differ from England's, so check there rather than using the figures above:</p>
<ul>
<li><strong>Wales:</strong> <a href="{S10["sfw"][1]}" rel="noopener">Student Finance Wales</a></li>
<li><strong>Scotland:</strong> <a href="{S10["saas"][1]}" rel="noopener">Student Awards Agency Scotland (SAAS)</a></li>
<li><strong>Northern Ireland:</strong> <a href="{S10["sfni"][1]}" rel="noopener">Student Finance NI</a></li>
</ul>
<p>Your loan's repayment plan also depends on where you're from and when you started. For example, GOV.UK says postgraduate students from Northern Ireland are on Plan 1 and those from Scotland are on Plan 4.</p>
{s10("sfw","saas","sfni","sfwo")}

<h2 id="repay">Repaying: Plan 5</h2>
<p>Students from England starting an undergraduate course on or after 1 August 2023 are on <strong>Plan 5</strong>. Repayments depend on income, not on how much you owe.</p>
<div class="grid g2">
<div class="card"><h3>Plan 5 thresholds</h3><ul><li><strong>£25,000</strong> a year</li><li><strong>£2,083</strong> a month</li><li><strong>£480</strong> a week</li></ul></div>
<div class="card"><h3>How much and how long</h3><ul><li>You repay <strong>9%</strong> of income over the threshold.</li><li>Interest is currently <strong>4.1%</strong> and is added even when you aren't repaying.</li><li>Any balance left is written off <strong>40 years</strong> after the April you were first due to repay.</li></ul></div>
</div>
<p><strong>Example (worked from the GOV.UK figures):</strong> pay of £2,500 a month is £417 over the £2,083 monthly threshold. 9% of £417 is about £37 a month.</p>
<p>For comparison, GOV.UK lists other plan thresholds as £26,900 (Plan 1), £29,385 (Plan 2), £33,795 (Plan 4) and £21,000 (Postgraduate Loan, repaid at 6%).</p>
{s10("plan","sfrepay","sfwo","p5int")}

<h2 id="grants">Grants, bursaries and DSA</h2>
<ul>
<li><strong>Bursaries, scholarships and awards.</strong> Each university or college sets its own rules on who qualifies, how much and how to apply. The money is paid to you directly and you don't usually pay it back. Ask your student support service.</li>
<li><strong>Extra help.</strong> GOV.UK lists extra support if, for example, you have children, pay for childcare, have an adult who depends on you, or are under 25 and estranged from your parents. Some courses, such as nursing or social work, have their own funding.</li>
<li><strong>Disabled Students' Allowance (DSA).</strong> Covers study-related costs because of a mental health problem, long-term illness, learning difficulty such as dyslexia, or other disability. It isn't means-tested and you <strong>don't pay it back</strong>. Undergraduates and postgraduates can get up to <strong>£27,783 a year</strong>. It can pay for specialist equipment, non-medical helpers, some taxi travel and other study support. You'll have a needs assessment first. If you're assessed as needing a new computer, you pay the first <strong>£200</strong>. Don't buy equipment before you're assessed – it won't be reimbursed.</li>
</ul>
{s10("extra","sfnew","dsa")}

<h2 id="bank">Student bank accounts and overdrafts</h2>
<p>Many banks offer a student current account. The main feature is usually an <strong>interest-free arranged overdraft</strong> – a limit you can borrow up to without paying interest while you study.</p>
<ul>
<li><strong>It's still borrowing.</strong> You have to pay it back. The limit is usually set by the bank, can be lower in your first year, and may depend on a credit check.</li>
<li><strong>Stay inside the limit.</strong> Going past it can mean payments are refused. How you manage an overdraft shows on your credit file.</li>
<li><strong>After graduation.</strong> Banks usually convert the account to a graduate account, and the interest-free limit tends to shrink over time. Once interest is charged, overdrafts can be expensive. Since 6 April 2020, FCA rules mean banks charge a single annual interest rate on overdrafts, with no fixed daily or monthly fees, and arranged and unarranged overdrafts are priced the same.</li>
<li><strong>Compare the terms, not the freebies.</strong> Look at the interest-free limit in each year, how long it lasts after you graduate, and the rate charged afterwards.</li>
</ul>
<p>See our <a href="bank-accounts.html">bank accounts guide</a> and <a href="credit-scores-debt-help.html">credit scores guide</a> for more.</p>
{s10("ps1916")}

<h2 id="phones">Mobile and broadband</h2>
<ul>
<li><strong>SIM-only plans.</strong> If you already own a phone, a SIM-only plan pays for calls, texts and data only. They are often available on a 30-day rolling contract as well as 12 or 24 months.</li>
<li><strong>Contract length versus term time.</strong> An academic year is roughly 9 to 10 months, and you may move each year. A 12, 18 or 24-month contract can outlast your tenancy, and leaving early usually means early-termination charges. A rolling contract gives more flexibility, often at a higher monthly price.</li>
<li><strong>Halls Wi-Fi.</strong> Most halls include internet in the rent. Check this before you buy home broadband, and check coverage at your new address with <a href="{S10["ofchk"][1]}" rel="noopener">Ofcom's checker</a>.</li>
<li><strong>Switching.</strong> You can switch mobile provider and keep your number by texting your current provider (Text to Switch). Providers must also tell you when your contract is ending.</li>
</ul>
<p>More detail on contracts, price rises and switching: <a href="broadband-phones.html">Broadband &amp; phones guide</a>.</p>
{s10("ofmob","ofecn","ofchk")}

<h2 id="travel">Travel</h2>
<div class="table-scroll"><table><thead><tr><th>Card</th><th>Who</th><th>Discount</th><th>Price</th></tr></thead><tbody>
<tr><td><strong>16-25 Railcard</strong></td><td>Aged 16 to 25, and mature students in full-time study</td><td>1/3 off most rail fares, including Advance. £12 minimum fare Monday to Friday, 04:30 to 09:59. No season tickets.</td><td><strong>£35</strong> for 1 year, <strong>£80</strong> for 3 years</td></tr>
<tr><td><strong>16-17 Saver</strong></td><td>Aged 16 or 17</td><td>50% off Standard Anytime, Off-Peak, Advance and Season tickets, with no time restrictions or minimum fare. Not valid on ScotRail.</td><td><strong>£35</strong> for 1 year</td></tr>
<tr><td><strong>Young Persons Coachcard</strong> (National Express)</td><td>Aged 16 to 26, or a full-time student</td><td>1/3 off Standard and Fully Flexible fares</td><td>Check the official page – prices shown differed when we checked</td></tr>
</tbody></table></div>
<ul>
<li>You can buy a 1-year 16-25 Railcard up to the day before your 26th birthday, and a 3-year card up to the day before your 24th birthday.</li>
<li>A 16-17 Saver bought from 17 August 2026 lasts a full year, even if you turn 18 while it's valid.</li>
<li><strong>Young person bus schemes.</strong> In Scotland, everyone aged 5 to 21 who lives there can travel free on most buses with a National Entitlement Card. Elsewhere in the UK, young person bus discounts are set locally by councils, transport authorities and bus operators, so check with yours.</li>
</ul>
{s10("rc1625","rc1617","nx","tsbus")}

<h2 id="discounts">Student discounts</h2>
<p>Three widely used schemes in the UK (listed alphabetically, not ranked):</p>
<ul>
<li><a href="{S10["beans"][1]}" rel="noopener">Student Beans</a> – an app and website where verified students get discount codes from retailers.</li>
<li><a href="{S10["totum"][1]}" rel="noopener">TOTUM</a> – a student discount card (formerly the NUS Extra card), with free and paid options.</li>
<li><a href="{S10["unidays"][1]}" rel="noopener">UNiDAYS</a> – an app and website where verified students get retailer discounts.</li>
</ul>
<p>A discount only saves money on something you were going to buy anyway. Many retailers also offer their own student discount directly.</p>
{s10("beans","totum","unidays")}

<h2 id="budget">Budgeting and hardship</h2>
<ul>
<li><strong>Plan by term.</strong> Your Maintenance Loan arrives at the start of each term, so divide it by the number of weeks until the next payment.</li>
<li><strong>Fixed costs first.</strong> Pay rent and essential bills first, then food and travel. What's left is for everything else.</li>
<li><strong>Track your spending.</strong> Banking apps and simple spreadsheets can show where money is going.</li>
<li><strong>Check you get everything you're entitled to.</strong> Bursaries and extra grants aren't always automatic.</li>
</ul>
<p><strong>Hardship funds.</strong> If you're struggling, your university or college may give you extra money from its hardship fund. GOV.UK lists examples of students who may qualify, such as student parents (especially single parents), mature students, students from low-income families, disabled students, care leavers and students who are homeless. Your university decides who qualifies and how much. The money is paid as a lump sum or in instalments and usually doesn't have to be paid back, though sometimes it's a loan. Contact your student services department.</p>
<p>If debts are building up, free help is listed on our <a href="credit-scores-debt-help.html#help">debt help page</a>.</p>
{s10("extra")}
<p>See also: <a href="bank-accounts.html">Bank accounts</a> · <a href="broadband-phones.html">Broadband &amp; phones</a> · <a href="savings.html">Savings</a> · <a href="jargon.html">Jargon buster</a>.</p>
</div><aside><div class="card toc"><h3>On this page</h3><a href="#funding">University funding</a><a href="#repay">Repaying: Plan 5</a><a href="#grants">Grants and DSA</a><a href="#bank">Student bank accounts</a><a href="#phones">Mobile and broadband</a><a href="#travel">Travel</a><a href="#discounts">Discounts</a><a href="#budget">Budgeting and hardship</a></div></aside></div>'''))
