import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

const N = Number(lines[ptr++]);
const T = Number(lines[ptr++]);
const A = Number(lines[ptr++]);

if (N - T < T || N - A < A) {
  console.log("Yes");
} else {
  console.log("No");
}
