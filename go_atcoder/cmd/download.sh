#!/usr/bin/env bash
set -eu

WORKSPACE="$(pwd)"
DEST_DIR="${WORKSPACE}/src"               # 生成先
TEMPLATE="${WORKSPACE}/templates/main.go"
CONTEST_FILE="${WORKSPACE}/contest"

# ファイル存在チェック
[ -f "${CONTEST_FILE}" ] || { echo "contest ファイルがありません"; exit 1; }
[ -f "${TEMPLATE}"     ] || { echo "テンプレートがありません"; exit 1; }

mkdir -p "${DEST_DIR}"
cd       "${DEST_DIR}"

# contest ファイルを走査（空行 + # コメント を除外）
grep -v '^\s*#' "${CONTEST_FILE}" | sed '/^\s*$/d' | while read -r CONTEST; do
  echo "=== Fetching ${CONTEST} ==="
  [ -d "${CONTEST}" ] && { echo "  → 既に存在、スキップ"; continue; }

  # 問題 + テストケースを取得
  acc new -c all "${CONTEST}"

  # 各問題 dir にテンプレ main.go を配置
  for dir in "${CONTEST}"/*; do
    [ -d "$dir" ] || continue
    [ -f "${dir}/main.go" ] || cp "${TEMPLATE}" "${dir}/main.go"
  done
done
