import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

const N = Number(lines[ptr++]);
const K = Number(lines[ptr++]);

let A: number[] = [];
for (let i = 0; i < N; i++) {
  A.push(Number(lines[ptr++]));
}

let B: number[] = A;
for (let i = 0; i < K; i++) {
  B.unshift(B[B.length - 1]);
  B.pop();
}

console.log(...B);
