// 이 코드는 통과하지 못함

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n").map(BigInt);

let answer = [];

// JavaScript의 Number 범위 벗어나기 때문에 BigInt로 처리해야 함
for (let i = 0; i < input.length; i++) {
  let count = 1;
  let result = BigInt(1);
  let done = false;

  while (!done) {
    const int = String(1).repeat(count);
    const current = BigInt(int);

    if (current % input[i] === BigInt(0)) {
      result = current.toString();
      done = true;
    } else {
      count++;
    }
  }

  answer.push(count);
}

console.log(answer.join("\n"));
