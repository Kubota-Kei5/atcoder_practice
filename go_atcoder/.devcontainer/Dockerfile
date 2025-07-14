# ベースイメージをGoの最新バージョンへ
FROM mcr.microsoft.com/devcontainers/go:1.22

WORKDIR /workspaces/go_atcoder

USER root
RUN go install github.com/securego/gosec/v2/cmd/gosec@v2.21.0 \
 && go install golang.org/x/tools/cmd/goimports@v0.24.0 \
 && go install github.com/cweill/gotests/gotests@latest

USER vscode