(function(){var f=document.getElementById('rv-form');if(!f)return;function v(i){return parseFloat(document.getElementById(i).value)}
function run(){var a=v('rv-amt'),r=MBSCalc.realValue(a,v('rv-infl'),v('rv-rate'),Math.round(v('rv-years')));document.getElementById('rv-nom').textContent=gbp(r.nominal,0);document.getElementById('rv-real').textContent=gbp(r.real,0);document.getElementById('rv-loss').textContent=a>0?((1-r.real/r.nominal)*100).toFixed(1)+'%':'–'}
f.addEventListener('input',run);f.addEventListener('submit',function(e){e.preventDefault();run()});run()})();
