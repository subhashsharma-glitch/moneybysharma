const C = require('../assets/calc.js'); let ok = true;
function chk(name, got, exp, tol) { const p = Math.abs(got - exp) <= tol; ok = ok && p; console.log((p ? 'PASS ' : 'FAIL ') + name + ': got ' + got.toFixed(4) + ' expected ' + exp); }
// Mortgage 1: £200,000, 5%, 25y repayment. Hand: r=0.05/12, n=300 -> 200000*r/(1-(1+r)^-300) = 1169.18
let m = C.mortgage(200000, 5, 25, 'repayment', 0); chk('mortgage repay monthly', m.monthly, 1169.18, 0.01);
chk('mortgage total interest', m.totalInterest, 1169.18 * 300 - 200000, 3);
// Mortgage 2: interest-only £150,000 at 4.2% -> 150000*0.042/12 = 525.00
m = C.mortgage(150000, 4.2, 25, 'interest', 0); chk('interest-only monthly', m.monthly, 525, 0.001);
chk('interest-only balance at end', m.balanceAtEnd, 150000, 0.01);
// Overpayment shortens term
m = C.mortgage(200000, 5, 25, 'repayment', 200); console.log('overpay £200 months', m.months, m.months < 300 ? 'PASS' : 'FAIL'); ok = ok && m.months < 300;
// Fees 1: £10,000, 5%, 10y, 0.45% -> 10000*(1.05*0.9955)^10
let f = C.fees(10000, 5, 10, 0.45, 120); chk('pct fee', f.pct, 10000 * Math.pow(1.05 * 0.9955, 10), 0.01);
chk('pct fee (hand: 1.045275^10 = 1.557061 -> 15,570.61)', f.pct, 15570.61, 0.05);
// Fees 2: flat £120/yr -> 10000*1.05^10 - 120*(1.05^10-1)/0.05 = 14,779.60
chk('flat fee', f.flat, 14779.60, 0.05);
// Gilt 1: par, 4% coupon, maturity exactly 5y on a coupon date -> GRY 4%; net at 40%: 2.4% s.a. -> (1.012)^2-1 = 2.4144%; equiv 4.024%
const s = new Date(Date.UTC(2026, 9, 12)); let g = C.gilt(100, 4, new Date(Date.UTC(2031, 9, 12)), 40, s);
chk('gilt1 GRY %', g.gry * 100, 4, 0.0005); chk('gilt1 net %', g.netYield * 100, 2.4144, 0.0005); chk('gilt1 equiv %', g.equivGross * 100, 4.024, 0.0005);
// Gilt 2: zero coupon, price 90, 2y -> GRY = 2*((100/90)^(1/4)-1)= 2*0.026690 = 5.3380%; net eff = sqrt(100/90)-1 = 5.4093%; equiv at 40% = 9.0155%
g = C.gilt(90, 0, new Date(Date.UTC(2028, 9, 12)), 40, s);
chk('gilt2 GRY %', g.gry * 100, 5.3380, 0.002); chk('gilt2 net %', g.netYield * 100, 5.4093, 0.002); chk('gilt2 equiv %', g.equivGross * 100, 9.0155, 0.003);
process.exit(ok ? 0 : 1);
