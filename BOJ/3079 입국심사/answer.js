// 이 코드는 통과하지 못함

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  let [first, ...rest] = input;
  let [, man] = first.split(" ").map(Number);
  let times = rest.map(Number);
  let max = Math.max(...times);

  let minTime = 1;
  let maxTime = max * man;
  let result = 1;

  while (maxTime <= minTime) {
    let mid = Math.floor((maxTime + minTime) / 2);

    let value = times.reduce((acc, cur) => {
      return acc + Math.floor(mid / cur);
    }, 0);

    if (value >= man) {
      maxTime = mid - 1;
      result = mid;
    } else {
      minTime = mid + 1;
    }
  }

  console.log(result);

  process.exit();
});
