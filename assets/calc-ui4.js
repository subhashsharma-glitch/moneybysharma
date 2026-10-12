(function(){var f=document.getElementById('bt-form');if(!f)return;function v(i){var x=parseFloat(document.getElementById(i).value);return isFinite(x)?x:0}
function run(){var r=MBSCalc.btSave(v('bt-bal'),v('bt-fee'),Math.round(v('bt-months')),v('bt-apr'),v('bt-pay'));
document.getElementById('bt-feeo').textContent=gbp(r.fee,2);document.getElementById('bt-int').textContent=gbp(r.interestAvoided,2);
var s=document.getElementById('bt-save');s.textContent=(r.saving<0?'−':'')+gbp(Math.abs(r.saving),2)+(r.saving<0?' (costs more)':'');
document.getElementById('bt-left').textContent=gbp(r.btLeft,2)}
f.addEventListener('input',run);f.addEventListener('submit',function(e){e.preventDefault();run()});run()})();
