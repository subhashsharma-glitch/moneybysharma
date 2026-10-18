/* Home page: weekly email sign-up (Buttondown). Buttondown's docs say the embed-subscribe endpoint must be the action of a normal
   HTML form (not fetch), because subscribers may need to follow its response (CAPTCHA/validation). So the form posts natively to a new tab;
   this script only validates, blocks bots (nameless honeypot, never sent) and shows an on-page confirmation. */
(function(){
var form=document.getElementById('wk-form');if(!form)return;
var $=function(id){return document.getElementById(id)};
var em=$('wk-email'),ck=$('wk-consent'),hp=$('wk-hp'),done=$('wk-done'),send=$('wk-send');
function flag(el,errId,bad){var e=$(errId);if(e)e.hidden=!bad;if(bad)el.setAttribute('aria-invalid','true');else el.removeAttribute('aria-invalid');return bad}
form.addEventListener('submit',function(e){
 var v=em.value.trim();
 var b1=flag(em,'wk-email-err',!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v));
 var b2=flag(ck,'wk-consent-err',!ck.checked);
 if(b1||b2){e.preventDefault();(b1?em:ck).focus();return}
 if(hp&&hp.value){e.preventDefault();done.hidden=false;form.hidden=true;return}   /* bot: pretend success, send nothing */
 /* valid: let the browser post the form natively (opens Buttondown's response in a new tab), then confirm on this page */
 setTimeout(function(){form.hidden=true;done.hidden=false;try{done.focus();done.scrollIntoView({block:'center',behavior:'smooth'})}catch(x){}},400);
});
})();
