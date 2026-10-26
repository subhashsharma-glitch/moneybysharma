# Credit cards page (exec'd from build.py)
S.update({
 "s75": ("legislation.gov.uk – Consumer Credit Act 1974, section 75", "https://www.legislation.gov.uk/ukpga/1974/39/section/75"),
 "ccms": ("FCA – Credit Card Market Study, Annex 2: how credit card products are regulated (section 75 range over £100 to £30,000; representative APR 51% test)", "https://www.fca.org.uk/publication/market-studies/ms14-6-2-ccms-annex-2.pdf"),
 "conc35": ("FCA Handbook – CONC 3.5 Financial promotions about credit agreements (representative APR)", "https://handbook.fca.org.uk/handbook/conc3/conc3s5"),
 "conc67": ("FCA Handbook – CONC 6.7 persistent debt rules (CONC 6.7.27R onwards)", "https://handbook.fca.org.uk/handbook/conc6/conc6s7"),
 "ps184": ("FCA – PS18/4: Credit card market study, persistent debt and earlier intervention (rules from 1 March 2018)", "https://www.fca.org.uk/publication/policy/ps18-04.pdf"),
 "icocredit": ("ICO – Credit: your information and credit reference agencies", "https://ico.org.uk/for-the-public/credit/"),
})
CARDS = [("American Express","https://www.americanexpress.com/en-gb/credit-cards/"),("Bank of Scotland","https://www.bankofscotland.co.uk/creditcards.html"),
 ("Barclaycard","https://www.barclaycard.co.uk/personal/credit-cards"),("Capital One","https://www.capitalone.co.uk/"),("The Co-operative Bank","https://www.co-operativebank.co.uk/products/credit-cards/"),
 ("first direct","https://www.firstdirect.com/loans-and-cards/credit-cards/"),("Halifax","https://www.halifax.co.uk/creditcards.html"),("HSBC UK","https://www.hsbc.co.uk/credit-cards/"),
 ("Lloyds","https://www.lloydsbank.com/credit-cards.html"),("M&amp;S Bank","https://www.marksandspencer.com/c/money/credit-card"),("MBNA","https://www.mbna.co.uk/credit-cards.html"),
 ("Nationwide","https://www.nationwide.co.uk/credit-cards"),("NatWest","https://www.natwest.com/credit-cards.html"),("Royal Bank of Scotland","https://www.rbs.co.uk/credit-cards.html"),
 ("Santander","https://www.santander.co.uk/personal/credit-cards"),("Tesco Bank","https://www.tescobank.com/credit-cards/"),("TSB","https://www.tsb.co.uk/credit-cards.html"),
 ("Vanquis","https://www.vanquis.com/credit-cards/"),("Virgin Money","https://uk.virginmoney.com/cards/"),("Zopa","https://www.zopa.com/credit-card"),("Aqua","https://www.aquacard.co.uk/")]
