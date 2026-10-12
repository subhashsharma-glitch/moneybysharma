(function(){
  var root=document.getElementById('rates');if(!root)return;
  var TYPES={'easy-access':'Easy access','notice':'Notice','fixed':'Fixed bond','cash-isa':'Cash ISA','regular-saver':'Regular saver'};
  var data=[],sortKey='aer',dir=-1;
  var body=root.querySelector('tbody'),fType=document.getElementById('f-type'),fF=document.getElementById('f-fscs'),fMin=document.getElementById('f-min'),count=document.getElementById('rates-count');
  function term(m){return m==null?'None':(m%12===0?(m/12)+(m===12?' year':' years'):m+' months')}
  function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
  function render(){
    var max=parseFloat(fMin.value);
    var rows=data.filter(function(r){return (!fType.value||r.type===fType.value)&&(!fF.checked||r.fscs)&&(isNaN(max)||r.minDeposit<=max)});
    rows.sort(function(a,b){var x=a[sortKey],y=b[sortKey];if(x==null)x=-1;if(y==null)y=-1;return (typeof x==='string'?x.localeCompare(y):x-y)*dir});
    body.innerHTML=rows.map(function(r){return '<tr><td>'+esc(r.provider)+(r.example?' <span class="tag soon">Example</span>':'')+'</td><td>'+esc(r.product)+'</td><td>'+TYPES[r.type]+'</td><td><b>'+r.aer.toFixed(2)+'%</b></td><td>'+term(r.termMonths)+'</td><td>'+gbp(r.minDeposit,0)+'</td><td>'+(r.fscs?'Yes':'No')+'</td><td>'+(r.sourceUrl?'<a href="'+esc(r.sourceUrl)+'" rel="noopener">Source</a>':'–')+'</td><td>'+(r.checked||'–')+'</td></tr>'}).join('')||'<tr><td colspan="9">No accounts match these filters.</td></tr>';
    count.textContent=rows.length+' of '+data.length+' rows shown';
    root.querySelectorAll('th[data-k]').forEach(function(th){th.setAttribute('aria-sort',th.dataset.k===sortKey?(dir>0?'ascending':'descending'):'none')});
  }
  root.querySelectorAll('th[data-k] button').forEach(function(b){b.addEventListener('click',function(){var k=b.parentNode.dataset.k;if(k===sortKey)dir=-dir;else{sortKey=k;dir=(k==='aer')?-1:1}render()})});
  [fType,fF,fMin].forEach(function(e){e.addEventListener('input',render)});
  fetch('data/savings-rates.json').then(function(r){return r.json()}).then(function(j){data=j.rates;document.getElementById('rates-banner').hidden=j.status==='live';if(j.statusMessage)document.getElementById('rates-banner').textContent=j.statusMessage;render()}).catch(function(){body.innerHTML='<tr><td colspan="9">Could not load rates.</td></tr>'});
})();
