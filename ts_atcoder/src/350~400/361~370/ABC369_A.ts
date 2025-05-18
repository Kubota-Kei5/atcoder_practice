import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

const A = Number(lines[ptr++]);
const B = Number(lines[ptr++]);

const diff: number = Math.abs(A - B);

if (A === B) {
  console.log(1);
} else if (diff % 2 === 0) {
  console.log(3);
} else {
  console.log(2);
}
