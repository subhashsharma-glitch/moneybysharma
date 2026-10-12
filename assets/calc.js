/* MoneyBySharma calculators – pure functions (also used by Node tests) */
(function (root) {
  "use strict";
  // Mortgage: monthly repayment schedule with optional monthly overpayment
  function mortgage(principal, annualRatePct, years, type, overpay) {
    var r = annualRatePct / 100 / 12, n = Math.round(years * 12), op = overpay || 0;
    var pay;
    if (type === "interest") pay = principal * r;
    else pay = r === 0 ? principal / n : principal * r / (1 - Math.pow(1 + r, -n));
    var bal = principal, totalInt = 0, totalPaid = 0, months = 0, yearly = [principal];
    for (var m = 1; m <= n && bal > 0.005; m++) {
      var interest = bal * r;
      var capital = (type === "interest" ? 0 : pay - interest) + op;
      if (capital > bal) capital = bal;
      bal -= capital; totalInt += interest; totalPaid += interest + capital; months = m;
      if (m % 12 === 0) yearly.push(Math.max(bal, 0));
    }
    if (type === "interest" && bal > 0.005) { totalPaid += bal; }
    if (months % 12 !== 0) yearly.push(Math.max(bal, 0));
    return { monthly: pay, months: months, totalInterest: totalInt, totalPaid: totalPaid,
             balanceAtEnd: type === "interest" ? bal : 0, yearlyBalance: yearly };
  }
  // Fee impact: annual compounding; % fee charged on year-end value; flat fee deducted at year end
  function fees(start, growthPct, years, pctFee, flatFee) {
    var g = growthPct / 100, f = pctFee / 100, a = start, b = start, rows = [];
    for (var y = 1; y <= years; y++) {
      a = a * (1 + g) * (1 - f);
      b = b * (1 + g) - flatFee; if (b < 0) b = 0;
      rows.push({ year: y, pct: a, flat: b });
    }
    var none = start * Math.pow(1 + g, years);
    return { pct: a, flat: b, noFees: none, pctCost: none - a, flatCost: none - b, rows: rows };
  }
  // Gilt cash flows (semi-annual, coupon dates counted back from maturity). Price per £100 nominal (clean).
  function addMonths(d, m) { var x = new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth() + m, d.getUTCDate())); return x; }
  function giltFlows(couponPct, maturity, settle) {
    var dates = [], d = maturity;
    while (d > settle) { dates.unshift(d); d = addMonths(d, -6); }
    var prev = d, next = dates[0];
    var frac = (settle - prev) / (next - prev);
    var c = couponPct / 2;
    return { dates: dates, accrued: c * frac, coupon: c, firstFrac: 1 - frac };
  }
  function solve(fn, lo, hi) { for (var i = 0; i < 200; i++) { var mid = (lo + hi) / 2; if (fn(mid) > 0) lo = mid; else hi = mid; } return (lo + hi) / 2; }
  function gilt(cleanPrice, couponPct, maturity, taxPct, settle) {
    settle = settle || new Date(); maturity = new Date(maturity);
    var fl = giltFlows(couponPct, maturity, settle);
    var dirty = cleanPrice + fl.accrued, yr = 365.25 * 864e5;
    function pv(y, tax) {
      var s = 0;
      fl.dates.forEach(function (dt, i) {
        var halfYears = fl.firstFrac + i, cf = fl.coupon * (1 - tax);
        if (i === fl.dates.length - 1) cf += 100;
        s += cf / Math.pow(1 + y / 2, halfYears);
      });
      return s;
    }
    var t = taxPct / 100;
    var gry = solve(function (y) { return pv(y, 0) - dirty; }, -0.5, 1);
    var net = solve(function (y) { return pv(y, t) - dirty; }, -0.5, 1);
    var netEff = Math.pow(1 + net / 2, 2) - 1;
    return { dirty: dirty, accrued: fl.accrued, gry: gry, netYield: netEff,
             equivGross: t < 1 ? netEff / (1 - t) : NaN, years: (maturity - settle) / yr };
  }
  // Pension pot at retirement: monthly contributions (gross, incl. tax relief) paid at month end
  function pension(startAge, retireAge, monthly, growthPct, feePct, inflPct, lumpAge, lumpEndAge, lumpYearly) {
    var net = (1 + growthPct / 100) * (1 - feePct / 100) - 1, i = Math.pow(1 + net, 1 / 12) - 1;
    var pot = 0, paid = 0, byAge = [];
    for (var age = Math.min(startAge, lumpAge == null ? startAge : lumpAge); age < retireAge; age++) {
      for (var m = 0; m < 12; m++) {
        pot *= 1 + i;
        if (age >= startAge) { pot += monthly; paid += monthly; }
        if (lumpAge != null && age >= lumpAge && age < lumpEndAge) { pot += lumpYearly / 12; paid += lumpYearly / 12; }
      }
      byAge.push({ age: age + 1, pot: pot });
    }
    var yrs = retireAge - Math.min(startAge, lumpAge == null ? startAge : lumpAge);
    return { pot: pot, real: pot / Math.pow(1 + inflPct / 100, yrs), paid: paid, netGrowth: net, byAge: byAge };
  }
  // Home battery charged off-peak, discharged at peak. Rates in pence/kWh. degr = capacity loss % per year.
  function battery(kWh, effPct, cheapP, peakP, cycles, cost, life, degrPct) {
    var perCycle = (kWh * peakP - kWh / (effPct / 100) * cheapP) / 100, yr1 = perCycle * cycles, total = 0, payback = null, cum = 0;
    for (var y = 1; y <= life; y++) { var s = yr1 * Math.pow(1 - (degrPct || 0) / 100, y - 1); if (payback === null && cum + s >= cost) payback = y - 1 + (cost - cum) / s; cum += s; total += s; }
    return { perCycle: perCycle, annual: yr1, simplePayback: yr1 > 0 ? cost / yr1 : Infinity, payback: payback, lifetimeSaving: total, net: total - cost };
  }
  // EV charging cost. Rates in pence/kWh, efficiency in miles/kWh.
  function ev(miles, mpk, homeP, publicP, homeSharePct) {
    var h = homeP / mpk, p = publicP / mpk, sh = homeSharePct / 100;
    return { homePpm: h, publicPpm: p, annual: (miles * sh * h + miles * (1 - sh) * p) / 100, blendedPpm: sh * h + (1 - sh) * p };
  }
  // Real value of a sum after inflation, with optional interest (both % a year, compounded yearly)
  function realValue(amount, inflPct, ratePct, years) {
    var rows = [], nominal = amount, real = amount;
    for (var y = 1; y <= years; y++) { nominal *= 1 + ratePct / 100; real = nominal / Math.pow(1 + inflPct / 100, y); rows.push({ year: y, nominal: nominal, real: real }); }
    return { nominal: nominal, real: real, rows: rows };
  }
  // Balance transfer: fee vs interest saved over the 0% period. APR converted to an equivalent monthly rate.
  function btSave(balance, feePct, months, aprPct, monthly) {
    var r = Math.pow(1 + aprPct / 100, 1 / 12) - 1, b = balance, interest = 0;
    for (var m = 0; m < months && b > 0; m++) { var i = b * r; interest += i; b = Math.max(0, b + i - monthly); }
    var fee = balance * feePct / 100;
    return { fee: fee, interestAvoided: interest, saving: interest - fee, oldLeft: b, btLeft: Math.max(0, balance + fee - monthly * months) };
  }
  var api = { btSave: btSave, realValue: realValue, mortgage: mortgage, fees: fees, gilt: gilt, pension: pension, battery: battery, ev: ev };
  if (typeof module !== "undefined") module.exports = api; else root.MBSCalc = api;
})(this);