CARDS.sort(key=lambda c: c[0].lower())
_cl = "".join(f'<li><a href="{u}" rel="noopener">{n}</a></li>' for n,u in CARDS)
BC,HS,SA,TE = "https://www.barclaycard.co.uk/personal/credit-cards","https://www.hsbc.co.uk/credit-cards/","https://www.santander.co.uk/personal/credit-cards","https://www.tescobank.com/credit-cards/"
CCHK, CCHK_SHORT = "26 October 2026", "26 Oct 2026"  # offers below checked on providers' own pages on this date
DEALS = [("Balance transfer","Barclaycard Platinum",BC,"0% on balance transfers for up to 35 months (transfers within 60 days); 0% on purchases for 3 months","3.15% per transfer","24.9% APR representative (variable)"),
 ("Balance transfer","HSBC UK Balance Transfer Credit Card",HS,"0% on balance transfers for up to 36 months","3.09% (minimum £5)","25.9% APR representative (variable), assumed limit £1,200"),
 ("Balance transfer","Tesco Bank Balance Transfer Credit Card",TE,"0% on balance transfers for 35 months; 0% on money transfers for 9 months","3.15% balance transfers; 3.99% money transfers","24.9% APR representative (variable), limit £1,200"),
 ("Balance transfer","Santander Everyday Long Term Balance Transfer",SA,"0% on balance transfers for 34 months; 0% on purchases for 3 months","3.15% (minimum £5)","24.9% APR representative (variable), assumed limit £1,200"),
 ("Purchases","Barclaycard Platinum (purchases)",BC,"0% on purchases for up to 24 months; 0% on balance transfers for up to 21 months","3.45% per transfer","24.9% APR representative (variable)"),
 ("Purchases and transfers","Tesco Bank Balance Transfer and Purchases",TE,"0% on purchases and balance transfers for 21 months","2.95% balance transfers","24.9% APR representative (variable), limit £1,200"),
 ("Cashback","Santander Rewards Credit Card",SA,"3% cashback on petrol, everyday travel, eating out and takeaways in the first year; 0.25% on other purchases; no foreign exchange fees on purchases abroad","No monthly fee","24.9% APR representative (variable), assumed limit £1,200"),
 ("Rewards (Avios)","Barclaycard Avios",BC,"1 Avios per £1 on eligible purchases","No monthly fee","29.9% APR representative (variable)"),
 ("Cashback / travel","Barclaycard Rewards",BC,"0.25% cashback on eligible purchases; no fees abroad","–","28.9% APR representative (variable)")]
