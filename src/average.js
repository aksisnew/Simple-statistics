let input = prompt("Enter numbers separated by spaces:");
let arr = input.split(" ");
for (let i = 0; i < arr.length; i++) {
    arr[i] = Number(arr[i]);
}
let sum = 0;
for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
}
let avg = sum / arr.length;
console.log(avg);