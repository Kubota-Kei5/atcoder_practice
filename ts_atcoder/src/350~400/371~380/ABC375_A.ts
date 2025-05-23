import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

const N: number = parseInt(lines[ptr++]);
const S: string[] = lines[ptr++].split("");

let ans: number = 0;
for (let i = 0; i < N - 2; i++) {
  if (S[i] === "#" && S[i + 1] === "." && S[i + 2] === "#") {
    ans += 1;
  }
}

console.log(ans);
