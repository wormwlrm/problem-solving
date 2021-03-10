var fs = require("fs");

var input = fs.readFileSync("/dev/stdin").toString().split(" ").map(Number);

const [a, b] = input;
let all = a * 60 + b;
let subtracted = all - 45;
if (subtracted < 0) {
  subtracted = 1440 + subtracted;
}
let hour = Math.floor(subtracted / 60);
let min = subtracted % 60;
console.log(`${hour} ${min}`);
