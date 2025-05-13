import * as fs from "fs";

const S = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n").join("");

const number = Number(S.replace("ABC", ""));

if (number === 316) {
  console.log("No");
} else if (number > 349 || number < 1) {
  console.log("No");
} else {
  console.log("Yes");
}
