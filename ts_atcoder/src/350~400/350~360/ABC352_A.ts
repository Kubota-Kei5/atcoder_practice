import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

const N = Number(lines[ptr++]);
const X = Number(lines[ptr++]);
const Y = Number(lines[ptr++]);
const Z = Number(lines[ptr++]);

if (X < Y) {
  if (X < Z && Z < Y) {
    console.log("Yes");
  } else {
    console.log("No");
  }
} else if (Y < X) {
  if (Y < Z && Z < X) {
    console.log("Yes");
  } else {
    console.log("No");
  }
}
