import { readFileSync } from "fs";
import { parse } from "path";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

const N: number = parseInt(lines[ptr++]);
const C: number = parseInt(lines[ptr++]);

let ans: number = 1;
let pre: number = parseInt(lines[ptr++]);

for (let i = 0; i < N; i++) {
  let T: number = parseInt(lines[ptr++]);

  if (T - pre >= C) {
    ans += 1;
    pre = T;
  }
}

console.log(ans);
