# %%
N,M=map(int,input().split())
cnt=0
edges=set()

for i in range(M):
    u,v=map(int,input().split())
    # 自己ループ
    if u==v:
        cnt+=1
        break
    # 多重辺
    comb=frozenset({u,v})
    if comb in edges:
        cnt+=1
        break
    else:
        edges.add(comb)

print(cnt)
