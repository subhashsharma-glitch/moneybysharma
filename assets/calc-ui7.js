/* Take-home pay illustration, 2026/27, England/Wales/Northern Ireland tax bands, standard 1257L code, monthly pay. */
(function(){var f=document.getElementById('tp-form');if(!f)return;
var SLT={none:0,p1:2241.66,p2:2448.75,p4:2816.25,p5:2083.33,pg:1750},SLR={p1:.09,p2:.09,p4:.09,p5:.09,pg:.06};
function v(i){return parseFloat(document.getElementById(i).value)}
function t(i,s){document.getElementById(i).textContent=s}
function neg(x){return (x>0?'−':'')+money(x)}
function money(x){return '£'+x.toLocaleString('en-GB',{minimumFractionDigits:2,maximumFractionDigits:2})}
function calc(sal,pct,scheme,plan){
 var m=sal/12,qual=Math.max(0,Math.min(sal,50270)-6240),empG=pct/100*qual/12,pen=empG*12;
 var ani=sal-(scheme==='net'?pen:0),pa=Math.max(0,12570-Math.max(0,ani-100000)/2),ti=Math.max(0,ani-pa);
 var tax=.2*Math.min(ti,37700)+.4*Math.max(0,Math.min(ti,125140)-37700)+.45*Math.max(0,ti-125140);tax/=12;
 var ni=.08*(Math.min(Math.max(m,1048),4189)-1048)+.02*Math.max(0,m-4189);
 var sl=0;if(plan!=='none'&&m>SLT[plan])sl=Math.floor((m-SLT[plan])*SLR[plan]);
 var penDed=scheme==='net'?empG:empG*.8,emp=.03*qual/12;
 return{m:m,tax:tax,ni:ni,sl:sl,penDed:penDed,net:m-tax-ni-sl-penDed,pensionTotal:empG+emp,relief:scheme==='net'?0:empG*.2}}
window.MBSPay=calc;
function run(){var sal=v('tp-sal'),pct=v('tp-pen');if(!(sal>=0)||!(pct>=0)||pct>100){['tp-tax','tp-ni','tp-pen-o','tp-sl','tp-net','tp-year','tp-ptot'].forEach(function(i){t(i,'–')});return}
 var r=calc(sal,pct,document.getElementById('tp-scheme').value,document.getElementById('tp-plan').value);
 t('tp-gross',money(r.m));t('tp-tax',neg(r.tax));t('tp-ni',neg(r.ni));t('tp-pen-o',neg(r.penDed));t('tp-sl',neg(r.sl));t('tp-net',money(r.net));t('tp-year',money(r.net*12));t('tp-ptot',money(r.pensionTotal))}
f.addEventListener('input',run);f.addEventListener('change',run);f.addEventListener('submit',function(e){e.preventDefault();run()});run()})();
