# https://zenn.dev/koyanagihitoshi/books/atcoder-classification-4/viewer/10-2-1

# %%
import sys
sys.setrecursionlimit(10**6)
N,M=map(int,input().split())
graph=[[] for _ in range(N)]
for _ in range(M):
    A,B=map(int,input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)
check=[False]*N
def dfs(vertex):
    if not check[vertex]:
        check[vertex]=True
        for next_vertex in graph[vertex]:
            dfs(next_vertex)
            
S=0
for vertex in range(N):
    if not check[vertex]:
        S+=1
        dfs(vertex)
print(M-N+S)