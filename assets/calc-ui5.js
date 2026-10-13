(function(){var f=document.getElementById('sp-form');if(!f)return;function v(i){var x=parseFloat(document.getElementById(i).value);return isFinite(x)&&x>0?x:0}
function band(n){return n<=30?'a basic fibre (FTTC) or 4G/5G connection may be enough':n<=80?'a superfast fibre (FTTC) or entry full fibre/cable package':n<=300?'a full fibre or cable package in the hundreds of Mbps':'a high-speed full fibre or cable package (500 Mbps+)'}
function run(){var r=MBSCalc.speedNeed(v('sp-people'),v('sp-hd'),v('sp-uhd'),v('sp-calls'),v('sp-games'),50);
document.getElementById('sp-base').textContent=Math.round(r.base)+' Mbps';document.getElementById('sp-need').textContent=Math.ceil(r.need)+' Mbps';document.getElementById('sp-band').textContent=band(r.need)}
f.addEventListener('input',run);f.addEventListener('submit',function(e){e.preventDefault();run()});run()})();
