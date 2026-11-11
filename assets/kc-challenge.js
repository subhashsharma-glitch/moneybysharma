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
  root.innerHTML =
    '<span class="tag">Challenge of the day</span>' +
    '<h2 id="kc-daily-h">' + title + "</h2>" +
    '<p class="kc-daily-text">' + esc(item.text) + "</p>" +
    (isRiddle
      ? '<button type="button" class="btn kc-daily-show" aria-expanded="false" aria-controls="kc-daily-answer">Show answer</button>' +
        '<p class="kc-daily-answer" id="kc-daily-answer" hidden></p>'
      : "");

  var btn = root.querySelector(".kc-daily-show");
  if (btn) {
    btn.addEventListener("click", function () {
      var ans = document.getElementById("kc-daily-answer");
      var on = ans.hidden;
      ans.hidden = !on;
      if (on) ans.textContent = item.answer || "";
      btn.setAttribute("aria-expanded", on ? "true" : "false");
      btn.textContent = on ? "Hide answer" : "Show answer";
    });
  }
})();
