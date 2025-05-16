import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

const N = Number(lines[ptr++]);
const X = Number(lines[ptr++]);
