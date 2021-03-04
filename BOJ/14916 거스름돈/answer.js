let fs = require("fs");
let input = Number(fs.readFileSync("/dev/stdin").toString());

let five = Math.floor(input / 5);
let two = 0;
let result = 0;

while (five >= 0) {
  two = Math.floor((input - five * 5) / 2);
  left = input - five * 5 - two * 2;

  if (left === 0) {
    result = five + two;
    break;
  } else if (left > 0) {
    five--;
  }

  if (five < 0) {
    result = -1;
    break;
  }
}

console.log(result);
