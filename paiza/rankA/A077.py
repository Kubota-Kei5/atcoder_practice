# %%

N, R = map(int, input().split())

volcano_map=[]
# volcano_mapの初期化
for i in range(N):
    volcano_map.append(list(map(int, input().split())))

# volcano間の距離がR以下の場合は記録
chain_map = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            chain_map[i].append(j)
        else:
            distance=abs(volcano_map[i][0] - volcano_map[j][0])+abs(volcano_map[i][1] - volcano_map[j][1])
            if distance <=R:
                chain_map[i].append(j)

sets=[]
for i in range(N):
    sets.append(set(chain_map[i]))
   

visited = [False] * N
group_cnt=0

for i in range(N):
    if not visited[i]:
        group_cnt+=1
        stack = [i]
        merged=sets[i].copy()
        visited[i]=True

        while stack:
            cur = stack.pop()
            for j in range(N):
                if not visited[j] and merged & sets[j]:
                    visited[j]=True
                    stack.append(j)
                    merged |= sets[j]

print(group_cnt)

# %%
N, R = map(int, input().split())
volcano_map = [tuple(map(int, input().split())) for _ in range(N)]
chain_map = [[] for _ in range(N)]
threshold_sq = (2 * R) ** 2

for i in range(N):
    xi, yi = volcano_map[i]
    for j in range(N):
        if i == j:
            continue
        xj, yj = volcano_map[j]
        dx = xi - xj
        dy = yi - yj
        if dx*dx + dy*dy <= threshold_sq:
            chain_map[i].append(j)

visited = [False] * N
group_cnt = 0

for i in range(N):
    if not visited[i]:
        group_cnt += 1
        stack = [i]
        visited[i] = True
        while stack:
            cur = stack.pop()
            for nb in chain_map[cur]:
                if not visited[nb]:
                    visited[nb] = True
                    stack.append(nb)


print(group_cnt)
