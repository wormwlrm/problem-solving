fs = require("fs-extra");
inquirer = require("inquirer");

async function create() {
  const { no } = await inquirer.prompt({
    type: "input",
    name: "no",
    message: "푼 문제 번호",
  });

  const { name } = await inquirer.prompt({
    type: "input",
    name: "name",
    message: "푼 문제 이름",
  });

  const path = `./BOJ/${no} ${name}`;
  fs.copySync("./template", path);

  fs.readFile(`${path}/README.md`, "utf8", function (err, data) {
    console.log("data :>> ", data);
    const formatted = data
      .replace(/\{\{ no \}\}/g, no)
      .replace(/\{\{ name \}\}/g, name);

    console.log("formatted :>> ", formatted);

    fs.writeFile(`${path}/README.md`, formatted, "utf8", function (err) {
      if (err) return console.log(err);
    });
  });
}

create();
