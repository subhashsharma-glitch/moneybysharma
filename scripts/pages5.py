# Bank accounts page (exec'd from build.py)
S.update({
 "fscsbb": ("FSCS – Banks, building societies and credit unions (limit, shared licences, temporary high balances)", "https://www.fscs.org.uk/what-we-cover/banks-building-societies/"),
 "bba": ("FCA – Basic bank accounts: the problems we found and how industry is committing to change", "https://www.fca.org.uk/publications/good-and-poor-practice/basic-bank-accounts-problems-industry-committing-change"),
 "bbahmt": ("GOV.UK/HM Treasury – Basic bank accounts: July 2023 to June 2024 (5 Nov 2025)", "https://www.gov.uk/government/publications/basic-bank-accounts-july-2023-to-june-2024/basic-bank-accounts-july-2023-to-june-2024"),
 "cass": ("Current Account Switch Service – The switching process and common questions", "https://www.currentaccountswitch.co.uk/the-switching-process-personal/"),
 "cassq": ("Current Account Switch Service – Common questions (personal)", "https://www.currentaccountswitch.co.uk/common-questions-personal/"),
 "payuk": ("Pay.UK – Current Account Switch Service (redirection period)", "https://www.wearepay.uk/what-we-do/switching-services/current-account-switch-service/"),
 "ps1916": ("FCA – PS19/16: High-Cost Credit Review, overdrafts policy statement (rules in force 6 April 2020)", "https://www.fca.org.uk/publications/policy-statements/ps19-16-high-credit-review-overdrafts"),
 "conc5c": ("FCA Handbook – CONC 5C Overdraft pricing", "https://handbook.fca.org.uk/handbook/conc5c"),
 "ipsos": ("Ipsos – Personal banking service quality, Great Britain (published August 2026, survey July 2025 – June 2026)", "https://www.ipsos.com/en-uk/personal-banking-service-quality-great-britain-august-2026"),
})
BANKS = [("Bank of Scotland","https://www.bankofscotland.co.uk/bankaccounts.html","High street"),("Barclays","https://www.barclays.co.uk/current-accounts/","High street"),
 ("Chase UK","https://www.chase.co.uk/gb/en/","App"),("The Co-operative Bank","https://www.co-operativebank.co.uk/products/bank-accounts/current-account/","High street"),
 ("first direct","https://www.firstdirect.com/banking/current-account/","Phone and app"),("Halifax","https://www.halifax.co.uk/bankaccounts/current-accounts.html","High street"),
 ("HSBC UK","https://www.hsbc.co.uk/current-accounts/","High street"),("Lloyds","https://www.lloydsbank.com/current-accounts.html","High street"),
 ("Metro Bank","https://www.metrobankonline.co.uk/bank-accounts/products/current-account/","High street"),("Monzo","https://monzo.com/current-account","App"),
 ("Nationwide","https://www.nationwide.co.uk/current-accounts/","Building society"),("NatWest","https://www.natwest.com/current-accounts.html","High street"),
 ("Revolut","https://www.revolut.com/bank-account/","App"),("Royal Bank of Scotland","https://www.rbs.co.uk/current_accounts.html","High street"),
 ("Santander","https://www.santander.co.uk/personal/current-accounts","High street"),("Starling Bank","https://www.starlingbank.com/current-account/","App"),
 ("TSB","https://www.tsb.co.uk/current-accounts.html","High street"),("Virgin Money","https://uk.virginmoney.com/current-accounts/","High street (part of Nationwide)")]
_bl = "".join(f'<tr><td><a href="{u}" rel="noopener">{n}</a></td><td>{k}</td></tr>' for n,u,k in BANKS)
BON = [("Barclays","https://www.barclays.co.uk/current-accounts/","Up to £300: £150 + £150","Barclays Bank Account. Apply in the app within 21 days, switch, and pay in a salary of at least £2,000 within 30 days to get £150. A further £150 if you keep using the account for five months, including 10 eligible debit card payments a month. New customers, 18+, UK residents."),
 ("first direct","https://www.firstdirect.com/banking/current-account/","£210 (£175 + £35 boost)","1st Account. Within 45 days of opening: full switch using CASS (at least 2 Direct Debits or standing orders), pay in £1,000, make 5+ debit card payments, and log on to digital banking. New customers only. Not available if you've opened an HSBC current account since 1 January 2018."),
 ("HSBC UK","https://www.hsbc.co.uk/current-accounts/","£220","HSBC Bank Account (Basic Bank Account not eligible). Open the account in the app and, within 60 days, complete a full switch using CASS (including 2 Direct Debits), pay in £2,000 and spend £500 on your debit card. New customers only."),
 ("Lloyds","https://www.lloydsbank.com/current-accounts.html","£200","New Club Lloyds, Club Lloyds Silver, Club Lloyds Platinum or Premier account. Switch using CASS with at least 3 active Direct Debits. Some of these accounts have monthly fees. Offer ends 9 December 2026."),
 ("Nationwide","https://www.nationwide.co.uk/current-accounts/switch","£175","New or existing FlexDirect, FlexAccount or FlexPlus. Full switch using CASS from a non-Nationwide or non-Virgin Money account with at least 2 Direct Debits, completed within 28 days. Pay in £1,000 and make 1 debit card payment within 31 days."),
 ("NatWest","https://www.natwest.com/current-accounts.html","£200","Switch a current account held elsewhere to a Select or Reward account. The bank's page says T&Cs and restrictions apply – read the full terms on its site.")]
