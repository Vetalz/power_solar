const power_panel = 0.535;
const square_panel = 2.42;
const region_kof = {
  kiev: 1120.5245614455,
  odessa: 1385.44567443922,
  dnieper: 1234.50525424498,
  chernivtsi: 1141.87201830626,
  kharkov: 1126.53440164897,
  chernihiv: 1066.02007457847,
  zhytomyr: 1075.12994817173,
  poltava: 1158.23370612163,
  kherson: 1388.45928610684,
  zaporizhzhia: 1295.89446759402,
  luhansk: 1223.41765002849,
  donetsk: 1240.81629893848,
  vinnytsia: 1120.338008714,
  nikolaev: 1335.3311774169,
  kirovograd: 1193.8405469227,
  sumy: 1081.82481115072,
  lviv: 1064.74925871025,
  cherkasy: 1173.87143910164,
  khmelnitsky: 1086.22990572955,
  volyn: 1059.32670310424,
  rivne: 1063.39379578255,
  ivano_frankivsk: 1080.48775088748,
  ternopil: 1080.71632965345,
  uzhgorod: 1167.80152233531
};
const degradation = 0.002;
const rate = 0.168;
const eur_usd = 1.18;
const price_panel = 157;
const price_inverter = 1875;
const price_fastening = 42;
const price_additional = 700;
const price_assembly = 4900;
const tax = 0.195;

let budget = 10000;
let power;
let count_panel;
let square_station;
let generation_panel;
let generation_year;
let profit;
let profit_tax;
let payback;

let region;

document.getElementById("region").addEventListener("change", function() {
  region = this.value;
  calculate();
});

document.getElementById("budget_value").addEventListener("change", function() {
  budget = this.value;
  calculate();
});

document.getElementById("range_value").addEventListener("change", function() {
  budget = this.value;
  calculate();
});

function calculate() {
  count_panel = Math.ceil((budget - price_inverter - price_additional - price_assembly)
      / (price_panel + price_fastening))
  power = Math.round(count_panel * power_panel)
  square_station = Math.round(count_panel * square_panel)
  generation_panel = power_panel * count_panel;
  generation_year = region_kof[region] * generation_panel
  profit = generation_year * (1 - degradation) * rate * eur_usd
  profit_tax = profit - profit * tax;
  payback = (count_panel * price_panel + price_inverter + count_panel * price_fastening
      + price_additional + price_assembly) / profit_tax

  if (count_panel < 0) {
    count_panel = 0;
    power = 0;
    square_station = 0;
    generation_panel = 0;
    generation_year = 0;
    profit = 0;
    profit_tax = 0;
    payback = 0;
  }

  if (power > 40) {
    document.getElementsByClassName("calc_warning")[0].style.display= 'block';
  }
  else {
    document.getElementsByClassName("calc_warning")[0].style.display= 'none';
  }

  document.getElementById("power").innerHTML = power;
  document.getElementById("count_panel").innerHTML = count_panel;
  document.getElementById("square_station").innerHTML = square_station;
  document.getElementById("generation_year").innerHTML = generation_year.toFixed(2);
  document.getElementById("profit").innerHTML = profit_tax.toFixed(2);
  document.getElementById("payback").innerHTML = payback.toFixed(2);
}