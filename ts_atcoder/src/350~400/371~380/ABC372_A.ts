import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

const S: string[] = [];

for (let i = 0; i < 3; i++) {
  S.push(lines[ptr++]);
}

let ans: string[] = [];
const N: number = S.length;

for (let i = 0; i < N; i++) {
  if (S[i] !== ".") {
    ans.push(S[i]);
  }
}

console.log(ans.join(""));
