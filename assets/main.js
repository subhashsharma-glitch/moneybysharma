(function(){var b=document.querySelector('.menu-btn'),n=document.getElementById('nav');if(b&&n){b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)})}})();
window.gbp=function(v,dp){return '£'+Number(v).toLocaleString('en-GB',{minimumFractionDigits:dp==null?2:dp,maximumFractionDigits:dp==null?2:dp})};
window.pct=function(v,dp){return (v*100).toFixed(dp==null?2:dp)+'%'};
document.addEventListener('click',function(e){document.querySelectorAll('nav.main details[open]').forEach(function(d){if(!d.contains(e.target))d.removeAttribute('open')})});
document.addEventListener('keydown',function(e){if(e.key==='Escape')document.querySelectorAll('nav.main details[open]').forEach(function(d){d.removeAttribute('open');d.querySelector('summary').focus()})});
