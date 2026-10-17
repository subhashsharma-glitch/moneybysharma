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

  /* ---------- overlay ---------- */
  var ov, input, list, status, active = -1, opener, last = null;
  function build() {
    if (ov) return;
    ov = document.createElement('div'); ov.className = 'sx'; ov.hidden = true;
    ov.innerHTML = '<div class="sx-back" data-close></div><div class="sx-box" role="dialog" aria-modal="true" aria-label="Search MoneyBySharma">' +
      '<form class="sx-form" role="search" action="search.html"><label class="sr" for="sx-q">Search MoneyBySharma</label>' +
      '<input id="sx-q" name="q" type="search" autocomplete="off" spellcheck="false" placeholder="Search guides, tools and jargon" role="combobox" aria-expanded="false" aria-controls="sx-list" aria-autocomplete="list">' +
      '<button type="button" class="sx-x" data-close aria-label="Close search">Esc</button></form>' +
      '<p class="sx-status" id="sx-status" role="status" aria-live="polite"></p><ul id="sx-list" class="sx-list" role="listbox" aria-label="Search results"></ul>' +
      '<p class="sx-foot"><a class="sx-all" hidden>See all results</a><span class="sx-keys">↑↓ to move · Enter to open · Esc to close</span></p></div>';
    document.body.appendChild(ov);
    var f = ov.querySelector('form'); f.setAttribute('action', new URL('search.html', ROOT).href);
    input = ov.querySelector('input'); list = ov.querySelector('ul'); status = ov.querySelector('#sx-status');
    input.addEventListener('input', run);
    ov.addEventListener('click', function (e) { if (e.target.closest('[data-close]')) close(); else if (e.target.closest('a.sx-all,.sx-item a')) { /* normal navigation */ } });
    f.addEventListener('submit', function (e) { var cur = list.querySelector('.sx-item[aria-selected=true] a'); if (cur) { e.preventDefault(); location.href = cur.href; } });
    ov.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { e.preventDefault(); close(); }
      else if (e.key === 'ArrowDown') { e.preventDefault(); move(1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); move(-1); }
      else if (e.key === 'Tab') { var f2 = [input, ov.querySelector('.sx-x'), ov.querySelector('.sx-all:not([hidden])')].filter(Boolean), i = f2.indexOf(document.activeElement); e.preventDefault(); f2[(i + (e.shiftKey ? -1 : 1) + f2.length) % f2.length].focus(); }
    });
  }
  function move(d) {
    var items = list.querySelectorAll('.sx-item'); if (!items.length) return;
    active = (active + d + items.length) % items.length; select(items);
  }
  function select(items) {
    items = items || list.querySelectorAll('.sx-item');
    items.forEach(function (li, i) { li.setAttribute('aria-selected', i === active ? 'true' : 'false'); });
    if (items[active]) { input.setAttribute('aria-activedescendant', items[active].id); items[active].scrollIntoView({ block: 'nearest' }); } else input.removeAttribute('aria-activedescendant');
  }
  function run() {
    var q = input.value.trim(), all = ov.querySelector('.sx-all');
    active = -1; input.removeAttribute('aria-activedescendant');
    if (!q) { list.textContent = ''; status.textContent = ''; all.hidden = true; input.setAttribute('aria-expanded', 'false'); return; }
    load().then(function () {
      if (input.value.trim() !== q) return;
      var out = search(q, 8); last = out; renderList(list, out, q, 'sx-r');
      input.setAttribute('aria-expanded', out.res.length ? 'true' : 'false');
      status.textContent = out.res.length ? (out.total > 8 ? 'Showing 8 of ' + out.total + ' results' : out.total + (out.total === 1 ? ' result' : ' results')) : 'No results for “' + q + '”. Try a shorter or different word.';
      all.href = new URL('search.html?q=' + encodeURIComponent(q), ROOT).href; all.hidden = !out.res.length || out.total <= 8;
      if (out.res.length) { active = 0; select(); }
    }).catch(function () { status.textContent = 'Search is unavailable right now.'; });
  }
  function open(e) {
    if (e) e.preventDefault();
    build(); opener = document.activeElement; ov.hidden = false; document.documentElement.classList.add('sx-open');
    load(); input.focus(); input.select();
  }
  function close() { if (!ov || ov.hidden) return; ov.hidden = true; document.documentElement.classList.remove('sx-open'); if (opener && opener.focus) opener.focus(); }

  document.addEventListener('click', function (e) { var b = e.target.closest && e.target.closest('.search-btn'); if (b && !(ov && !ov.hidden)) { if (document.body.getAttribute('data-search') === 'page') { e.preventDefault(); var pq = document.getElementById('sp-q'); if (pq) pq.focus(); return; } open(e); } });
  document.addEventListener('pointerover', function (e) { if (e.target.closest && e.target.closest('.search-btn')) load(); });
  document.addEventListener('keydown', function (e) {
    if (e.key !== '/' || e.ctrlKey || e.metaKey || e.altKey) return;
    var t = e.target, tag = t && t.tagName;
    if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT' || (t && t.isContentEditable)) return;
    if (document.body.getAttribute('data-search') === 'page') { var q = document.getElementById('sp-q'); if (q) { e.preventDefault(); q.focus(); } return; }
    open(e);
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
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', pageMode); else pageMode();
  window.mbsSearch = { open: open, search: function (q) { return load().then(function () { return search(q, 50); }); } };
})();
