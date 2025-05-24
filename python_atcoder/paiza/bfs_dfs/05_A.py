# https://paiza.jp/works/mondai/bfs_dfs_problems/bfs_dfs_problems__judge_reach
# %%
from collections import deque

H, W= map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

grid = [list(input().rstrip()) for _ in range(H)]

visited = [[-1]*W for _ in range(H)]
queue = deque([(sy, sx)])
visited[sy][sx] = 0

while queue:
    cy, cx = queue.popleft()
    if visited[cy][cx] == 0:
        continue
    for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
        ny, nx = cy+dy, cx+dx
        if (0 <= ny < H and 0 <= nx < W and
            grid[ny][nx] != '#' and visited[ny][nx] == -1):
            visited[ny][nx] = 0
            queue.append((ny, nx))

if visited[gy][gx] == -1:
    print("No")
else:
    print("Yes")
# %%
from collections import deque

H, W = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

sy -= 1; sx -= 1
gy -= 1; gx -= 1

grid = [list(input().rstrip()) for _ in range(H)]

visited = [[False]*W for _ in range(H)]
queue = deque([(sy, sx)])
visited[sy][sx] = True

dirs = [(-1,0), (1,0), (0,-1), (0,1)]

while queue:
    y, x = queue.popleft()
    if (y, x) == (gy, gx):
        break
    for dy, dx in dirs:
        ny, nx = y + dy, x + dx
        if 0 <= ny < H and 0 <= nx < W:
            if not visited[ny][nx] and grid[ny][nx] != '#':
                visited[ny][nx] = True
                queue.append((ny, nx))

print("Yes" if visited[gy][gx] else "No")