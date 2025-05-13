import { readFileSync } from "fs";

// 1. 標準入力を行単位で読み込む
const lines = readFileSync(0, "utf-8").trim().split("\n");

// 2. 1行目 → list1、2行目 → list2 にパース
const A: number[] = lines[0].trim().split(/\s+/).map(Number);
const B: number[] = lines[1].trim().split(/\s+/).map(Number);

const totalA: number = A.reduce((acc, cur) => acc + cur, 0);
const totalB: number = B.reduce((acc, cur) => acc + cur, 0);
const ans: number = totalA - totalB + 1;

console.log(ans);
