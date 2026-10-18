/* Feedback page: posts the form to FormSubmit (formsubmit.co) by AJAX, so the visitor stays on this page.
   Same service as the YA Transit site. On any failure it shows the direct address with a mailto/copy fallback. */
(function(){
var form=document.getElementById('fb-form');if(!form)return;
var ENDPOINT=form.getAttribute('data-endpoint'),TO=form.getAttribute('data-email');
var $=function(id){return document.getElementById(id)};
var type=$('fb-type'),pg=$('fb-page'),msg=$('fb-msg'),em=$('fb-email'),cnt=$('fb-count'),hp=$('fb-hp'),send=$('fb-send');
var done=$('fb-done'),fail=$('fb-fail');
var LABEL={dislike:"Something I don't like",topic:"A topic I'd like covered",suggestion:'A suggestion or improvement',mistake:'A mistake or out-of-date information'};
/* optional prefill: feedback.html?type=mistake&page=deals.html (a page file name is mapped to its nearest area; an area key also works) */
var MAP={};try{MAP=JSON.parse(pg.getAttribute('data-map')||'{}')}catch(e){}
var prefillPath='',prefillArea='';
function isKey(v){for(var i=0;i<pg.options.length;i++)if(pg.options[i].value&&pg.options[i].value===v)return true;return false}
function areaFor(v){if(isKey(v))return v;var c=v.split('#')[0].split('?')[0].replace(/^\//,'');return MAP[c]||''}
try{var q=new URLSearchParams(location.search),t=q.get('type'),p=q.get('page');
 if(t&&LABEL[t])type.value=t;
 if(p&&p.length<120&&/^[A-Za-z0-9._\/#?=&%-]+$/.test(p)){var ar=areaFor(p);if(ar){pg.value=ar;prefillArea=ar;if(!isKey(p))prefillPath=p.replace(/^\//,'')}}}catch(e){}
function count(){cnt.textContent=msg.value.length.toLocaleString('en-GB')}msg.addEventListener('input',count);count();
function flag(el,errId,bad){var e=$(errId);if(e)e.hidden=!bad;if(bad)el.setAttribute('aria-invalid','true');else el.removeAttribute('aria-invalid');return bad}
function build(){
 var area=pg.value?pg.options[pg.selectedIndex].text:'';
 var path=(pg.value&&pg.value===prefillArea&&prefillPath)?prefillPath:'';
 var url=path&&/^[A-Za-z0-9\-_\/]+\.html(#[\w-]+)?$/.test(path)?'https://moneybysharma.co.uk/'+path:'';
 var where=area?(area+(path?' \u2013 '+path:'')):'Not specified';
 var subject='MoneyBySharma feedback: '+LABEL[type.value]+(area&&pg.value!=='other'?' ('+area+')':'');
 var data={_subject:subject,_template:'table',_captcha:'false',Form:'Feedback',Type:LABEL[type.value],Area:where,Message:msg.value.trim()};
 if(url)data.Page=url;
 var mail=em.value.trim();if(mail){data.email=mail;data._replyto=mail}
 var body=data.Message+'\n\n---\nType: '+data.Type+'\nPart of the site: '+where+(url?'\nPage: '+url:'')+(mail?'\nReply to: '+mail:'')+'\n';
 return{subject:subject,body:body,data:data,mailto:'mailto:'+TO+'?subject='+encodeURIComponent(subject)+'&body='+encodeURIComponent(body)};
}
function show(box){done.hidden=box!==done;fail.hidden=box!==fail;if(box){box.hidden=false;try{box.focus();box.scrollIntoView({block:'center',behavior:'smooth'})}catch(x){}}}
function busy(on){send.disabled=on;if(!send.hasAttribute('data-label'))send.setAttribute('data-label',send.textContent);send.textContent=on?'Sending\u2026':send.getAttribute('data-label')}
form.addEventListener('submit',function(e){
 e.preventDefault();
 if(send.disabled)return;
 var b1=flag(type,'fb-type-err',!type.value);
 var b2=flag(msg,'fb-msg-err',!msg.value.trim());
 var v=em.value.trim(),b3=flag(em,'fb-email-err',v!==''&&!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v));
 if(b1||b2||b3){(b1?type:b2?msg:em).focus();return}
 var m=build();
 $('fb-mailto').href=m.mailto;$('fb-copy-src').value='To: '+TO+'\nSubject: '+m.subject+'\n\n'+m.body;$('fb-copied').textContent='';
 if(hp&&hp.value){show(done);form.hidden=true;return}   /* honeypot filled: pretend success, send nothing */
 show(null);busy(true);
 var ctl=window.AbortController?new AbortController():null,timer=setTimeout(function(){if(ctl)ctl.abort()},15000);
 fetch(ENDPOINT,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(m.data),signal:ctl?ctl.signal:undefined})
  .then(function(r){return r.json().catch(function(){return{}}).then(function(j){return{ok:r.ok,j:j}})})
  .then(function(res){clearTimeout(timer);busy(false);
   var s=res.j&&res.j.success;
   if(res.ok&&(s===true||s==='true')){form.hidden=true;show(done)}else show(fail)})
  .catch(function(){clearTimeout(timer);busy(false);show(fail)});
});
var again=$('fb-again');
if(again)again.addEventListener('click',function(){form.reset();count();prefillArea='';prefillPath='';form.hidden=false;show(null);type.focus()});
var copy=$('fb-copy');
if(copy)copy.addEventListener('click',function(){
 var src=$('fb-copy-src'),out=$('fb-copied'),text=src.value;
 function ok(){out.textContent='Copied.'}
 function fallback(){src.classList.remove('sr');src.removeAttribute('aria-hidden');src.removeAttribute('tabindex');src.style.cssText='width:100%;min-height:9rem;margin-top:.5rem';src.select();try{document.execCommand('copy')?ok():out.textContent='Select the text above and copy it.'}catch(x){out.textContent='Select the text above and copy it.'}}
 if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(text).then(ok,fallback);else fallback();
});
})();
