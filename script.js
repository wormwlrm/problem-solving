fs = require("fs-extra");
inquirer = require("inquirer");

const [_node, _file, argNo, ...argName] = process.argv;

async function create() {
  const { no } = await inquirer.prompt({
    type: "input",
    name: "no",
    message: "푼 문제 번호",
    default: argNo,
  });

  const { name } = await inquirer.prompt({
    type: "input",
    name: "name",
    message: "푼 문제 이름",
    default: argName.join(),
  });

  const path = `./BOJ/${no} ${name}`;
  fs.copySync("./template", path);

  fs.readFile(`${path}/README.md`, "utf8", function (err, data) {
    const formatted = data
      .replace(/\{\{ no \}\}/g, no)
      .replace(/\{\{ name \}\}/g, name);

    fs.writeFile(`${path}/README.md`, formatted, "utf8", function (err) {
      if (err) return console.log(err);
    });
  });
}

create();
