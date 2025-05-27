import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

const N: number = Number(lines[ptr++]);
const H: number[] = [];

for (let i = 0; i < N; i++) {
  H.push(Number(lines[ptr++]));
}
