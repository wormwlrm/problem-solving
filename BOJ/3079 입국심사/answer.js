let fs = require("fs");

let [first, ...rest] = fs.readFileSync("/dev/stdin").toString().split("\n");

let [, man] = first.split(" ").map(Number);
let times = rest.map(Number);

let time = [0];

let turn = 1;

while (true) {
  let value = times.reduce((acc, cur) => {
    return acc + Math.floor(turn / cur);
  }, 0);

  time.push(value);

  if (value >= man) {
    break;
  }

  turn++;
}

console.log(time.length - 1);
