import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

const R = Number(lines[ptr++]);

if (R < 100) {
  console.log(100 - R);
} else if (R < 200) {
  console.log(200 - R);
} else if (R < 300) {
  console.log(300 - R);
} else if (R < 400) {
  console.log(400 - R);
}
