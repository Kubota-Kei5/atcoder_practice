# move_n_times
# %%
from collections import deque
H,W,N = map(int, input().split())
y,x = map(int, input().split())



visited = [[-1]*W for _ in range(H)]
queue = deque()
visited[y][x] = 0
queue.append((y,x))

while queue:
    cy, cx = queue.popleft()
    if visited[cy][cx] == N:
        continue
    for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
        ny, nx = cy+dy, cx+dx
        if 0 <= ny < H and 0 <= nx < W and visited[ny][nx] == -1:
            visited[ny][nx] = visited[cy][cx] + 1
            queue.append((ny,nx))


grid = [['.']*W for _ in range(H)]
grid[y][x] = '*'

for i in range(H):
    for j in range(W):
        if visited[i][j] != -1:
            grid[i][j] = '*'
        else:
            grid[i][j] = '.'

for row in grid:
    print(''.join(row))
# %%
