let input = Number(require("fs").readFileSync("/dev/stdin").toString());

let next = input;
let count = 0;

while (true) {
  count++;
  let first = Math.floor(next / 10);
  let second = next % 10;
  let sum = first + second;
  next = second * 10 + (sum % 10);

  if (next === input) break;
}

console.log(count);
