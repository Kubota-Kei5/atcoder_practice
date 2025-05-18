import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

const L = Number(lines[ptr++]);
const R = Number(lines[ptr++]);

if (L === 1 && R === 0) {
  console.log("Yes");
} else if (L === 0 && R === 1) {
  console.log("No");
} else {
  console.log("Invalid");
}
