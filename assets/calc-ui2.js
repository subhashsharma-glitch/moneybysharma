(function(){
  var C=window.MBSCalc;function v(id){return parseFloat(document.getElementById(id).value)}function set(id,t){var e=document.getElementById(id);if(e)e.textContent=t}
  function on(f,fn){if(!f)return;f.addEventListener('input',fn);f.addEventListener('submit',function(e){e.preventDefault();fn()});fn()}
  function bars(cv,labels,vals,fmt){if(!cv)return;var dpr=window.devicePixelRatio||1,w=cv.clientWidth,h=cv.clientHeight;cv.width=w*dpr;cv.height=h*dpr;var x=cv.getContext('2d');x.scale(dpr,dpr);x.clearRect(0,0,w,h);
    var max=Math.max.apply(null,vals)||1,pb=28,pt=22,n=vals.length,bw=(w-20)/n;x.font='12px system-ui';x.textAlign='center';
    vals.forEach(function(val,k){var bh=(h-pt-pb)*val/max,bx=10+k*bw+bw*0.15;x.fillStyle=k===0?'#d9822b':'#176b60';x.fillRect(bx,h-pb-bh,bw*0.7,bh);x.fillStyle='#14211f';x.fillText(fmt(val),bx+bw*0.35,h-pb-bh-6);x.fillStyle='#4a5a57';x.fillText(labels[k],bx+bw*0.35,h-8)})}
  window.MBSbars=bars;
  // Pensions
  var pf=document.getElementById('pen-form'),last;
  on(pf,function(){var start=Math.round(v('pen-start')),r=C.pension(start,67,v('pen-monthly'),v('pen-growth'),v('pen-fee'),v('pen-infl'));
    set('pen-r-pot',gbp(r.pot,0));set('pen-r-real',gbp(r.real,0));set('pen-r-paid',gbp(r.paid,0));
    var ages=[18,25,35,45].filter(function(a){return a<67}),vals=ages.map(function(a){return C.pension(a,67,v('pen-monthly'),v('pen-growth'),v('pen-fee'),v('pen-infl')).real});
    last=[ages.map(function(a){return 'Start '+a}),vals];bars(document.getElementById('pen-chart'),last[0],vals,function(x){return gbp(x/1000,0)+'k'});
    set('pen-chart-desc','Bar chart of pot at 67 in today\'s money: '+ages.map(function(a,k){return 'start at '+a+' '+gbp(vals[k],0)}).join(', ')+'.')});
  window.addEventListener('resize',function(){last&&bars(document.getElementById('pen-chart'),last[0],last[1],function(x){return gbp(x/1000,0)+'k'})});
  // Battery
  on(document.getElementById('bat-form'),function(){var r=C.battery(v('bat-kwh'),v('bat-eff'),v('bat-cheap'),v('bat-peak'),v('bat-cycles'),v('bat-cost'),Math.round(v('bat-life')),v('bat-degr'));
    set('bat-r-annual',gbp(r.annual,0));set('bat-r-payback',r.annual<=0?'Never':(r.payback===null?'Not within lifespan':r.payback.toFixed(1)+' years'));set('bat-r-net',gbp(r.net,0));
    set('bat-r-text','Each full cycle saves about '+gbp(r.perCycle)+'. Simple payback ignoring degradation: '+(r.annual>0?(r.simplePayback).toFixed(1)+' years':'never')+'. Lifetime saving after degradation: '+gbp(r.lifetimeSaving,0)+'.')});
  // EV
  on(document.getElementById('ev-form'),function(){var r=C.ev(v('ev-miles'),v('ev-eff'),v('ev-home'),v('ev-public'),v('ev-share'));
    set('ev-r-home',r.homePpm.toFixed(1)+'p');set('ev-r-public',r.publicPpm.toFixed(1)+'p');set('ev-r-annual',gbp(r.annual,0));
    set('ev-r-text','Blended cost about '+r.blendedPpm.toFixed(1)+'p a mile.')});
})();
