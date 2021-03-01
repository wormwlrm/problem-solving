let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n").map(Number);

let [count, ...rest] = input;

let max = 0;

rest.sort((a, b) => b - a);

for (let index = 0; index < count; index++) {
  const weight = rest[index] * (index + 1);
  if (weight > max) {
    max = weight;
  }
}

console.log(max);
