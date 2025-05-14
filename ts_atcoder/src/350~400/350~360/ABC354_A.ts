import { readFileSync } from "fs";

const H: number = Number(readFileSync(0, "utf-8").trim());

let day = 0;
let height = 0;
let growth = 1;

while (height <= H) {
  height += growth;
  growth <<= 1;
  day++;
}

console.log(day);
