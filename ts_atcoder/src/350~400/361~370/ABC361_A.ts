import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

const N = Number(lines[ptr++]);
const K = Number(lines[ptr++]);
const X = Number(lines[ptr++]);

const A: number[] = [];

for (let i = 0; i < N; i++) {
  A.push(Number(lines[ptr++]));
}

A.splice(K, 0, X);

console.log(...A);
