let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString();

// JavaScript의 Number 범위 벗어나기 때문에 BigInt로 처리해야 함
const fibonacci = [BigInt(0), BigInt(1)];

const index = Number(input);

function recursive(i) {
  if (fibonacci[i] !== undefined) {
    return fibonacci[i];
  } else {
    fibonacci[i] = recursive(i - 1) + recursive(i - 2);
    return fibonacci[i];
  }
}

console.log(recursive(index).toString());
