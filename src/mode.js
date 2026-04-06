let input = prompt("Enter numbers separated by spaces:");
let arr = input.split(" ");
for (let i = 0; i < arr.length; i++) {
    arr[i] = Number(arr[i]);
}
let freq = {};
for (let i = 0; i < arr.length; i++) {
    let num = arr[i];
    if (freq[num] === undefined) {
        freq[num] = 1;
    } else {
        freq[num]++;
    }
}
let maxCount = 0;
let mode;
for (let key in freq) {
    if (freq[key] > maxCount) {
        maxCount = freq[key];
        mode = Number(key);
    }
}
console.log(mode);