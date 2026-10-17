(function(){var f=document.getElementById('gr-form');if(!f)return;
function v(i){return parseFloat(document.getElementById(i).value)}
function t(i,s){document.getElementById(i).textContent=s}
function money(x){return '£'+x.toLocaleString('en-GB',{minimumFractionDigits:2,maximumFractionDigits:2})}
function yrs(x){return (Math.round(x*10)/10).toFixed(1)+' years'}
function run(){var a=v('gr-amt'),r=v('gr-rate')/100,y=v('gr-years'),n=parseInt(document.getElementById('gr-freq').value,10);
if(!(a>=0)||!(r>=0)||!(y>=0)){['gr-simple','gr-comp','gr-aer','gr-r72','gr-exact'].forEach(function(i){t(i,'–')});return}
t('gr-simple',money(a*(1+r*y)));t('gr-comp',money(a*Math.pow(1+r/n,n*y)));
t('gr-aer',(r>0?((Math.pow(1+r/n,n)-1)*100).toFixed(2)+'%':'0.00%'));
if(r>0){t('gr-r72',yrs(72/(r*100)));t('gr-exact',yrs(Math.log(2)/(n*Math.log(1+r/n))))}else{t('gr-r72','–');t('gr-exact','–')}}
f.addEventListener('input',run);f.addEventListener('change',run);f.addEventListener('submit',function(e){e.preventDefault();run()});run()})();
