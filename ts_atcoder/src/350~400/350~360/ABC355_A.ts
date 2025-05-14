import { readFileSync } from "fs";

const tokens = readFileSync(0, "utf-8").trim().split(/\s+/).map(Number);

let ptr = 0;
const A: number = tokens[ptr++];
const B: number = tokens[ptr++];

let suspect: number[] = [1, 2, 3];

const filteredSuspect: number[] = suspect.filter(
  (item) => item !== A && item !== B
);

if (filteredSuspect.length === 1) {
  console.log(filteredSuspect[0]);
} else {
  console.log(-1);
}
