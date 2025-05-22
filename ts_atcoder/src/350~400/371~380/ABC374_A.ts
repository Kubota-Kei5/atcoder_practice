import { readFileSync } from "fs";

const lines = readFileSync(0, "utf-8").trim().split(/\s+/);
const S: string = lines[0];

const arrayS: string[] = S.split("");

let char: string = arrayS.slice(-3).join("");

if (char === "san") {
  console.log("Yes");
} else {
  console.log("No");
}
