1. ブラウザでログイン → DevTools → Application → Cookies
1. REVEL_SESSION を右クリックして **Copy value**

```bash
read -r RS
```

```bash
cat > ~/.config/atcoder-cli-nodejs/session.json <<JSON
{
  "cookies": [
    "REVEL_FLASH=",
    "REVEL_SESSION=$RS"
  ]
}
JSON
```

```bash
acc session
```