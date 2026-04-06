
let input = prompt("Enter numbers separated by spaces:");


let arr = input.split(" ");
for (let i = 0; i < arr.length; i++) {
    arr[i] = Number(arr[i]);
}


for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length - i - 1; j++) {
        if (arr[j] > arr[j + 1]) {
  
            let temp = arr[j];
            arr[j] = arr[j + 1];
            arr[j + 1] = temp;
        }
    }
}


let median;
let n = arr.length;

if (n % 2 === 0) {
    median = (arr[n / 2 - 1] + arr[n / 2]) / 2;
} else {
    median = arr[Math.floor(n / 2)];
}


console.log("Sorted array:", arr);
console.log("Median:", median);