_bon = "".join(f'<tr><td><a href="{u}" rel="noopener">{n}</a></td><td>{a}</td><td>{c}</td></tr>' for n,u,a,c in BON)
pages["bank-accounts.html"] = page("bank-accounts.html","Bank accounts – MoneyBySharma",
 "UK current accounts explained: account types, basic bank accounts, switching with CASS, £120,000 FSCS protection, overdraft rules, an A–Z of banks and how switching bonuses work.",
 ph("Bank accounts","Bank accounts","Types of current account, how switching works, how your money is protected, overdraft rules, and an A–Z of banks. A neutral list – we don't rate or recommend anyone."), W(f'''
<div class="cols"><div>
<div class="note" style="margin-top:1.5rem"><strong>Information only – not advice.</strong> MoneyBySharma has no affiliation with, and receives no payment or commission from, any bank, building society or app. Nothing here is a recommendation. Accounts, fees and offers change often, so always check the current terms with the provider before you apply.</div>
<h2 id="types">Types of account</h2>
<ul>
<li><strong>Current account.</strong> Your everyday account for wages, bills, card payments and transfers. Many have no monthly fee.</li>
<li><strong>Packaged account.</strong> You pay a monthly fee for extras such as travel, phone or breakdown insurance. Work out whether you'd use, and are eligible for, each benefit. Compare the yearly fee with what the cover would cost you separately, and check you aren't already covered elsewhere.</li>
<li><strong>Joint account.</strong> Shared by two (or sometimes more) people. Each holder can usually withdraw all the money. Each is also responsible for the full overdraft. A joint account creates a <em>financial association</em> on your credit files, so a lender may look at the other person's record too. When the account closes, the association stays until you ask the credit reference agencies to remove it.</li>
<li><strong>Student and graduate accounts.</strong> These are for people in higher education. They usually come with an interest-free arranged overdraft, which shrinks after you graduate. Check when the free overdraft ends and what it costs after that.</li>
<li><strong>Basic bank account.</strong> This has no overdraft and no fees for standard operations, including a failed payment. It lets you receive money, pay bills by Direct Debit and use a debit card. Under the Payment Accounts Regulations 2015, nine designated providers must offer one to people who are legally resident in the UK and either don't have a UK bank account or aren't eligible for the provider's other accounts. The nine are Barclays UK, The Co-operative Bank, HSBC UK, Lloyds Banking Group (including Halifax and Bank of Scotland), Nationwide Building Society, NatWest Group (including RBS and Ulster Bank), Santander UK, TSB and Virgin Money UK (now a brand of Nationwide). For contracts entered into on or after 28 April 2026, a provider must give 90 days' notice and a specific reason before closing a basic account.</li>
<li><strong>Business account.</strong> If you run a business, its money should usually be kept separate. Business accounts often charge fees for transactions. For FSCS purposes, a limited company has its own £120,000 limit, but a sole trader's personal and business money is added together.</li>
</ul>
{src("bba","bbahmt","fscsbb")}
<h2 id="switch">Switching with the Current Account Switch Service (CASS)</h2>
<ul>
<li><strong>7 working days.</strong> You pick a switch date with your new bank (not a weekend or bank holiday) and allow 7 working days. Your Direct Debits, standing orders and incoming payments move across automatically.</li>
<li><strong>Your old account closes.</strong> A full switch closes your old account. Until the switch date you can still use it, but don't set up new payments on it in the 7 working days before.</li>
<li><strong>Redirection.</strong> Payments still sent to your old account are redirected to the new one, and the sender is told your new details automatically. Pay.UK says redirection lasts at least three years, or longer if it's still needed.</li>
<li><strong>The Current Account Switch Guarantee.</strong> If something goes wrong in the switch, any interest or charges it causes on either account are refunded.</li>
<li><strong>Overdrafts.</strong> An overdraft doesn't move automatically. Agree any overdraft with the new bank before you start the switch.</li>
</ul>
{src("cass","cassq","payuk")}
<h2 id="fscs">FSCS deposit protection: £120,000</h2>
<p>On <strong>1 December 2025</strong> the FSCS deposit limit rose from £85,000 to <strong>£120,000 per eligible person, per bank, building society or credit union</strong>. If a UK-authorised firm fails, the FSCS aims to pay you within seven working days, and you don't need to claim.</p>
<ul>
<li><strong>The limit is per banking licence, not per brand.</strong> Some brands share one licence and count as one bank. For example, Halifax is a division of Bank of Scotland plc, and first direct is a division of HSBC UK Bank plc. You can check which brands share a licence on the Financial Services Register or with the FSCS checker.</li>
<li><strong>Joint accounts:</strong> each holder is covered up to £120,000.</li>
<li><strong>Temporary high balances:</strong> money from certain life events, such as a house sale, an inheritance or an insurance payout, is protected up to £1.4 million for six months from when it was first deposited.</li>
<li>App providers: check the provider is a UK-authorised bank. Money held with an e-money firm isn't covered by the FSCS in the same way.</li>
</ul>
<p>See also our <a href="savings.html#fscs">savings guide</a>.</p>
{src("fscsbb")}
<h2 id="overdrafts">Overdrafts and fees</h2>
<ul>
<li><strong>Arranged overdraft:</strong> a borrowing limit agreed with your bank in advance.</li>
<li><strong>Unarranged overdraft:</strong> when you go overdrawn without an agreed limit, or beyond it. Banks can refuse the payment instead.</li>
<li><strong>The 2020 FCA rules.</strong> Since 6 April 2020, banks have had to charge for overdrafts using a single, simple annual interest rate. There are no daily or monthly overdraft fees, and no fees for arranging an overdraft of up to £10,000. The unarranged rate can't be higher than the arranged rate. Overdrafts are advertised with an APR, so you can compare them.</li>
<li><strong>Buffers:</strong> some accounts give an interest-free amount, such as the first few hundred pounds of an arranged overdraft. Interest is charged only on borrowing above it.</li>
<li><strong>Failed (refused) payment fees:</strong> these are still allowed, but the FCA says they should reasonably reflect the bank's cost of refusing the payment. Basic bank accounts can't charge them.</li>
</ul>
<p>Borrowing on a credit card instead? See <a href="credit-cards.html">Credit cards and deals</a>.</p>
{src("ps1916","conc5c")}
<h2 id="providers">Banks and building societies A–Z</h2>
<p>Each link goes to the provider's own current account page, checked on {CHECKED}. This list isn't complete, and the order says nothing about price or quality. We don't show fees, rates or ratings.</p>
<div class="table-scroll"><table><caption class="sr">Current account providers</caption><thead><tr><th scope="col">Provider</th><th scope="col">Type</th></tr></thead><tbody>{_bl}</tbody></table></div>
<p>To compare service, the 17 largest providers in Great Britain must publish independent survey results run by Ipsos, as required by the Competition and Markets Authority (CMA). The survey asks customers whether they would recommend each provider's overall service, online and mobile banking, branches and overdrafts. The latest results, published in August 2026, cover July 2025 to June 2026. They're updated every February and August. <a href="{S["ipsos"][1]}" rel="noopener">See the Ipsos service quality results</a>.</p>
{src("ipsos")}
<h2 id="bonuses">Deals and switching bonuses</h2>
<p>Some banks pay a cash bonus when you move your account using CASS. The usual conditions are:</p>
<ul>
<li>you must use a <em>full</em> switch (closing your old account)</li>
<li>you must move a minimum number of Direct Debits</li>
<li>you must pay in a set amount, sometimes a salary</li>
<li>you may need to make some card payments within a deadline</li>
<li>you usually mustn't have held an account with that bank, or its sister brands, before.</li>
</ul>
<p>Bonuses are paid only once the conditions are met, they can be withdrawn at any time, and they change often. Opening an account usually involves a credit check. A bonus is only one factor, alongside fees, overdraft costs and service.</p>
<p><strong>Offers seen on banks' own pages on {CHECKED}</strong> (a summary only; read the full terms on the bank's site):</p>
<div class="table-scroll"><table><caption class="sr">Switching offers seen on 12 October 2026</caption><thead><tr><th scope="col">Bank (source)</th><th scope="col">Bonus</th><th scope="col">Main conditions as stated by the bank</th></tr></thead><tbody>{_bon}</tbody></table></div>
<p class="hint">We may not have seen every offer. Offers can end without notice, so the bank's own page is the only reliable source. Inclusion here isn't a recommendation.</p>
</div><aside><div class="card toc"><h3>On this page</h3><a href="#types">Account types</a><a href="#switch">Switching (CASS)</a><a href="#fscs">FSCS protection</a><a href="#overdrafts">Overdrafts &amp; fees</a><a href="#providers">Providers A–Z</a><a href="#bonuses">Switching bonuses</a><a href="credit-cards.html">Credit cards</a><a href="jargon.html">Jargon buster</a></div></aside></div>'''))
