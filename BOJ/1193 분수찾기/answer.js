let fs = require("fs");
let input = Number(fs.readFileSync("/dev/stdin").toString());

// 홀수 라인인지 짝수 라인인지 확인
let even = false;

// 몇 번째 라인인지 확인
let cycle = 1;

// 빼기 할 떄 쓸 값
let diff = input;

while (true) {
  diff = diff - cycle;
  if (diff <= 0) {
    break;
  }
  cycle++;
  even = !even;
}

// 그러면 cycle 을 통해 sum을 알 수 있음
let sum = cycle + 1;

// 짝수 라인이면 분자가 더 큼
if (even) {
  let mo = 1 - diff;
  let ja = sum - 1 + diff;
  console.log(`${ja}/${mo}`);
} else {
  // 홀수 라인이면 분모가 더 큼
  let mo = sum - 1 + diff;
  let ja = 1 - diff;
  console.log(`${ja}/${mo}`);
}