_dl = "".join(f'<tr><td>{t}</td><td><a href="{u}" rel="noopener">{n}</a></td><td>{o}</td><td>{fe}</td><td>{a}</td></tr>' for t,n,u,o,fe,a in DEALS)
pages["credit-cards.html"] = page("credit-cards.html","Credit cards and deals – MoneyBySharma",
 "How UK credit cards work: card types, representative APR, minimum payments, persistent debt rules, credit checks, Section 75, balance transfer fee maths, an A–Z of card providers and dated offers.",
 ph("Credit cards","Credit cards and deals","How credit cards work, what protects you, how to check the cost of a balance transfer, and an A–Z of card providers. Factual information only – we don't rate or recommend any card."), W(f'''
<div class="cols"><div>
<div class="note" style="margin-top:1.5rem"><strong>Information only – not advice.</strong> MoneyBySharma has no affiliation with, and receives no payment or commission from, any card provider or comparison site, and none of the links here are affiliate links. Nothing here is a recommendation or an invitation to apply. Offers depend on your circumstances and change often, so always check the current terms with the provider.</div>
<div class="note" role="note" style="border-left-color:#b3261e"><strong>Borrowing costs money.</strong> Only borrow what you can afford to repay. Missing payments can lead to fees, more interest and damage to your credit record. If you're worried about debt, free and confidential help is available from <a href="https://www.moneyhelper.org.uk/" rel="noopener">MoneyHelper</a>, <a href="https://www.stepchange.org/" rel="noopener">StepChange</a> and <a href="https://nationaldebtline.org/" rel="noopener">National Debtline</a>.</div>
<h2 id="types">Types of card</h2>
<ul>
<li><strong>0% balance transfer.</strong> You move debt from another card and pay no interest on it for an introductory period. There's usually a one-off fee, a percentage of the amount moved, and you often have to make the transfer within a set number of days.</li>
<li><strong>0% purchase.</strong> No interest on new spending for an introductory period. After that, the standard rate applies to whatever is still owed.</li>
<li><strong>Money transfer.</strong> Sends money from the card into your bank account, usually for a fee. It's often treated differently from purchases.</li>
<li><strong>Cashback and rewards.</strong> These pay back a percentage of your spending, or points such as supermarket points or Avios (airline points used by British Airways and others). The rewards are usually worth far less than the interest if you carry a balance.</li>
<li><strong>Credit-builder.</strong> Lower limits and usually higher rates, for people with a short or poor credit history. Paying on time can help build a record.</li>
<li><strong>Travel / no foreign-fee cards.</strong> These don't add a foreign transaction fee when you spend abroad. Cash withdrawals may still cost money.</li>
</ul>
<h2 id="how">How credit cards work</h2>
<ul>
<li><strong>Representative APR.</strong> The APR includes interest and compulsory fees. "Representative" means the lender expects at least 51% of people accepted through that advert to get that rate or lower. Up to 49% may be offered a higher rate, a lower limit or a shorter 0% period.</li>
<li><strong>Interest-free period on purchases.</strong> If you pay the full statement balance by the due date, most cards charge no interest on purchases. This doesn't normally apply to cash withdrawals or balance transfers.</li>
<li><strong>Minimum payments.</strong> Paying only the minimum keeps your account in order. But most of each payment can go on interest, so the debt takes much longer, and costs much more, to clear.</li>
<li><strong>Cash withdrawals.</strong> Usually a cash fee and a higher interest rate that starts straight away, with no interest-free period.</li>
<li><strong>Late and over-limit fees.</strong> Missing a payment or going over your limit can lead to a fee, losing a 0% deal and a mark on your credit file. The fee amounts are in each card's summary box.</li>
<li><strong>Persistent debt rules (FCA, from 1 March 2018).</strong> If over 18 months you've paid more in interest, fees and charges than you've repaid of the borrowing itself, your card provider must contact you and suggest paying more if you can. If that's still the case after 36 months, the provider must offer ways to repay the balance in a reasonable time, usually 3 to 4 years. If you can't afford more, it must show forbearance, for example by reducing or waiving interest. The card may then be suspended.</li>
</ul>
{src("conc35","ccms","conc67","ps184")}
<h2 id="credit">Credit scores and eligibility checkers</h2>
<ul>
<li><strong>Three credit reference agencies (CRAs):</strong> <a href="https://www.equifax.co.uk/" rel="noopener">Equifax</a>, <a href="https://www.experian.co.uk/" rel="noopener">Experian</a> and <a href="https://www.transunion.co.uk/" rel="noopener">TransUnion</a>. Lenders may use one or more. You can get your statutory credit report free from each.</li>
<li><strong>Soft search:</strong> used by eligibility checkers and for some quotes. Lenders can't see it, and it doesn't affect your credit score.</li>
<li><strong>Hard search:</strong> made when you actually apply. Other lenders can see it, and several in a short time can make it harder to get credit.</li>
<li>Eligibility checkers show how likely you are to be accepted, using a soft search. They're not a guarantee, unless a card is described as "pre-approved".</li>
</ul>
{src("icocredit")}
<h2 id="protection">Protection: Section 75 and chargeback</h2>
<ul>
<li><strong>Section 75 of the Consumer Credit Act 1974.</strong> If you pay at least partly by credit card for a single item or service costing over £100 and up to £30,000, the card provider is jointly liable with the seller if the seller breaches the contract or misrepresents the goods. That covers cases such as goods not arriving or the firm going bust. It applies even if you put only part of the cost on the card.</li>
<li><strong>Chargeback.</strong> Chargeback isn't a legal right. It's a voluntary process under the card scheme rules (Visa, Mastercard and others) for asking your card provider to reverse a payment. It works on debit cards too and has no minimum amount, but there are strict time limits.</li>
<li>If your provider rejects a valid claim, you can complain to it and then to the <a href="https://www.financial-ombudsman.org.uk/" rel="noopener">Financial Ombudsman Service</a>.</li>
</ul>
{src("s75","ccms")}
<h2 id="safe">Using cards safely</h2>
<ul>
<li><strong>Pay in full by Direct Debit</strong> if you can. You won't miss a payment, and you won't pay interest on purchases.</li>
<li>If you can't pay in full, set the Direct Debit for more than the minimum.</li>
<li><strong>Know when 0% ends</strong> and what rate applies afterwards. New spending on a balance transfer card may not be at 0%.</li>
<li><strong>Do the balance transfer maths.</strong> A 3% fee on £3,000 is £90, paid up front. That's only worth it if you'd otherwise pay more than £90 in interest over the period.</li>
</ul>
<h3 id="calc">Balance transfer calculator</h3>
<p>Compares the one-off transfer fee with the interest you'd pay on your current card over the same number of months, making the same monthly payment. <strong>The values filled in are examples only, not real offers</strong> – change them to match your own figures.</p>
<form id="bt-form" class="calc fields" style="margin:.6rem 0">
<div><label for="bt-bal">Balance to transfer (£)</label><input id="bt-bal" type="number" value="3000" min="0" step="100"></div>
<div><label for="bt-apr">Current card APR (%)</label><input id="bt-apr" type="number" value="24.9" min="0" step="0.1"></div>
<div><label for="bt-fee">Transfer fee (%)</label><input id="bt-fee" type="number" value="3" min="0" step="0.01"></div>
<div><label for="bt-months">0% period (months)</label><input id="bt-months" type="number" value="24" min="1" max="60"></div>
<div><label for="bt-pay">Monthly payment (£)</label><input id="bt-pay" type="number" value="100" min="0" step="10"></div>
<div style="grid-column:1/-1" class="results" aria-live="polite"><div class="res"><span>Transfer fee</span><b id="bt-feeo">–</b></div><div class="res"><span>Interest on current card over the period</span><b id="bt-int">–</b></div><div class="res"><span>Difference (interest minus fee)</span><b id="bt-save">–</b></div><div class="res"><span>Left to pay when 0% ends</span><b id="bt-left">–</b></div></div>
<p class="hint" style="grid-column:1/-1">This is an illustration, not a quote. It assumes your current card's APR stays the same and is charged monthly, that no new spending goes on either card, that you're accepted for the full transfer, and that the fee is added to the new balance. Your actual offer, fee and 0% period depend on the lender's assessment of you.</p></form>
<h2 id="providers">Card providers A–Z</h2>
<p>Each link goes to the provider's own credit card page, checked on {CHECKED}. This list isn't complete, and the order says nothing about price or quality. We don't show ratings.</p>
<ul style="columns:2;max-width:560px;column-gap:2rem">{_cl}</ul>
<h2 id="deals">Offers seen on providers' own pages</h2>
<p>These figures were copied from each provider's own credit cards page on <strong>{CCHK}</strong>. They're a factual snapshot, not a recommendation. "Up to" means some people get a shorter 0% period. You may be offered a different rate, limit or 0% period, or be declined, depending on your circumstances. Offers change often and can end without notice, so check the provider's page and summary box for current terms.</p>
<div class="table-scroll"><table><caption class="sr">Credit card offers seen on {CCHK}</caption><thead><tr><th scope="col">Type</th><th scope="col">Card (source)</th><th scope="col">Introductory offer / feature</th><th scope="col">Transfer or account fee</th><th scope="col">Representative APR</th></tr></thead><tbody>{_dl}</tbody></table></div>
<p class="hint">Checked {CCHK_SHORT}. Offers we couldn't confirm on a provider's own page have been left out.</p>
<p>See also: <a href="bank-accounts.html">Bank accounts</a> (overdrafts and switching) · <a href="jargon.html">Jargon buster</a>.</p>
</div><aside><div class="card toc"><h3>On this page</h3><a href="#types">Card types</a><a href="#how">How cards work</a><a href="#credit">Credit checks</a><a href="#protection">Section 75 &amp; chargeback</a><a href="#safe">Using cards safely</a><a href="#calc">Transfer calculator</a><a href="#providers">Providers A–Z</a><a href="#deals">Offers seen</a><a href="bank-accounts.html">Bank accounts</a><a href="jargon.html">Jargon buster</a></div></aside></div>'''), scripts=("calc.js","calc-ui4.js"))
