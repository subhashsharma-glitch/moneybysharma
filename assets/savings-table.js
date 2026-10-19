(function(){
  var root=document.getElementById('rates');if(!root)return;
  var TYPES={'easy-access':'Easy access','notice':'Notice','fixed':'Fixed bond','cash-isa':'Cash ISA','regular-saver':'Regular saver'};
  var MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  var data=[],sortKey='aer',dir=-1;
  var body=root.querySelector('tbody'),fType=document.getElementById('f-type'),fF=document.getElementById('f-fscs'),fMin=document.getElementById('f-min'),count=document.getElementById('rates-count');
  function term(r){if(r.termLabel)return r.termLabel;var m=r.termMonths;return m==null?'None':(m%12===0?(m/12)+(m===12?' year':' years'):m+' months')}
  function day(s){if(!s)return '–';var p=s.split('-');return (+p[2])+' '+MON[+p[1]-1]+' '+p[0]}
  function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
  function money(v){return v==null?'Not stated':gbp(v,0)}
  function td(l,h,c){return '<td data-label="'+l+'"'+(c?' class="'+c+'"':'')+'>'+h+'</td>'}
  function render(){
    var max=parseFloat(fMin.value);
    var rows=data.filter(function(r){return (!fType.value||r.type===fType.value)&&(!fF.checked||r.fscs)&&(isNaN(max)||r.minDeposit==null||r.minDeposit<=max)});
    rows.sort(function(a,b){var x=a[sortKey],y=b[sortKey];if(x==null)x=-1;if(y==null)y=-1;return (typeof x==='string'?x.localeCompare(y):x-y)*dir});
    body.innerHTML=rows.map(function(r){return '<tr>'+td('Provider','<strong>'+esc(r.provider)+'</strong>'+(r.example?' <span class="tag soon">Example</span>':''),'r-prov')+td('Product',esc(r.product))+td('Type',TYPES[r.type])+td('AER','<b>'+r.aer.toFixed(2)+'%</b>')+td('Term',esc(term(r)))+td('Min deposit',money(r.minDeposit))+td('Key conditions',esc(r.conditions||''),'r-cond')+td('FSCS',r.fscs?'Yes':'No')+td('Source',(r.sourceUrl?'<a href="'+esc(r.sourceUrl)+'" target="_blank" rel="noopener">Provider page<span class="sr"> for '+esc(r.provider)+' (opens in a new tab)</span></a>':'–')+'<span class="r-chk">Checked '+day(r.checked)+'</span>','r-src')+'</tr>'}).join('')||'<tr><td colspan="9">No accounts match these filters.</td></tr>';
    count.textContent=rows.length+' of '+data.length+' rows shown. Sorted by '+({aer:'AER',provider:'provider',product:'product',type:'type',termMonths:'term',minDeposit:'min deposit',fscs:'FSCS'}[sortKey])+(dir<0?' (high to low)':' (low to high)')+'. Sort order is not a ranking or recommendation.';
    syncSort();
    root.querySelectorAll('th[data-k]').forEach(function(th){th.setAttribute('aria-sort',th.dataset.k===sortKey?(dir>0?'ascending':'descending'):'none')});
  }
  root.querySelectorAll('th[data-k] button').forEach(function(b){b.addEventListener('click',function(){var k=b.parentNode.dataset.k;if(k===sortKey)dir=-dir;else{sortKey=k;dir=(k==='aer')?-1:1}render()})});
  [fType,fF,fMin].forEach(function(e){e.addEventListener('input',render)});
  var fS=document.getElementById('f-sort');function syncSort(){if(fS){var v=sortKey+':'+dir;fS.value=[].some.call(fS.options,function(o){return o.value===v})?v:''}}
  if(fS)fS.addEventListener('input',function(){if(!fS.value)return;var p=fS.value.split(':');sortKey=p[0];dir=+p[1];render()});
  fetch('data/savings-rates.json').then(function(r){return r.json()}).then(function(j){data=j.rates;var bn=document.getElementById('rates-banner');bn.hidden=j.status==='live';if(j.statusMessage)bn.textContent=j.statusMessage;render()}).catch(function(){if(!body.children.length)body.innerHTML='<tr><td colspan="9">Could not load rates.</td></tr>'});
})();
