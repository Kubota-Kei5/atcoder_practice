# TypeScirptの競プロ文法まとめ

PythonistaがTypeScirptにコンバートした際に覚えた文法をメモしていく

## 標準入力

node.jsの標準モジュールであるfsを使って標準入力を受け取る。
おまじないだと思って毎回書く。

```typescript
// ts/src/Main.ts
import { readFileSync } from "fs";

// まとめて読み込んで空白ごとに分割
const input = readFileSync(0, "utf-8").trim().split(/\s+/);
let ptr = 0;
```

### 1. 半角区切りで複数の数字を受け取る

ポインタを使って一個ずつ受け取る

```typescript
// Python: N,M = map(int, input().split())
const N = Number(input[ptr++]);
const M = Number(input[ptr++]);
```

### 2. 文字列として受け取る

```typescript
// Python: N = str(input())
const s = input[ptr++];
```

### 3. listに格納していく

一個ずつ受け取ってlistにpushしていく

```typescript
// Python: A = list(map(int, input().split()))
import { readFileSync } from "fs";

// 1) 標準入力を文字列として読み込み
const line = readFileSync(0, "utf-8").trim();

// 2) 空白で分割してから Number に変換
const list: number[] = line
  .split(/\s+/) // ["0","1","0","1","2","2","0","0","1"]
  .map(Number); // [0, 1, 0, 1, 2, 2, 0, 0, 1]
```

### 4. 2次元配列を作る

```typescript
// python:
// hoge_map = []
// for i in range(N):
//    huga = list(map(int, input().split()))
//    hoge_map.append(huga)

// N, M を先に読み取る
const N = Number(tokens[ptr++]);
const M = Number(tokens[ptr++]);

// 2次元配列を手動で組み立て
const hoge_map: number[][] = [];
for (let i = 0; i < N; i++) {
  const row: number[] = [];
  for (let j = 0; j < M; j++) {
    row.push(Number(tokens[ptr++])); // トークンを順に消費
  }
  hoge_map.push(row);
}
```

### 5. グリッドを作る

```typescript
// Python: X = [[.]*N for _ in range(N)]
const X: string[][] = Array.from({ length: N }, () =>
  Array<string>(N).fill(".")
);
```

## 出力

## 型変換/型判定

### 1. 値を数値に変換

Numberコンストラクターを使う

```typescript
// ベーシックな書き方
const n1 = Number("123");

//短縮形の+演算子もある → かっこいいからこっちのほうがおすすめ
const n = +"123";
```

<details>
<summary>
その他**Number**オブジェクトの便利な関数・定数
</summary>

| プロパティ／メソッド              | 説明                                                               |
| --------------------------------- | ------------------------------------------------------------------ |
| `Number.POSITIVE_INFINITY`        | 正の無限大。`1/0` の結果など。                                     |
| `Number.NEGATIVE_INFINITY`        | 負の無限大。`-1/0` の結果など。                                    |
| `Number.isFinite(value)`          | 引数が有限の数値かどうかを判定。`Infinity` や `NaN` は `false`。   |
| `Number.isInteger(value)`         | 引数が整数かどうかを判定。小数点以下がある値は `false`。           |
| `Number.parseInt(string[,radix])` | 文字列を整数に変換。グローバルの `parseInt` と同じ機能。           |
| `Number.parseFloat(string)`       | 文字列を浮動小数点数に変換。グローバルの `parseFloat` と同じ機能。 |

</details>

### 2. 値を文字列に変換

文字列に変換する（=pyhonでいうstr()に相当する）方法は主に3つ

| 方法                       | 説明                                                   |
| -------------------------- | ------------------------------------------------------ |
| `String(value)`            | 任意の値を文字列に変換するビルトイン関数。             |
| `value.toString()`         | オブジェクトのメソッド。ほとんどの組み込み型で利用可。 |
| テンプレートリテラル `${}` | 式を埋め込む形で文字列化。非文字列でも安全に扱える。   |

```typescript
const n = 123;
const b = true;
const obj = { x: 1 };

// 1) String()
console.log(String(n)); // "123"
console.log(String(b)); // "true"
console.log(String(obj)); // "[object Object]"

// 2) .toString()
console.log(n.toString()); // "123"
console.log(b.toString()); // "true"

// 3) テンプレートリテラル
console.log(`${n}`); // "123"
console.log(`${b}`); // "true"
console.log(`${obj}`); // "[object Object]"
```
