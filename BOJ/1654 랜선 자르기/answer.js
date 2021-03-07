var fs = require("fs");
var input = fs.readFileSync("/dev/stdin").toString();

function answer(input) {
  let [first, ...rest] = input.split("\n");

  let [k, n] = first.split(" ").map(Number);
  let lengths = rest.map(Number);

  let right = Math.max(...lengths);
  let left = 1;

  let maxLength = 0;

  while (left <= right) {
    let mid = Math.floor((right + left) / 2);
    let value = lengths.reduce((acc, cur) => {
      return acc + Math.floor(cur / mid);
    }, 0);

    if (value === n) {
      left = mid + 1;
      maxLength = mid;
    } else if (value > n) {
      left = mid + 1;
      maxLength = mid;
    } else {
      right = mid - 1;
    }
  }

  console.log(maxLength);
}

answer(input);
