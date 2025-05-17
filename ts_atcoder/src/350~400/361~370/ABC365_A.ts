import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/).map(Number);
let ptr = 0;

const N: number = lines[ptr++];
const T: number = lines[ptr++];
