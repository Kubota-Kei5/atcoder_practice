import { readFileSync } from "fs";

const tokens = readFileSync(0, "utf-8").trim().split(/\s+/);

let ptr: number = 0;
const N: number = parseInt(tokens[ptr++]);
let ans: number = 0;
for (let i = 0; i < N; i++) {
  let S: string = tokens[ptr++].toString();
  if (S === "Takahashi") {
    ans++;
  }
}
console.log(ans);
