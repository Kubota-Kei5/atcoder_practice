import { readFileSync } from "fs";

const tokens = readFileSync(0, "utf-8").trim().split(/\s+/).map(Number);

let ptr = 0;
const N: number = tokens[ptr++];
const L: number = tokens[ptr++];
const R: number = tokens[ptr++];

let numList: number[] = [];

for (let i = 0; i < N; i++) {
  numList.push(i + 1);
}

for (let i = L - 1; i < R; i++) {
  numList[i] = R - (i - (L - 1));
}

console.log(numList.join(" "));
console.log(...numList);
