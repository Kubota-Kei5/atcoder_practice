import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

const N: number = parseInt(lines[ptr++]);
const Q: number = parseInt(lines[ptr++]);
let ans: number = 0;
let L: number = 1;
let R: number = 2;

for (let i = 0; i < Q; i++) {
  let H: string = lines[ptr++];
  let T: number = parseInt(lines[ptr++]);
  if (H === "L") {
    if (T < R && R < L) {
      ans += N - L + T;
      L = T;
    } else if (L < R && R < T) {
      ans += N - T + L;
      L = T;
    } else {
      ans += Math.abs(L - T);
      L = T;
    }
  } else {
    if (T < L && L < R) {
      ans += N - R + T;
      R = T;
    } else if (R < L && L < T) {
      ans += N - T + R;
      R = T;
    } else {
      ans += Math.abs(R - T);
      R = T;
    }
  }
}

console.log(ans);
