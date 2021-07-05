let yob1 = parseInt(prompt("person 1: enter your birth year"));
let yob2 = parseInt(prompt("person 2: enter your birth year"));

let older;
let younger;
yob1 > yob2 ? (older = yob1, younger = yob2) : (older = yob2, younger = yob1);

let dif = older - younger;

let halfYear = older + dif;

console.log(halfYear);
