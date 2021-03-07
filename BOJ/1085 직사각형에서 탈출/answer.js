var fs = require("fs");
var input = fs.readFileSync("/dev/stdin").toString();

function answer(input) {
  const [x, y, w, h] = input.split(" ").map(Number);

  let min = x;

  if (y < min) {
    min = y;
  }

  if (w - x < min) {
    min = w - x;
  }

  if (h - y < min) {
    min = h - y;
  }

  console.log(min);
}

answer(input);
