# %%

import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
vertex_list = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    u, v = a-1, b-1
    vertex_list[u].append(v)
    vertex_list[v].append(u)

# 辺の数チェック
if M != N:
    print("No")
    sys.exit()

# 次数チェック
if any(len(adj) != 2 for adj in vertex_list):
    print("No")
    sys.exit()

# 閉路検出
visited = [False]*N
stack = [0]
visited[0] = True
while stack:
    u = stack.pop()
    for v in vertex_list[u]:
        if not visited[v]:
            visited[v] = True
            stack.append(v)

if all(visited):
    print("Yes")
else:
    print("No")
