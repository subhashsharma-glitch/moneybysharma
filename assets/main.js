(function(){var b=document.querySelector('.menu-btn'),n=document.getElementById('nav'),h=document.querySelector('header.site');if(b&&n){b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);if(h)h.classList.toggle('menu-open',o)})}})();
/* Small screens: Guides groups fold into an accordion (the group holding the current page starts open) */
(function(){var mq=window.matchMedia&&window.matchMedia('(max-width:959.98px)'),hs=[].slice.call(document.querySelectorAll('nav.main .dd-h'));if(!mq||!hs.length)return;
function tog(h){var li=h.parentNode,o=li.classList.toggle('open');h.setAttribute('aria-expanded',o)}
function sync(){hs.forEach(function(h){var li=h.parentNode;if(mq.matches){li.classList.add('acc');if(li.querySelector('a[aria-current=page]'))li.classList.add('open');h.setAttribute('role','button');h.tabIndex=0;h.setAttribute('aria-expanded',li.classList.contains('open'))}else{li.classList.remove('acc','open');h.removeAttribute('role');h.removeAttribute('tabindex');h.removeAttribute('aria-expanded')}})}
hs.forEach(function(h){h.addEventListener('click',function(){if(mq.matches)tog(h)});h.addEventListener('keydown',function(e){if(mq.matches&&(e.key==='Enter'||e.key===' ')){e.preventDefault();tog(h)}})});
if(mq.addEventListener)mq.addEventListener('change',sync);else if(mq.addListener)mq.addListener(sync);sync()})();
window.gbp=function(v,dp){return '£'+Number(v).toLocaleString('en-GB',{minimumFractionDigits:dp==null?2:dp,maximumFractionDigits:dp==null?2:dp})};
window.pct=function(v,dp){return (v*100).toFixed(dp==null?2:dp)+'%'};
document.addEventListener('click',function(e){document.querySelectorAll('nav.main details[open]').forEach(function(d){if(!d.contains(e.target))d.removeAttribute('open')})});
document.addEventListener('keydown',function(e){if(e.key==='Escape')document.querySelectorAll('nav.main details[open]').forEach(function(d){d.removeAttribute('open');d.querySelector('summary').focus()})});
(function(){function ext(root){(root.querySelectorAll?root:document).querySelectorAll('a[href^="http"]:not([data-ext])').forEach(function(a){a.setAttribute('data-ext','');var h=a.hostname.toLowerCase();if(h==='moneybysharma.co.uk'||/\.moneybysharma\.co\.uk$/.test(h)||h===location.hostname)return;a.target='_blank';a.rel='noopener noreferrer';if(!a.querySelector('.sr-nt')){var s=document.createElement('span');s.className='sr sr-nt';s.textContent=' (opens in new tab)';a.appendChild(s)}})}
window.mbsExtLinks=ext;ext(document);new MutationObserver(function(ms){ms.forEach(function(m){m.addedNodes.forEach(function(n){if(n.nodeType===1)ext(n.parentNode||n)})})}).observe(document.body,{childList:true,subtree:true})})();
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('summary .dd-link');if(!a)return;e.preventDefault();var d=a.closest('details');d.open=!d.open});

/* wide tables: show a "scroll sideways" hint on any .table-scroll whose table is wider than its box */
(function(){var boxes=[].slice.call(document.querySelectorAll('.table-scroll'));if(!boxes.length)return;
 boxes.forEach(function(b){var h=document.createElement('span');h.className='scroll-hint';h.hidden=true;h.setAttribute('aria-hidden','true');h.textContent='Scroll sideways to see all columns \u2192';b.parentNode.insertBefore(h,b);b._hint=h;
  b.addEventListener('scroll',function(){if(b.scrollLeft+b.clientWidth>=b.scrollWidth-2)b._hint.textContent='\u2190 Scroll back for the first columns';else b._hint.textContent='Scroll sideways to see all columns \u2192'},{passive:true})});
 function check(){boxes.forEach(function(b){var more=b.scrollWidth>b.clientWidth+2;b.classList.toggle('has-more',more);b._hint.hidden=!more})}
 check();addEventListener('resize',check);addEventListener('load',check);setTimeout(check,800);
 if(window.MutationObserver)boxes.forEach(function(b){new MutationObserver(check).observe(b,{childList:true,subtree:true})});})();
