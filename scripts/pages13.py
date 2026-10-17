# Explained Simply: Money Matters – viewable page (exec'd from build.py). Page images are made by scripts/pdf_pages.py.
ES_PAGES = ["Cover", "Your payslip, decoded", "Tax, NI &amp; minimum pay", "Budgeting that sticks", "Bank accounts &amp; paying", "Saving &amp; interest",
 "Where to keep savings", "Borrowing &amp; credit", "Student loans, simply", "Pensions, simply", "Insurance &amp; investing", "Scams &amp; fraud",
 "Money words, decoded", "Mistakes everyone makes", "Keep these numbers handy"]
_toc = "".join(f'<li><a href="#page-{i}">{t}</a> <span class="hint">· page {i}</span></li>' for i, t in enumerate(ES_PAGES, 1))
_imgs = "".join(f'<figure id="page-{i}"><img src="assets/explained-simply/page-{i:02d}.webp" width="1125" height="1407" loading="{"eager" if i == 1 else "lazy"}" decoding="async" alt="Page {i} of 15 of Explained Simply: Money Matters: {t}. The full text is in the PDF download."><figcaption>Page {i} of 15 · {t}</figcaption></figure>' for i, t in enumerate(ES_PAGES, 1))
pages["explained-simply-money-matters.html"] = page("explained-simply-money-matters.html", "Explained Simply: Money Matters – free illustrated guide – MoneyBySharma",
 "Explained Simply: Money Matters is a free 15-page illustrated guide to UK money by MoneyBySharma, covering payslips, tax, budgeting, savings, borrowing, student loans, pensions and scams. Read it here or download the PDF.",
 ph('<a href="resources.html">Resources</a> › Explained Simply: Money Matters', "Explained Simply: Money Matters", "A free illustrated guide to UK money by MoneyBySharma. Read it on this page, or download the PDF."), W(f'''
<p class="cs-actions"><a class="btn" href="assets/explained-simply-money-matters.pdf" download>Download the PDF (1.7 MB)</a> <a href="#page-1">Start reading</a> <a href="resources.html">Back to Resources</a></p>
<div style="max-width:760px"><p>Explained Simply: Money Matters is a 15-page illustrated guide, by MoneyBySharma, to the basics of UK money: payslips and tax, budgeting, bank accounts, saving and ISAs, borrowing, student loans, pensions, insurance, investing and scams. Figures were checked in October 2026 for the 2026/27 tax year (England).</p>
<p class="hint">Information only, not financial advice. The pages below are images of the PDF so they look the same on every device. For the full text, selectable and with its links, download the PDF.</p>
<h2 id="inside">What's inside</h2><ol class="es-toc">{_toc}</ol></div>
<h2 id="read">Read the guide</h2>
<div class="es-pages">{_imgs}</div>
<p class="cs-actions"><a class="btn" href="assets/explained-simply-money-matters.pdf" download>Download the PDF (1.7 MB)</a> <a href="#main">Back to the top</a> <a href="resources.html">Back to Resources</a></p>'''))
