import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

const R = Number(lines[ptr++]);
const G = Number(lines[ptr++]);
const B = Number(lines[ptr++]);
const C = String(lines[ptr++]);

if (C === "Red") {
  console.log(Math.min(G, B));
} else if (C === "Green") {
  console.log(Math.min(R, B));
} else if (C === "Blue") {
  console.log(Math.min(R, G));
}
