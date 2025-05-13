import { readFileSync } from "fs";

const tokens = readFileSync(0, "utf-8").trim().split(/\s+/).map(Number);

let ptr = 0;
const N = tokens[ptr++];
const H: number[] = [];

for (let i = 0; i < N; i++) {
  H.push(tokens[ptr++]);
}

const target: number = H[0];
let ans: number = -1;
for (let i = 1; i < N; i++) {
  if (H[i] > target) {
    ans = i + 1;
    break;
  }
}
console.log(ans);
