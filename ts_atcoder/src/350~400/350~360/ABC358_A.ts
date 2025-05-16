import { readFileSync } from "fs";

const tokens = readFileSync(0, "utf-8").trim().split(/\s+/);

let ptr = 0;
const S: string = tokens[ptr++].toString();
const T: string = tokens[ptr++].toString();

if (S === "AtCoder" && T === "Land") {
  console.log("Yes");
} else {
  console.log("No");
}
