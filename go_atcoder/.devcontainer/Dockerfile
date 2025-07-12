# ベースイメージをGoの最新バージョンへ
FROM golang:1.22.4

RUN useradd -ms /bin/bash vscode

WORKDIR /workspaces/go_atcoder

RUN go install github.com/securego/gosec/v2/cmd/gosec@latest \
    && go install golang.org/x/tools/cmd/goimports@latest \
    && go install github.com/cweill/gotests/...@latest

USER vscode