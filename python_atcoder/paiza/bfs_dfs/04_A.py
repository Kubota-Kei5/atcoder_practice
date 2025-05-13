# move_obstacle
# %%
from collections import deque

H, W, N = map(int, input().split())
y, x = map(int, input().split())

grid = [list(input().rstrip()) for _ in range(H)]

visited = [[-1]*W for _ in range(H)]
queue = deque([(y, x)])
visited[y][x] = 0

while queue:
    cy, cx = queue.popleft()
    if visited[cy][cx] == N:
        continue
    for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
        ny, nx = cy+dy, cx+dx
        if (0 <= ny < H and 0 <= nx < W and
            grid[ny][nx] != '#' and visited[ny][nx] == -1):
            visited[ny][nx] = visited[cy][cx] + 1
            queue.append((ny, nx))

for i in range(H):
    for j in range(W):
        if visited[i][j] != -1 and visited[i][j] <= N:
            grid[i][j] = '*'

for row in grid:
    print(''.join(row))
# %%
