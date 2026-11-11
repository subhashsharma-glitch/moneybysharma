/* Daily tip, quiz and myth-or-fact on the home page. Data from #mbs-daily-data (built from data/daily-features.json). */
(function () {
  var ROOT = document.getElementById("daily");
  var DATA_EL = document.getElementById("mbs-daily-data");
  if (!ROOT || !DATA_EL) return;
  var DATA;
  try { DATA = JSON.parse(DATA_EL.textContent); } catch (e) { return; }
  var STORE = "mbs-quiz-streak";

  function todayUK() {
    var q = (location.search.match(/[?&]date=(\d{4}-\d\d-\d\d)/) || [])[1];
    if (q) return q;
    try {
      return new Intl.DateTimeFormat("en-CA", { timeZone: "Europe/London", year: "numeric", month: "2-digit", day: "2-digit" }).format(new Date());
    } catch (e) { return new Date().toISOString().slice(0, 10); }
  }
  function realTodayUK() {
    try {
      return new Intl.DateTimeFormat("en-CA", { timeZone: "Europe/London", year: "numeric", month: "2-digit", day: "2-digit" }).format(new Date());
    } catch (e) { return new Date().toISOString().slice(0, 10); }
  }
  function dayIndex(iso, n) {
    var p = iso.split("-").map(Number);
    var days = Math.floor(Date.UTC(p[0], p[1] - 1, p[2]) / 86400000);
    return ((days % n) + n) % n;
  }
  function shiftDate(iso, days) {
    var p = iso.split("-").map(Number);
    var d = new Date(Date.UTC(p[0], p[1] - 1, p[2] + days));
    return d.toISOString().slice(0, 10);
  }
  function fmt(iso) {
    var p = iso.split("-").map(Number);
    return new Date(Date.UTC(p[0], p[1] - 1, p[2])).toLocaleDateString("en-GB", { weekday: "long", day: "numeric", month: "long", year: "numeric", timeZone: "UTC" });
  }
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c];
    });
  }
  function srcHTML(item) {
    if (!item.sourceUrl) return '<p class="src">' + esc(item.source || "") + (item.checked ? " · " + esc(item.checked) : "") + "</p>";
    return '<p class="src"><a href="' + esc(item.sourceUrl) + '" target="_blank" rel="noopener noreferrer">' + esc(item.source) + '<span class="sr sr-nt"> (opens in a new tab)</span></a>' + (item.checked ? " · " + esc(item.checked) : "") + "</p>";
  }
  function pageHTML(item) {
    if (!item.page) return "";
    return ' <a href="' + esc(item.page) + '">' + esc(item.pageLabel || "Read more") + "</a>";
  }
  function loadStreak() {
    try { return JSON.parse(localStorage.getItem(STORE) || "null") || { streak: 0, last: "", pick: null, correct: null }; }
    catch (e) { return { streak: 0, last: "", pick: null, correct: null }; }
  }
  function saveStreak(obj) {
    try { localStorage.setItem(STORE, JSON.stringify(obj)); } catch (e) {}
  }
  function yesterdayOf(iso) { return shiftDate(iso, -1); }

  function render(date) {
    var tips = DATA.tips || [], quiz = DATA.quiz || [], myths = DATA.myths || [];
    if (!tips.length || !quiz.length || !myths.length) return;
    var tip = tips[dayIndex(date, tips.length)];
    var q = quiz[dayIndex(date, quiz.length)];
    var myth = myths[dayIndex(date, myths.length)];
    var real = realTodayUK();
    var isRealDay = date === real;
    var st = loadStreak();
    var previewBar = "";
    if (DATA.preview) {
      previewBar = '<div class="daily-preview"><p><strong>Preview only</strong> — these daily features are not on the live site yet. They follow the UK date (Europe/London). Use the buttons, or add <code>?date=2026-11-12</code> to the address, to try another day.</p>' +
        '<div class="daily-preview-row"><button type="button" class="btn ghost daily-prev" data-shift="-1">Previous day</button>' +
        '<span class="daily-preview-date">' + esc(fmt(date)) + "</span>" +
        '<button type="button" class="btn ghost daily-next" data-shift="1">Next day</button></div></div>';
    }
    ROOT.innerHTML =
      previewBar +
      '<div class="wrap">' +
      '<p class="daily-kicker"><span class="tag">Today</span> ' + esc(fmt(date)) + "</p>" +
      ' <h2 id="daily-h">' + esc(DATA.heading || "Today's money bite") + '</h2>' +
      '<p class="daily-lead">A short tip, a one-question quiz and a myth-or-fact card, rotating each UK day. ' + esc(DATA.disclaimer || "Information, not financial advice.") + "</p>" +
      '<article class="card daily-tip" aria-labelledby="daily-tip-h">' +
        '<span class="tag">Money tip of the day</span>' +
        '<h3 id="daily-tip-h">' + esc(tip.title) + "</h3>" +
        "<p>" + esc(tip.body) + "</p>" +
        srcHTML(tip) + pageHTML(tip) +
      "</article>" +
      '<div class="grid g2 daily-grid">' +
        '<article class="card daily-quiz" aria-labelledby="daily-quiz-h">' +
          '<span class="tag">Daily quiz</span>' +
          '<h3 id="daily-quiz-h">Today\'s question</h3>' +
          '<p class="daily-q" id="daily-q">' + esc(q.question) + "</p>" +
          '<div class="daily-opts" role="group" aria-labelledby="daily-q"></div>' +
          '<div class="daily-explain" id="daily-explain" role="status" hidden></div>' +
          '<p class="daily-streak" id="daily-streak"></p>' +
          '<p class="hint">Your streak stays in this browser only. Nothing is sent to us. See <a href="privacy.html#s-daily-quiz-streak">Privacy</a>.</p>' +
        "</article>" +
        '<article class="card daily-myth" aria-labelledby="daily-myth-h">' +
          '<span class="tag">Myth or fact?</span>' +
          '<h3 id="daily-myth-h" class="sr">Myth or fact</h3>' +
          '<div class="daily-flip-wrap">' +
            '<button type="button" class="daily-flip" id="daily-flip" aria-expanded="false" aria-controls="daily-myth-back">' +
              '<span class="daily-face daily-front">' +
                '<p class="daily-claim">' + esc(myth.claim) + "</p>" +
                '<span class="hint">Tap or press to flip</span>' +
              "</span>" +
              '<span class="daily-face daily-back" id="daily-myth-back">' +
                '<p class="daily-verdict daily-verdict-' + esc(myth.verdict) + '">' + (myth.verdict === "fact" ? "Fact" : "Myth") + "</p>" +
                "<p>" + esc(myth.explain) + "</p>" +
                srcHTML(myth) +
              "</span>" +
            "</button>" +
          "</div>" +
        "</article>" +
      "</div>" +
      '<p class="hint daily-foot">' + esc(DATA.disclaimer || "Information, not financial advice.") + "</p>" +
      "</div>";

    if (DATA.preview) {
      ROOT.querySelectorAll("[data-shift]").forEach(function (btn) {
        btn.addEventListener("click", function () {
          var next = shiftDate(date, Number(btn.getAttribute("data-shift")));
          var u = new URL(location.href);
          u.searchParams.set("date", next);
          history.replaceState({}, "", u);
          render(next);
        });
      });
    }

    var opts = ROOT.querySelector(".daily-opts");
    q.options.forEach(function (label, i) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "daily-opt";
      b.setAttribute("data-i", String(i));
      b.innerHTML = '<span class="daily-opt-n">' + String.fromCharCode(65 + i) + "</span><span>" + esc(label) + "</span>";
      opts.appendChild(b);
    });

    var explain = document.getElementById("daily-explain");
    var streakEl = document.getElementById("daily-streak");
    function streakText(s, note) {
      var n = s.streak || 0;
      var t = n === 1 ? "1 day" : n + " days";
      streakEl.textContent = "Streak: " + t + "." + (note ? " " + note : "");
    }
    function showAnswer(pick, justAnswered) {
      opts.querySelectorAll(".daily-opt").forEach(function (b) {
        var i = Number(b.getAttribute("data-i"));
        b.disabled = true;
        if (i === q.answer) b.classList.add("is-correct");
        if (i === pick && pick !== q.answer) b.classList.add("is-wrong");
      });
      var ok = pick === q.answer;
      explain.hidden = false;
      explain.innerHTML = "<p><strong>" + (ok ? "That's right." : "Not this time.") + "</strong> " + esc(q.explain) + "</p>" + srcHTML(q);
      var note = "";
      if (!isRealDay) note = "Previewing another day, so the streak is unchanged.";
      else if (justAnswered && !ok) note = "A missed question resets the streak.";
      streakText(loadStreak(), note);
    }
    function alreadyAnsweredToday() { return isRealDay && st.last === real && st.pick != null; }

    if (alreadyAnsweredToday()) {
      showAnswer(st.pick, false);
    } else {
      streakText(st, isRealDay ? "" : "Previewing another day — answering here will not change your streak.");
      opts.addEventListener("click", function (ev) {
        var btn = ev.target.closest(".daily-opt");
        if (!btn || btn.disabled) return;
        var pick = Number(btn.getAttribute("data-i"));
        var correct = pick === q.answer;
        if (isRealDay) {
          var cur = loadStreak();
          if (cur.last === real) return;
          if (correct) cur.streak = (cur.last === yesterdayOf(real) && cur.correct) ? (cur.streak || 0) + 1 : 1;
          else cur.streak = 0;
          cur.last = real;
          cur.pick = pick;
          cur.correct = correct;
          saveStreak(cur);
        }
        showAnswer(pick, true);
      });
    }

    var flip = document.getElementById("daily-flip");
    var wrap = ROOT.querySelector(".daily-flip-wrap");
    function sizeFlip() {
      var front = flip.querySelector(".daily-front");
      var back = flip.querySelector(".daily-back");
      var h = Math.max(front.scrollHeight, back.scrollHeight);
      wrap.style.minHeight = h + "px";
      flip.style.minHeight = h + "px";
    }
    sizeFlip();
    window.addEventListener("resize", sizeFlip, { passive: true });
    flip.addEventListener("click", function () {
      var on = flip.classList.toggle("is-flipped");
      flip.setAttribute("aria-expanded", on ? "true" : "false");
      sizeFlip();
    });
  }

  render(todayUK());
})();
