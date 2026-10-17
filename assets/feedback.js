/* Feedback page: builds a pre-filled email (mailto:) in the visitor's own email app. Nothing is sent or stored by this site. */
(function(){
var form=document.getElementById('fb-form');if(!form)return;
var TO='hello@moneybysharma.co.uk';
var $=function(id){return document.getElementById(id)};
var type=$('fb-type'),pg=$('fb-page'),msg=$('fb-msg'),em=$('fb-email'),cnt=$('fb-count'),after=$('fb-after');
var LABEL={dislike:"Something I don't like",topic:"A topic I'd like covered",suggestion:'A suggestion or improvement',mistake:'A mistake or out-of-date information'};
/* optional prefill: feedback.html?type=mistake&page=deals.html */
try{var q=new URLSearchParams(location.search),t=q.get('type'),p=q.get('page');
 if(t&&LABEL[t])type.value=t;
 if(p){for(var i=0;i<pg.options.length;i++)if(pg.options[i].value===p){pg.value=p;break}}}catch(e){}
function count(){cnt.textContent=msg.value.length.toLocaleString('en-GB')}msg.addEventListener('input',count);count();
function flag(el,errId,bad){var e=$(errId);if(e)e.hidden=!bad;if(bad)el.setAttribute('aria-invalid','true');else el.removeAttribute('aria-invalid');return bad}
function build(){
 var pageTxt=pg.value?pg.options[pg.selectedIndex].text:'';
 var url=pg.value&&/\.html$/.test(pg.value)?'https://moneybysharma.co.uk/'+pg.value:'';
 var subject='MoneyBySharma feedback: '+LABEL[type.value]+(pageTxt&&pg.value&&pg.value!=='other'?' ('+pageTxt+')':'');
 var body=msg.value.trim()+'\n\n---\nType: '+LABEL[type.value]+'\nPage: '+(pageTxt||'Not about a particular page')+(url?' ('+url+')':'')+(em.value.trim()?'\nReply to: '+em.value.trim():'')+'\n';
 return{subject:subject,body:body,href:'mailto:'+TO+'?subject='+encodeURIComponent(subject)+'&body='+encodeURIComponent(body)};
}
form.addEventListener('submit',function(e){
 e.preventDefault();
 var b1=flag(type,'fb-type-err',!type.value);
 var b2=flag(msg,'fb-msg-err',!msg.value.trim());
 var v=em.value.trim(),b3=flag(em,'fb-email-err',v!==''&&!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v));
 if(b1||b2||b3){(b1?type:b2?msg:em).focus();return}
 var m=build();
 $('fb-copy-src').value='To: '+TO+'\nSubject: '+m.subject+'\n\n'+m.body;
 after.hidden=false;after.focus();
 try{after.scrollIntoView({block:'nearest',behavior:'smooth'})}catch(x){}
 window.location.href=m.href;
});
var copy=$('fb-copy');
if(copy)copy.addEventListener('click',function(){
 var src=$('fb-copy-src'),out=$('fb-copied'),text=src.value;
 function ok(){out.textContent='Copied.'}
 function fallback(){src.classList.remove('sr');src.removeAttribute('aria-hidden');src.removeAttribute('tabindex');src.style.cssText='width:100%;min-height:9rem;margin-top:.5rem';src.select();try{document.execCommand('copy')?ok():out.textContent='Select the text above and copy it.'}catch(x){out.textContent='Select the text above and copy it.'}}
 if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(text).then(ok,fallback);else fallback();
});
})();
