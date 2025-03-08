# %%
from functools import reduce
import operator

def find_all_label_paths(N, labeled_edges):
    graph = [[] for _ in range(N+1)]
    for (u, v, w) in labeled_edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    all_label_paths = []
    visited = [False] * (N+1)

    def dfs(current_vertex, label_path):
        if current_vertex == N:
            all_label_paths.append(label_path[:])
            return

        for (nxt, edge_label) in graph[current_vertex]:
            if not visited[nxt]:
                visited[nxt] = True
                label_path.append(edge_label)

                dfs(nxt, label_path)

                label_path.pop()
                visited[nxt] = False

    visited[1] = True
    dfs(1, [])

    return all_label_paths

N, M=map(int,input().split())
l=[]
for i in range(M):
    u,v,w=map(int,input().split())
    l.append((u,v,w))


routes = find_all_label_paths(N, l)
ans=float('inf')
for r in routes:
    ans=min(ans,reduce(operator.xor, r, 0))
    
print(ans)