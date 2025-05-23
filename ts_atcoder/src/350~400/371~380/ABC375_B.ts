import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

const N: number = parseInt(lines[ptr++]);
let cx: number = 0;
let cy: number = 0;
9;

const calcDist = (cx: number, cy: number, nx: number, ny: number): number => {
  return Math.sqrt(Math.pow(cx - nx, 2) + Math.pow(cy - ny, 2));
};

let ans: number = 0;

for (let i = 0; i < N; i++) {
  let nx: number = parseInt(lines[ptr++]);
  let ny: number = parseInt(lines[ptr++]);

  let dist: number = calcDist(cx, cy, nx, ny);
  ans += dist;
  cx = nx;
  cy = ny;
}

ans += calcDist(cx, cy, 0, 0);
console.log(ans);
