# https://atcoder.jp/contests/abc213/tasks/abc213_d

# %%
import sys
sys.setrecursionlimit(300000)
N=int(input())
AB=[[] for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,input().split())
    AB[a].append(b)
    AB[b].append(a)
for i in range(N+1):
    AB[i].sort()

ans=[]
def dfs(u,p):
    ans.append(u)
    for v in AB[u]:
        if v!=p:
            dfs(v,u)
            ans.append(u)
            
dfs(1,-1)
print(*ans)
# %%
