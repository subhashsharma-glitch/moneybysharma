(function(){
 var f=document.getElementById('an-form');if(!f)return;
 var D=JSON.parse(document.getElementById('an-data').textContent),o=document.getElementById('an-out');
 function g(id){return document.getElementById(id)}
 function money(v){return '£'+Math.round(v).toLocaleString('en-GB')}
 function esc(s){return s.replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c]})}
 var srcLine='Source: <a href="'+D.url+'" target="_blank" rel="noopener">'+D.src+'</a>, quotes dated '+D.dated+'. Checked '+D.checked+'.';
 function na(msg){o.innerHTML='<div class="note an-na"><b>Estimate not available.</b> '+msg+' Get real quotes from <a href="https://comparison.moneyhelper.org.uk/en/tools/annuities" target="_blank" rel="noopener">MoneyHelper\'s annuity comparison tool</a> or a provider.</div><p class="src">'+srcLine+'</p>'}
 function run(){
  var pot=parseFloat(g('an-pot').value),age=parseInt(g('an-age').value,10),life=g('an-life').value,e=g('an-esc').value,gp=g('an-g').value,tfc=g('an-tfc').value==='yes';
  if(!(pot>0))return na('Enter your pension pot.');
  if(!(age>0))return na('Enter your age.');
  var buy=tfc?pot*0.75:pot,cash=pot-buy;
  if(age<55)return na('The published reference rates start at age 55, the usual minimum age for buying an annuity (57 from April 2028).');
  if(age>=80)return na('The published reference rates stop at age 75, so we can\'t give a reliable figure at '+age+'.');
  if(buy<10000)return na('The amount used to buy the annuity ('+money(buy)+') is below the £10,000 minimum several providers state, and the reference rates are for £100,000.');
  if(buy>1000000)return na('The reference rates are for a £100,000 purchase; very large purchases are priced individually.');
  var k=life+'|'+e+'|'+gp,r=D.rates[k];
  var names={level:'level',rpi:'RPI-linked','3pc':'rising 3% a year'};
  var desc=(life==='joint'?'joint life (50% to partner)':'single life')+', '+names[e]+', '+(gp==='0'?'no guarantee':gp+'-year guarantee');
  if(!r)return na('The published table doesn\'t include a '+esc(desc)+' annuity, and we don\'t invent adjustments. Options with an estimate: single life level (no guarantee or 5 years), single life RPI or 3% with 5 years, joint life level or 3% with no guarantee.');
  var i=0;for(var j=0;j<D.ages.length;j++){if(D.ages[j]<=age)i=j}
  var a=D.ages[i],per=r[i],ann=per*buy/100000;
  o.innerHTML='<div class="results an-res"><div class="res"><span>Estimated income per year (before tax)</span><b>'+money(ann)+'</b></div><div class="res"><span>Estimated income per month (before tax)</span><b>'+money(ann/12)+'</b></div>'+(tfc?'<div class="res"><span>Tax-free cash taken first</span><b>'+money(cash)+'</b></div>':'')+'</div>'+
   '<p class="an-est"><b>This is an estimate, not a quote.</b> Based on '+money(buy)+' buying a '+esc(desc)+' annuity, using the published figure of '+money(per)+' a year per £100,000 at age '+a+(a!==age?' (the nearest published age at or below '+age+')':'')+'.</p><p class="src">'+srcLine+'</p>';
 }
 f.addEventListener('input',run);f.addEventListener('change',run);f.addEventListener('submit',function(ev){ev.preventDefault()});run();
})();
