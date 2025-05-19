import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

const S: string[] = [];

for (let i = 0; i < 3; i++) {
  S.push(lines[ptr++]);
}

// ABC
if (S[0] === "<" && S[1] === "<" && S[2] === "<") {
  console.log("B");
}

// ACB
if (S[0] === "<" && S[1] === "<" && S[2] === ">") {
  console.log("C");
}

// BAC
if (S[0] === ">" && S[1] === "<" && S[2] === "<") {
  console.log("A");
}

// BCA
if (S[0] === ">" && S[1] === ">" && S[2] === "<") {
  console.log("C");
}

// CAB
if (S[0] === "<" && S[1] === ">") {
  console.log("A");
}

// CBA
if (S[0] === ">" && S[1] === ">" && S[2] === ">") {
  console.log("B");
}
