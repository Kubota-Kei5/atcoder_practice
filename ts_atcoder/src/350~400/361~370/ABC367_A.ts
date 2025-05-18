import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

const A = Number(lines[ptr++]);
const B = Number(lines[ptr++]);
const C = Number(lines[ptr++]);

if (B < C) {
  if (B < A && A < C) {
    console.log("No");
  } else {
    console.log("Yes");
  }
} else {
  if (C < A && A < B) {
    console.log("Yes");
  } else {
    console.log("No");
  }
}
