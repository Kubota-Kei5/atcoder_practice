import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

let ans: number = 0;
for (let i = 1; i < 13; i++) {
  let S: string = lines[ptr++];
  if (S.length === i) {
    ans += 1;
  }
}

console.log(ans);
