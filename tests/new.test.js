const C=require('../assets/calc.js');let ok=true;
function chk(n,g,e,t){const p=Math.abs(g-e)<=t;ok=ok&&p;console.log((p?'PASS ':'FAIL ')+n+': got '+g.toFixed(4)+' expected '+e)}
// Pension 1: £100/month, 0% growth/fee/inflation, age 57->67 = 120 x £100 = £12,000
let r=C.pension(57,67,100,0,0,0);chk('pension1 pot',r.pot,12000,0.001);chk('pension1 real',r.real,12000,0.001);
// Pension 2: £200/month 25->67, 5% growth, 0.5% fee -> net 4.475%; i=(1.04475)^(1/12)-1; FV=200*((1+i)^504-1)/i = 289,378.94; real at 2% = /1.02^42 = 125,967.85
r=C.pension(25,67,200,5,0.5,2);chk('pension2 pot',r.pot,289378.94,0.05);chk('pension2 real',r.real,125967.85,0.05);
// Junior SIPP: £3,600 gross/yr birth->18, 0% growth -> 18 x 3,600 = 64,800
r=C.pension(67,67,0,0,0,0,0,18,3600);chk('junior sipp 0%',r.pot,64800,0.01);
// Battery 1: 10kWh, 90%, 7p cheap, 27p peak, 300 cycles: per cycle (270-77.78)/100=£1.9222; yr £576.67; £4,000 -> 6.94 yrs
let b=C.battery(10,90,7,27,300,4000,15,0);chk('battery1 annual',b.annual,576.67,0.01);chk('battery1 payback',b.simplePayback,6.9364,0.001);
// Battery 2: 5kWh, 100%, 10p, 30p, 365 cycles: £1/cycle -> £365/yr; £3,650 -> 10 yrs
b=C.battery(5,100,10,30,365,3650,15,0);chk('battery2 annual',b.annual,365,0.001);chk('battery2 payback',b.payback,10,0.001);
// EV 1: 10,000mi, 4 mi/kWh, 7p home, 79p public, 80% home: 1.75p & 19.75p/mi; 8000*1.75+2000*19.75 = £535
let e=C.ev(10000,4,7,79,80);chk('ev1 home ppm',e.homePpm,1.75,1e-9);chk('ev1 public ppm',e.publicPpm,19.75,1e-9);chk('ev1 annual',e.annual,535,1e-6);
// EV 2: 7,000mi, 3.5 mi/kWh, 28p, 100% home: 8p/mi -> £560
e=C.ev(7000,3.5,28,79,100);chk('ev2 ppm',e.homePpm,8,1e-9);chk('ev2 annual',e.annual,560,1e-6);
// Real value 1: £1,000, 2% inflation, 0% interest, 10y -> 1000/1.02^10 = 820.35
let rv=C.realValue(1000,2,0,10);chk('real1',rv.real,820.35,0.005);
// Real value 2: interest equals inflation (3%/3%) -> real stays £1,000; nominal 1000*1.03^5 = 1159.27
rv=C.realValue(1000,3,3,5);chk('real2 real',rv.real,1000,1e-9);chk('real2 nominal',rv.nominal,1159.27,0.005);
// Balance transfer 1: £3,000, 3% fee, 12 months, 0% APR on old card -> interest 0, fee £90, saving -£90, BT left 3090-100*12=1890
{let t=C.btSave(3000,3,12,0,100);chk('bt1 fee',t.fee,90,1e-9);chk('bt1 saving',t.saving,-90,1e-9);chk('bt1 btLeft',t.btLeft,1890,1e-9);}
// Balance transfer 2: £1,200, APR 1.01^12-1 (=1%/month), no payments, 12 months: interest 1200*(1.01^12-1)=152.19; fee 2%=24; saving 128.19
{let t=C.btSave(1200,2,12,(Math.pow(1.01,12)-1)*100,0);chk('bt2 interest',t.interestAvoided,152.1900,0.001);chk('bt2 saving',t.saving,128.19,0.001);}
process.exit(ok?0:1);
