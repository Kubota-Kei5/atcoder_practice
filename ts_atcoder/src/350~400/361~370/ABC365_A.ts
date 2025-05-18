import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/).map(Number);
let ptr = 0;

const Y: number = lines[ptr++];

if (Y % 4 !== 0) {
  console.log(365);
} else if (Y % 100 !== 0) {
  console.log(366);
} else if (Y % 400 !== 0) {
  console.log(365);
} else {
  console.log(366);
}
