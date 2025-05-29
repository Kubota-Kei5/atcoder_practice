import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;

const Q = Number(lines[ptr++]);

const snakeLength: number[] = [];
const snakeHead: number[] = [];

let headIdx = 0;
let offset = 0;

for (let i = 0; i < Q; i++) {
  const type = lines[ptr++];

  if (type === "1") {
    const l = Number(lines[ptr++]);

    if (snakeLength.length === 0) {
      snakeHead.push(0);
    } else {
      const prev = snakeHead.length - 1;
      snakeHead.push(snakeHead[prev] + snakeLength[prev]);
    }
    snakeLength.push(l);
  } else if (type === "2") {
    offset += snakeLength[headIdx];
    headIdx += 1;
  } else if (type === "3") {
    const k = Number(lines[ptr++]);
    const idx = headIdx + k - 1;
    const currentHeadPos = snakeHead[idx] - offset;
    console.log(currentHeadPos);
  }
}
