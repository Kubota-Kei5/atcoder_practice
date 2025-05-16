import { readFileSync } from "fs";

const tokens = readFileSync(0, "utf-8").trim().split(/\s+/);

const S: string = tokens[0];

if (S === "RMS" || S === "RSM" || S === "SRM") {
  console.log("Yes");
} else {
  console.log("No");
}
