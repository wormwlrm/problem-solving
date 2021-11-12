const { exec } = require("child_process");

const [_node, _file, no] = process.argv;

exec(`git add .`);
exec(`git cm "백준 ${no}번"`);
