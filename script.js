fs = require("fs-extra");
inquirer = require("inquirer");
fetch = require("node-fetch");

const [_node, _file, argNoOrAddress, ...argName] = process.argv;

async function getManual() {
  const { no } = await inquirer.prompt({
    type: "input",
    name: "no",
    message: "푼 문제 번호",
    default: argNoOrAddress,
  });

  const { name } = await inquirer.prompt({
    type: "input",
    name: "name",
    message: "푼 문제 이름",
    default: argName.join(" "),
  });

  return { no, name };
}

async function getAuto() {
  const response = await fetch(argNoOrAddress, {
    method: "get",
  }).then((r) => {
    return r.text();
  });

  const [noAndName] = /(?<=<title>).*(?=<\/title>)/gi.exec(response);
  const [no, name] = noAndName.split("번: ");

  return {
    no,
    name,
  };
}

function isHttpAddress(string) {
  return /https\:/.test(string);
}

function replaceText(data, no, name, encoded = false) {
  return data
    .replace(/\{\{ no \}\}/g, encoded ? encodeURI(no) : no)
    .replace(/\{\{ name \}\}/g, encoded ? encodeURI(name) : name);
}

function copyTemplate({ no, name } = {}, files = []) {
  const path = `./BOJ/${no} ${name}`;
  fs.copySync("./template", path);

  files.forEach((file) => {
    fs.readFile(`${path}/${file.name}`, "utf8", function (err, data) {
      const formatted = replaceText(data, no, name, file.encoded);
      console.log(formatted);

      fs.writeFile(`${path}/${file.name}`, formatted, "utf8", function (err) {
        if (err) return console.log(err);
      });
    });
  });
}

async function create() {
  const { no, name } = isHttpAddress(argNoOrAddress)
    ? await getAuto()
    : await getManual();

  copyTemplate(
    {
      no,
      name,
    },
    [
      {
        name: "README.md",
        encoded: false,
      },
      {
        name: "answer.py",
        encoded: true,
      },
    ]
  );
}

create();
