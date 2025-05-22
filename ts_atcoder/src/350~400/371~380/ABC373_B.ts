import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
const S: string = lines[0];
const arrayS: string[] = S.split("");
const alphabet: string[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");

let ans = 0;
let pre = arrayS.indexOf("A");

for (let k = 1; k < alphabet.length; k++) {
  const ch = alphabet[k];
  const idx = arrayS.indexOf(ch)!;
  ans += Math.abs(idx - pre);
  pre = idx;
}

console.log(ans);
