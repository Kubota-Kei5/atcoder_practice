import { readFileSync } from "fs";

const tokens = readFileSync(0, "utf-8").trim().split(/\s+/).map(Number);

let ptr = 0;
const N = tokens[ptr++];
let M = tokens[ptr++];
const H: number[] = [];

for (let i = 0; i < N; i++) {
  H.push(tokens[ptr++]);
}

let count = 0;
for (let i = 0; i < N; i++) {
  if (M >= H[i]) {
    M -= H[i];
    count++;
  } else {
    break;
  }
}

console.log(count);
