# move_three_times
# %%
def move_grid(y, x, grid, n_map, step, H, W):
    for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
        ny, nx = y+dy, x+dx
        if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] == '.':
            grid[ny][nx] = '*'
            n_map[step].append((ny, nx))
    return grid, n_map

def n_steps_grid(n, y, x, grid, n_map):
    H, W = len(grid), len(grid[0])
    n_map[0].append((y,x))
    for step in range(1, n+1):
        for py, px in n_map[step-1]:
            grid, n_map = move_grid(py, px, grid, n_map, step, H, W)
    return grid, n_map


H, W = map(int, input().split())
y, x = map(int, input().split())
grid = [['.']*W for _ in range(H)]
grid[y][x] = '*'

# 初期値からnマス移動が必要
n=3

# i番目には初期位置からiマスの移動が必要な位置を記録
n_map = [ [] for _ in range(n+1) ]

grid, n_map = n_steps_grid(n, y, x, grid, n_map)

for row in grid:
    print(''.join(row))