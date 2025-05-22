import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

let S: string = lines[ptr++];
let T: string = lines[ptr++];

const arrayS: string[] = S.split("");
const arrayT: string[] = T.split("");
let ans: number = 0;

if (arrayS.length < arrayT.length) {
  ans = arrayS.length + 1;
} else if (arrayS.length > arrayT.length) {
  ans = arrayT.length + 1;
} else {
  ans = 0;
}

for (let i = 0; i < arrayS.length; i++) {
  if (arrayS[i] !== arrayT[i]) {
    ans = i + 1;
    break;
  }
}

console.log(ans);
