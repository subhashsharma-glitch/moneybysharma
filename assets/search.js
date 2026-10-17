/* MoneyBySharma site search: static, client-side, no external services, no tracking.
   Lazy-loads assets/search-index.json the first time search is opened. */
(function () {
  'use strict';
  var me = document.currentScript, SRC = me ? me.src : '';
  var ROOT = new URL('../', SRC || location.href);                // site root
  var INDEX = new URL('assets/search-index.json', ROOT).href;
  var DB = null, loading = null, VOC = null;
  var TYPE = ['Page', 'Section', 'Jargon', 'File'];

  function norm(s) { return s.toLowerCase().replace(/[‘’']/g, '').replace(/&/g, ' and '); }
  function words(s) { return norm(s).match(/[a-z0-9£%]+/g) || []; }
  function esc(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }

  function load() {
    if (DB) return Promise.resolve(DB);
    if (loading) return loading;
    loading = fetch(INDEX).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }).then(function (j) {
      var voc = {};
      DB = j.e.map(function (e) {
        var tw = words(e[1] + ' ' + e[2]), bw = words(e[4]);
        tw.concat(bw).forEach(function (w) { voc[w] = (voc[w] || 0) + 1; });
        return { u: e[0], t: e[1], p: e[2], k: e[3], x: e[4], tl: norm(e[1]), bl: norm(e[4]), tw: tw, bs: new Set(bw), ts: new Set(tw) };
      });
      VOC = Object.keys(voc);
      return DB;
    });
    return loading;
  }

  // one-edit distance (substitution, insertion, deletion, adjacent swap)
  function near(a, b) {
    if (a === b) return true;
    var la = a.length, lb = b.length;
    if (Math.abs(la - lb) > 1) return false;
    var i = 0; while (i < la && i < lb && a[i] === b[i]) i++;
    if (la === lb) {
      if (a.slice(i + 1) === b.slice(i + 1)) return true;
      return a[i] === b[i + 1] && a[i + 1] === b[i] && a.slice(i + 2) === b.slice(i + 2);
    }
    return la > lb ? a.slice(i + 1) === b.slice(i) : b.slice(i + 1) === a.slice(i);
  }
  function expand(tok) {            // -> [{w, wt}] words from the site vocabulary
    var out = [], pre = [];
    for (var i = 0; i < VOC.length; i++) { if (VOC[i].indexOf(tok) === 0) pre.push(VOC[i]); }
    pre.forEach(function (w) { out.push({ w: w, wt: w === tok ? 1 : 0.8 }); });
    if (tok.length >= 4 && out.length < 3) {
      for (var j = 0; j < VOC.length; j++) { var w = VOC[j]; if (w.length >= 4 && near(tok, w) && out.every(function (o) { return o.w !== w; })) out.push({ w: w, wt: 0.5 }); }
    }
    return out;
  }

  function search(q, limit) {
    var toks = words(q).filter(function (t, i, a) { return a.indexOf(t) === i; });
    if (!toks.length || !DB) return { res: [], hl: [] };
    var ex = toks.map(expand), hl = [];
    ex.forEach(function (list) { list.forEach(function (o) { hl.push(o.w); }); });
    var phrase = norm(q).trim(), multi = toks.length > 1, res = [];
    DB.forEach(function (e) {
      var score = 0, ok = true;
      for (var i = 0; i < ex.length && ok; i++) {
        var best = 0;
        for (var j = 0; j < ex[i].length; j++) {
          var o = ex[i][j], s = 0;
          if (e.ts.has(o.w)) s = (e.tw[0] === o.w ? 16 : 12) * o.wt;       // title words
          else if (e.bs.has(o.w)) s = 3 * o.wt;                             // body words
          if (s > best) best = s;
        }
        if (!best && toks[i].length >= 3 && e.tl.indexOf(toks[i]) > -1) best = 4;
        if (!best && toks[i].length >= 3 && e.bl.indexOf(toks[i]) > -1) best = 1;
        if (!best) ok = false; else score += best;
      }
      if (!ok) return;
      if (e.tl === phrase) score += 30;
      else if (multi && e.tl.indexOf(phrase) > -1) score += 14;
      if (multi && e.bl.indexOf(phrase) > -1) score += 6;
      score += [4, 0, 1, 1][e.k];                                           // pages first, then terms
      res.push({ e: e, s: score });
    });
    res.sort(function (a, b) { return b.s - a.s || a.e.t.length - b.e.t.length; });
    return { res: res.slice(0, limit || 8), total: res.length, hl: hl };
  }

  function snippet(text, hl, n) {
    var lc = norm(text), pos = -1;
    for (var i = 0; i < hl.length; i++) { var p = lc.search(new RegExp('(^|[^a-z0-9])' + esc(hl[i]))); if (p > -1 && (pos < 0 || p < pos)) pos = p; }
    var start = Math.max(0, pos - 50), s = text.slice(start, start + n);
    if (start > 0) s = '…' + s.replace(/^\S*\s/, '');
    if (start + n < text.length) s = s.replace(/\s\S*$/, '') + '…';
    return s;
  }
  function mark(parent, text, hl) {  // build DOM (no innerHTML): highlight matched words
    if (!hl.length) { parent.appendChild(document.createTextNode(text)); return; }
    var re = new RegExp('(^|[^A-Za-z0-9£%])(' + hl.slice().sort(function (a, b) { return b.length - a.length; }).map(esc).join('|') + ')', 'gi'), last = 0, m;
    while ((m = re.exec(text))) {
      var st = m.index + m[1].length;
      if (st > last) parent.appendChild(document.createTextNode(text.slice(last, st)));
      var mk = document.createElement('mark'); mk.textContent = m[2]; parent.appendChild(mk);
      last = st + m[2].length;
    }
    if (last < text.length) parent.appendChild(document.createTextNode(text.slice(last)));
  }
  function href(u) { return new URL(u, ROOT).href; }

  function renderList(ul, out, q, idp) {
    ul.textContent = '';
    out.res.forEach(function (r, i) {
      var li = document.createElement('li'), a = document.createElement('a');
      li.id = idp + i; li.setAttribute('role', 'option'); li.className = 'sx-item';
      a.href = href(r.e.u); a.tabIndex = -1;
      var t = document.createElement('span'); t.className = 'sx-t'; mark(t, r.e.t, out.hl);
      var m = document.createElement('span'); m.className = 'sx-m'; m.textContent = r.e.k === 1 ? r.e.p : TYPE[r.e.k] + (r.e.k === 2 ? ' · Jargon buster' : '');
      var sn = document.createElement('span'); sn.className = 'sx-s'; mark(sn, snippet(r.e.x, out.hl, 130), out.hl);
      a.appendChild(t); a.appendChild(m); a.appendChild(sn); li.appendChild(a); ul.appendChild(li);
    });
  }

  /* ---------- header search (inline dropdown) ---------- */
  var form, input, toggle, panel, list, status, all, active = -1, shown = false, N = 8;
  function isPage() { return document.body.getAttribute('data-search') === 'page'; }
  function narrow() { return toggle && getComputedStyle(toggle).display !== 'none'; }   // icon + expanding row layout (< 1024px)
  function init() {
    form = document.getElementById('hs'); if (!form) return;
    input = document.getElementById('hs-q'); toggle = document.querySelector('.hs-toggle');
    var row = form.querySelector('.hs-row');
    form.setAttribute('action', new URL('search.html', ROOT).href);
    if (toggle) toggle.setAttribute('href', new URL('search.html', ROOT).href);
    panel = document.createElement('div'); panel.className = 'hs-panel'; panel.id = 'hs-panel'; panel.hidden = true;
    status = document.createElement('p'); status.className = 'sx-status'; status.id = 'hs-status'; status.setAttribute('role', 'status'); status.setAttribute('aria-live', 'polite');
    list = document.createElement('ul'); list.className = 'sx-list'; list.id = 'hs-list'; list.setAttribute('role', 'listbox'); list.setAttribute('aria-label', 'Search results');
    var foot = document.createElement('p'); foot.className = 'hs-foot';
    all = document.createElement('a'); all.className = 'sx-all'; all.hidden = true; all.textContent = 'See all results';
    var keys = document.createElement('span'); keys.className = 'hs-keys'; keys.textContent = '↑↓ to move · Enter to open · Esc to close';
    foot.appendChild(all); foot.appendChild(keys);
    panel.appendChild(status); panel.appendChild(list); panel.appendChild(foot); row.appendChild(panel);
    input.setAttribute('role', 'combobox'); input.setAttribute('aria-expanded', 'false'); input.setAttribute('aria-controls', 'hs-list');
    input.setAttribute('aria-autocomplete', 'list'); input.setAttribute('aria-haspopup', 'listbox');

    input.addEventListener('input', run);
    input.addEventListener('focus', function () { load(); if (input.value.trim() && last && !shown) show(); });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown') { e.preventDefault(); if (!shown && last && last.res.length) show(); move(1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); if (shown) move(-1); }
      else if (e.key === 'Enter') { var cur = list.querySelector('.sx-item[aria-selected=true] a'); if (shown && cur) { e.preventDefault(); location.href = cur.href; } }
      else if (e.key === 'Escape') {
        if (shown) { e.preventDefault(); hide(); }
        else if (narrow() && form.classList.contains('open')) { e.preventDefault(); collapse(true); }
      }
    });
    form.addEventListener('submit', function (e) {
      var cur = list.querySelector('.sx-item[aria-selected=true] a');
      if (shown && cur) { e.preventDefault(); location.href = cur.href; }
      else if (!input.value.trim()) { e.preventDefault(); input.focus(); }
    });
    if (toggle) {
      toggle.addEventListener('click', function (e) { e.preventDefault(); if (form.classList.contains('open')) collapse(true); else expandRow(); });
      toggle.addEventListener('pointerover', load);
    }
    document.addEventListener('pointerdown', function (e) {
      if (form.contains(e.target) || (toggle && toggle.contains(e.target))) return;
      hide();   // never collapse the row here: it would shift the layout between pointerdown and click
    });
    document.addEventListener('focusin', function (e) { if (shown && !form.contains(e.target) && !(toggle && toggle.contains(e.target))) hide(); });
  }
  function expandRow() { form.classList.add('open'); toggle.setAttribute('aria-expanded', 'true'); load(); input.focus(); }
  function collapse(refocus) { hide(); form.classList.remove('open'); if (toggle) { toggle.setAttribute('aria-expanded', 'false'); if (refocus) toggle.focus(); } }
  function show() { if (shown) return; shown = true; panel.hidden = false; input.setAttribute('aria-expanded', 'true'); }
  function hide() { if (!form) return; shown = false; panel.hidden = true; active = -1; input.setAttribute('aria-expanded', 'false'); input.removeAttribute('aria-activedescendant'); list.querySelectorAll('.sx-item').forEach(function (li) { li.setAttribute('aria-selected', 'false'); }); }
  function move(d) {
    var items = list.querySelectorAll('.sx-item'); if (!items.length) return;
    active = active < 0 ? (d > 0 ? 0 : items.length - 1) : (active + d + items.length) % items.length;
    items.forEach(function (li, i) { li.setAttribute('aria-selected', i === active ? 'true' : 'false'); });
    var li = items[active]; input.setAttribute('aria-activedescendant', li.id);
    if (li.offsetTop < list.scrollTop) list.scrollTop = li.offsetTop;                                   // keep it in view without scrolling the page
    else if (li.offsetTop + li.offsetHeight > list.scrollTop + list.clientHeight) list.scrollTop = li.offsetTop + li.offsetHeight - list.clientHeight;
  }
  function run() {
    var q = input.value.trim();
    active = -1; input.removeAttribute('aria-activedescendant');
    if (!q) { last = null; list.textContent = ''; status.textContent = ''; all.hidden = true; hide(); return; }
    load().then(function () {
      if (input.value.trim() !== q) return;
      var out = search(q, N); last = out; renderList(list, out, q, 'hs-r'); list.scrollTop = 0;
      status.textContent = out.res.length ? (out.total > N ? 'Showing ' + N + ' of ' + out.total + ' results' : out.total + (out.total === 1 ? ' result' : ' results')) : 'No results for “' + q + '”. Try a shorter or different word.';
      all.href = new URL('search.html?q=' + encodeURIComponent(q), ROOT).href; all.hidden = !out.res.length;
      shown = false; show();
    }).catch(function (err) { if (window.console) console.error(err && err.stack); status.textContent = 'Search is unavailable right now.'; show(); });
  }
  var last = null;
  function focusSearch() {
    if (!form) return;
    document.querySelectorAll('nav.main details[open]').forEach(function (d) { d.removeAttribute('open'); });
    if (narrow()) expandRow(); else { load(); input.focus(); input.select(); }
  }
  document.addEventListener('keydown', function (e) {
    if (e.key !== '/' || e.ctrlKey || e.metaKey || e.altKey) return;
    var t = e.target, tag = t && t.tagName;
    if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT' || (t && t.isContentEditable)) return;
    if (isPage()) { var q = document.getElementById('sp-q'); if (q) { e.preventDefault(); q.focus(); return; } }
    if (form) { e.preventDefault(); focusSearch(); }
  });

  /* ---------- search.html (no overlay) ---------- */
  function pageMode() {
    var box = document.getElementById('sp-results'); if (!box) return;
    var q = document.getElementById('sp-q'), st = document.getElementById('sp-status');
    function go() {
      var v = q.value.trim(); box.textContent = '';
      if (!v) { st.textContent = 'Type a word or phrase to search the site.'; return; }
      load().then(function () {
        var out = search(v, 50); renderList(box, out, v, 'sp-r');
        box.querySelectorAll('.sx-item').forEach(function (li) { li.removeAttribute('role'); });
        st.textContent = out.res.length ? out.total + (out.total === 1 ? ' result' : ' results') + ' for “' + v + '”' : 'No results for “' + v + '”. Try a shorter or different word.';
      }).catch(function () { st.textContent = 'Search is unavailable right now.'; });
    }
    var init = new URLSearchParams(location.search).get('q'); if (init) q.value = init;
    q.addEventListener('input', function () { history.replaceState(null, '', q.value.trim() ? '?q=' + encodeURIComponent(q.value.trim()) : location.pathname); go(); });
    document.getElementById('sp-form').addEventListener('submit', function (e) { e.preventDefault(); go(); });
    go();
  }
  function ready() { init(); pageMode(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', ready); else ready();
  window.mbsSearch = { open: focusSearch, search: function (q) { return load().then(function () { return search(q, 50); }); } };
})();
