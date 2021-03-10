const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  let [count, ...rest] = input;

  let hotel = [...Array(15)].map(() => {
    return [1, ...Array(14).fill(0)];
  });

  hotel[0].forEach((e, index) => {
    hotel[0][index] = index + 1;
  });

  hotel.forEach((a, index) => {
    hotel[index].forEach((b, index2) => {
      if (b > 0) {
        return;
      }
      let sum = hotel[index - 1].reduce((acc, cur, index3) => {
        if (index3 > index2) {
          return acc;
        }
        return acc + cur;
      }, 0);
      hotel[index][index2] = sum;
    });
  });

  for (let i = 0; i < count; i++) {
    // 층
    let floor = rest[2 * i];

    // 호
    let room = rest[2 * i + 1];

    console.log(hotel[floor][room - 1]);
  }

  process.exit();
});
