# %%
N=int(input())
S=str(input())
Q=int(input())

# ヒント：for文でtranslateをQ回処理するのが大変
# 変換マップを作って1回のmaketransで済むようにする

for _ in range(Q):
    c,d=map(str,input().split())
    S=S.translate(str.maketrans({c:d}))

print(S)
