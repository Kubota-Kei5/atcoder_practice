import { readFileSync } from "fs";

const input = readFileSync("/dev/stdin", "utf-8");
const lines = input.trim().split("\n");

const N = Number(lines[0]);
let prev = "";
let canEat = true;

for (let i = 1; i <= N - 1; i++) {
  const s = lines[i];
  if (s === "sweet" && prev === "sweet") {
    canEat = false;
    break;
  }
  prev = s;
}

console.log(canEat ? "Yes" : "No");
