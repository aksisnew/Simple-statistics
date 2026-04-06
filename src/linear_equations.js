let a1 = Number(prompt("Enter a1:"));
let b1 = Number(prompt("Enter b1:"));
let c1 = Number(prompt("Enter c1:"));
let a2 = Number(prompt("Enter a2:"));
let b2 = Number(prompt("Enter b2:"));
let c2 = Number(prompt("Enter c2:"));

let det = a1 * b2 - a2 * b1;

let x = (c1 * b2 - c2 * b1) / det;
let y = (a1 * c2 - a2 * c1) / det;

console.log(x, y);