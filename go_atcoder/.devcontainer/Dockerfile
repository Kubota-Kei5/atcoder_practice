FROM golang:1.24-alpine AS builder

# ビルドに必要なパッケージをインストール
RUN apk add --no-cache git

# Go モジュールキャッシュ用ディレクトリ
WORKDIR /go/src/app

# go.mod をコピーして依存解決
COPY go.mod .
RUN go mod download

# ソースをコピーしてビルド
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o server ./hello.go

FROM alpine:latest

ARG USERNAME=k395599
ARG USER_ID=1000
ARG GROUP_ID=1000

# 非 root ユーザー追加
RUN addgroup -g ${GROUP_ID} ${USERNAME} \
 && adduser -D -u ${USER_ID} -G ${USERNAME} -s /bin/sh ${USERNAME}

# ビルド済バイナリだけをコピー
WORKDIR /home/${USERNAME}/app
COPY --from=builder /go/src/app/server .

# パーミッション調整
RUN chown -R ${USERNAME}:${USERNAME} /home/${USERNAME}/app \
 && chmod +x server

# コンテナ実行時のユーザー指定
USER ${USERNAME}
EXPOSE 8080

# 実行コマンド
ENTRYPOINT ["./server"]
