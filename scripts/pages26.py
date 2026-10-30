# pages26.py – "How we cut our home insurance by £160 with one phone call" (PREVIEW, 30 Oct 2026).
# Subhash approved adding the article; he must OK the preview before it goes live.
# Going live = set HI_LIVE = True in scripts/build.py and rebuild. That flag:
#   * adds the page to the Guides menu ("Borrowing & protection"), * adds Article schema (pages23 GUIDES),
#   * runs this script before the SEO pass so it joins site search, * drops noindex and adds it to the sitemap.
# Personal figures come from our own Halifax renewal letter and quotes (Oct 2026); rules link to the FCA Handbook.
_HI = "home-insurance-renewal.html"
_S = lambda u, t: f'<a href="{u}">{t}</a>'
_R65 = "https://www.handbook.fca.org.uk/handbook/ICOBS/6/5.html"
_R6B = "https://www.handbook.fca.org.uk/handbook/ICOBS/6B/2.html"
_CHK = "checked 30 October 2026"
_PREV = "" if HI_LIVE else '''<div class="card" style="border-left:5px solid #d9822b;margin-top:1rem"><strong>Preview, not live.</strong> Hidden from search engines, the sitemap, site search and menus. To confirm before publishing: the "about 20%" rise (needs last year's premium from the renewal letter) and "twenty minutes of comparing".</div>'''
pages[_HI] = page(_HI, "How We Cut Our Home Insurance by £160 With One Call",
  "Our home insurance renewal rose about 20%. We compared quotes, removed cover we didn't need and rang our insurer. The steps and call script we used.",
  ph("Home insurance renewal", "How we cut our home insurance by £160 with one phone call",
     "Our renewal price jumped by about 20%. Twenty minutes of comparing and one polite phone call later, we were paying £160 less with the same insurer. Here's exactly what we did, so you can try it too. Information, not financial advice.") + W(_PREV + f'''
<p>When our home insurance renewal letter from Halifax arrived, the number on it was £528.49 for the year. That included £55.08 for home emergency cover, and it was around 20% more than we'd paid the year before. Nothing about our home had changed. We hadn't claimed. It was simply the price going up because we hadn't asked questions.</p>
<p>So we decided to ask some.</p>

<h2 id="compare">What we found when we compared</h2>
<p>We ran a comparison on Compare the Market and got 42 quotes back. The lowest started from £247 with Lemonade, but that came with a £250 excess, meaning we'd pay the first £250 of any claim ourselves.</p>
<p>Looking a little further up the list made things clearer:</p>
<ul>
<li><strong>Lemonade (lowest price):</strong> from £247, £250 excess</li>
<li><strong>Lemonade Super:</strong> £289, £100 excess</li>
<li><strong>Lemonade Epic:</strong> £386, including accidental damage, legal cover and home emergency</li>
</ul>
<p class="hint">These were the quotes we were offered in October 2026 for our home. Yours will be different.</p>
<p>To keep on top of it all, we used Grok Bot, an AI assistant, as a helper. It ran the comparison quotes, laid the cover out side by side (excesses, away-from-home cover, accidental damage, legal expenses) and helped us prepare a short script for calling our insurer. It was genuinely useful for the fiddly comparing, but we still checked the details ourselves, made the call and made the decision.</p>
<p>We also spotted something on our own policy: we were still paying to cover an expensive item we no longer needed covering. Removing it was an easy win.</p>

<h2 id="call">The phone call</h2>
<p>Armed with real quotes, we rang Halifax. We explained that our renewal had gone up by about 20%, that we'd found comparable cover for less, and asked what they could do.</p>
<p>The new price: <strong>£30.71 a month, roughly £368.52 a year.</strong> That's about <strong>£160 less</strong> than the renewal letter. After confirming the cover was what we needed, we chose to stay. Staying wasn't the goal; getting a fair price for the cover we wanted was.</p>

<h2 id="steps">How to do it yourself</h2>
<ol>
<li><strong>Check your renewal against last year.</strong> Since April 2017, your renewal notice must show last year's premium next to the new one so you can compare them. And since 1 January 2022, for home and motor insurance, your renewal price can't be higher than the price the insurer would charge an equivalent new customer. If your price has gone up and nothing has changed, that's your cue. Sources: {_S(_R65, "FCA Handbook ICOBS 6.5.1R")} and {_S(_R6B, "FCA Handbook ICOBS 6B.2.1R")} ({_CHK}).</li>
<li><strong>Remove cover you don't need.</strong> Look at specified items, add-ons and extras. Things you've sold or no longer own may still be on there.</li>
<li><strong>Compare quotes with accurate answers.</strong> Use a comparison site or two, and answer every question honestly. A cheap quote based on wrong details could leave you with a claim that isn't paid.</li>
<li><strong>Compare the cover, not just the price.</strong> Check the excess, the claim limits (including single-item limits), and add-ons like accidental damage, away-from-home cover, legal expenses and home emergency.</li>
<li><strong>Call your insurer and ask.</strong> Tell them what you've found and ask if they can match it or improve their price. Ask for the retentions or renewals team if needed.</li>
<li><strong>Check annual vs monthly cost.</strong> Paying monthly can include interest, so ask for both figures and compare the total over 12 months.</li>
<li><strong>Never let your old policy lapse before the new one starts.</strong> If you switch, make sure the new cover starts on the day the old one ends, with no gap.</li>
</ol>

<div class="card" style="background:#e7f2ef;border-left:5px solid #d9822b;margin:1.5rem 0">
<p><strong>Our short call script</strong></p>
<p>"Hi, I've just received my home insurance renewal and it's gone up by around 20%. I've compared quotes and found similar cover for less, for example [quote and insurer]. I'd like to stay with you if possible. Is there anything you can do on the price? I'd also like to remove [item] as I no longer need it covered. Could you tell me the annual price and the monthly price, and whether monthly includes interest?"</p></div>

<h2 id="takeaway">The takeaway</h2>
<p>Loyalty doesn't always pay, but a phone call often does. Our £160 saving took a bit of comparing and a few minutes on the phone. Your result may be bigger, smaller, or you may find switching is the better option. The point is to check rather than let renewal happen automatically.</p>
<p>New to insurance terms like excess and premium? See {_S("insurance-basics.html", "Insurance basics")}.</p>

<p class="hint" style="margin-top:1.5rem">Information, not financial advice. Savings vary depending on your home, circumstances and insurer. This article shares our own experience. Always check policy documents carefully before you buy or change cover.</p>'''))
if not HI_LIVE:
    PREVIEW_PAGES.add(_HI)
    pages[_HI] = pages[_HI].replace('<link rel="icon"', '<meta name="robots" content="noindex"><link rel="icon"', 1)
