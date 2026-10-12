(function(){
  var C=window.MBSCalc;function v(id){return parseFloat(document.getElementById(id).value)}function set(id,t){document.getElementById(id).textContent=t}
  function on(form,fn){if(!form)return;form.addEventListener('input',fn);form.addEventListener('submit',function(e){e.preventDefault();fn()});fn()}
  // Fees
  on(document.getElementById('fee-form'),function(){
    var r=C.fees(v('fee-start'),v('fee-growth'),Math.round(v('fee-years')),v('fee-pct'),v('fee-flat'));
    set('fee-r-pct',gbp(r.pct,0));set('fee-r-flat',gbp(r.flat,0));set('fee-r-none',gbp(r.noFees,0));
    set('fee-r-text','Over '+Math.round(v('fee-years'))+' years the percentage fee costs about '+gbp(r.pctCost,0)+' and the flat fee about '+gbp(r.flatCost,0)+' (including lost growth), compared with no fees.');
  });
  // Mortgage
  var cv=document.getElementById('mort-chart');
  function draw(bal){if(!cv)return;var dpr=window.devicePixelRatio||1,w=cv.clientWidth,h=cv.clientHeight;cv.width=w*dpr;cv.height=h*dpr;var x=cv.getContext('2d');x.scale(dpr,dpr);x.clearRect(0,0,w,h);
    var pl=58,pb=28,pt=10,pr=10,max=bal[0]||1,n=bal.length-1||1;x.font='12px system-ui';x.fillStyle='#4a5a57';x.strokeStyle='#dfe5e2';
    for(var i=0;i<=4;i++){var yy=pt+(h-pt-pb)*i/4;x.beginPath();x.moveTo(pl,yy);x.lineTo(w-pr,yy);x.stroke();x.fillText('£'+Math.round(max*(1-i/4)/1000)+'k',4,yy+4)}
    var step=Math.max(1,Math.ceil(n/8));for(var j=0;j<=n;j+=step){x.fillText('Yr '+j,pl+(w-pl-pr)*j/n-12,h-8)}
    x.beginPath();bal.forEach(function(b,k){var px=pl+(w-pl-pr)*k/n,py=pt+(h-pt-pb)*(1-b/max);k?x.lineTo(px,py):x.moveTo(px,py)});
    x.strokeStyle='#0f4c45';x.lineWidth=3;x.stroke();x.lineTo(pl+(w-pl-pr),h-pb);x.lineTo(pl,h-pb);x.closePath();x.fillStyle='rgba(23,107,96,.12)';x.fill()}
  var last;on(document.getElementById('mort-form'),function(){
    var type=document.getElementById('mort-type').value,r=C.mortgage(v('mort-amt'),v('mort-rate'),v('mort-years'),type,v('mort-over')||0);
    set('mort-r-monthly',gbp(r.monthly));set('mort-r-int',gbp(r.totalInterest,0));
    var y=Math.floor(r.months/12),m=r.months%12;set('mort-r-term',type==='interest'?gbp(r.balanceAtEnd,0)+' owed at end':y+' yrs'+(m?' '+m+' mths':''));
    document.getElementById('mort-r-term-label').textContent=type==='interest'?'Balance still owed':'Time to clear';
    last=r.yearlyBalance;draw(last);
    set('mort-chart-desc','Chart: outstanding balance falls from '+gbp(last[0],0)+' to '+gbp(last[last.length-1],0)+' over '+(last.length-1)+' years.');
  });window.addEventListener('resize',function(){last&&draw(last)});
  // Gilts
  var gsel=document.getElementById('gilt-pick');
  if(gsel){fetch('data/gilts.json').then(function(r){return r.json()}).then(function(j){var now=new Date().toISOString().slice(0,10);
    j.gilts.filter(function(g){return g.maturity>now}).forEach(function(g){var o=document.createElement('option');o.value=g.coupon+'|'+g.maturity;o.textContent=g.name+' (matures '+g.maturity+')';gsel.appendChild(o)});
    document.getElementById('gilt-src').textContent='Gilt list: '+j.source+', close of business '+j.closeOfBusiness+' (fetched '+j.fetched+').'});
    gsel.addEventListener('change',function(){if(!gsel.value)return;var p=gsel.value.split('|');document.getElementById('gilt-coupon').value=p[0];document.getElementById('gilt-mat').value=p[1];gfn()})}
  function gfn(){var mat=document.getElementById('gilt-mat').value;if(!mat)return;var md=new Date(mat+'T00:00:00Z');var t=new Date();var s=new Date(Date.UTC(t.getFullYear(),t.getMonth(),t.getDate()));
    if(md<=s){set('gilt-r-gry','–');return}
    var r=C.gilt(v('gilt-price'),v('gilt-coupon'),md,parseFloat(document.getElementById('gilt-band').value),s);
    set('gilt-r-gry',pct(r.gry));set('gilt-r-net',pct(r.netYield));set('gilt-r-eq',isNaN(r.equivGross)?'–':pct(r.equivGross));
    set('gilt-r-text','Accrued interest about £'+r.accrued.toFixed(2)+' per £100 nominal, so the dirty price is about £'+r.dirty.toFixed(2)+'. Years to maturity: '+r.years.toFixed(2)+'.')}
  on(document.getElementById('gilt-form'),gfn);
})();
