import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

const N: number = Number(lines[ptr++]);
const M: number = Number(lines[ptr++]);

let taroList: boolean[] = [];

for (let i = 0; i < N; i++) {
  taroList.push(true);
}

for (let i = 0; i < M; i++) {
  let A: number = Number(lines[ptr++]);
  let B: string = String(lines[ptr++]);

  if (B === "M" && taroList[A - 1]) {
    taroList[A - 1] = false;
    console.log("Yes");
  } else {
    console.log("No");
  }
}
