/* Kids Corner: challenge of the day. Data from #kc-daily-data. No storage, no network. */
(function () {
  var root = document.getElementById("kc-daily");
  var dataEl = document.getElementById("kc-daily-data");
  if (!root || !dataEl) return;
  var items;
  try { items = JSON.parse(dataEl.textContent); } catch (e) { return; }
  if (!items || !items.length) return;

  function todayUK() {
    var q = (location.search.match(/[?&]date=(\d{4}-\d\d-\d\d)/) || [])[1];
    if (q) return q;
    try {
      return new Intl.DateTimeFormat("en-CA", { timeZone: "Europe/London", year: "numeric", month: "2-digit", day: "2-digit" }).format(new Date());
    } catch (e) { return new Date().toISOString().slice(0, 10); }
  }
  function dayOfYear(iso) {
    var p = iso.split("-").map(Number);
    var start = Date.UTC(p[0], 0, 1);
    var cur = Date.UTC(p[0], p[1] - 1, p[2]);
    return Math.floor((cur - start) / 86400000) + 1;
  }
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c];
    });
  }

  var item = items[((dayOfYear(todayUK()) % items.length) + items.length) % items.length];
  var isRiddle = item.type === "riddle";
  var title = isRiddle ? "Today's riddle" : "Today's challenge";
  var choices = (isRiddle && item.choices && item.choices.length) ? item.choices : null;
  var html =
    '<span class="tag">Challenge of the day</span>' +
    '<h2 id="kc-daily-h">' + title + "</h2>" +
    '<p class="kc-daily-text" id="kc-daily-q">' + esc(item.text) + "</p>";
  if (choices) {
    html += '<div class="kc-daily-choices" role="group" aria-labelledby="kc-daily-q">';
    for (var i = 0; i < choices.length; i++) {
      html += '<button type="button" class="kc-daily-choice" data-i="' + i + '">' + esc(choices[i]) + "</button>";
    }
    html += "</div>" +
      '<div class="kc-daily-fb" id="kc-daily-fb" role="status" aria-live="polite" hidden></div>';
  }
  root.innerHTML = html;

  var fb = document.getElementById("kc-daily-fb");
  var btns = root.querySelectorAll(".kc-daily-choice");
  if (!btns.length) return;

  function showFb(kind, inner) {
    fb.hidden = false;
    fb.className = "kc-daily-fb is-" + kind;
    fb.innerHTML = inner;
  }

  root.addEventListener("click", function (e) {
    var btn = e.target.closest(".kc-daily-choice");
    if (!btn || btn.disabled) return;
    var choice = choices[Number(btn.getAttribute("data-i"))];
    if (choice === item.answer) {
      for (var i = 0; i < btns.length; i++) {
        btns[i].disabled = true;
        if (btns[i] === btn) btns[i].classList.add("is-right");
      }
      showFb(
        "right",
        "<p>" + esc(item.feedback_right || "Well done!") + "</p>" +
          '<p class="kc-daily-answer-line">The answer is ' + esc(item.answer) + "</p>"
      );
    } else {
      btn.classList.add("is-wrong");
      btn.disabled = true;
      showFb("wrong", "<p>" + esc(item.feedback_wrong || "Not quite! Try again.") + "</p>");
    }
  });

  root.addEventListener("keydown", function (e) {
    if (e.key !== "ArrowDown" && e.key !== "ArrowUp" && e.key !== "ArrowRight" && e.key !== "ArrowLeft") return;
    var list = [];
    for (var i = 0; i < btns.length; i++) if (!btns[i].disabled) list.push(btns[i]);
    if (!list.length) return;
    var idx = list.indexOf(document.activeElement);
    if (idx < 0) idx = e.key === "ArrowUp" || e.key === "ArrowLeft" ? 0 : -1;
    var dir = (e.key === "ArrowDown" || e.key === "ArrowRight") ? 1 : -1;
    var next = list[(idx + dir + list.length) % list.length];
    if (next) {
      e.preventDefault();
      next.focus();
    }
  });
})();
