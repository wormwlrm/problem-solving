let input = Number(require("fs").readFileSync("/dev/stdin").toString());

let cycle = 1;
let temp = input - 1;
let count = 1;

while (true) {
  if (temp <= 0) {
    break;
  }

  temp = temp - cycle * 6;
  cycle++;
  count++;
}

console.log(count);
