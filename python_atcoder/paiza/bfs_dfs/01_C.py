# %%
H,W=map(int, input().split())
y,x=map(int, input().split())

grid=[['.']*W for _ in range(H)]

grid[y][x]='*'

if H>1:
    if y==0:
        grid[y+1][x] = '*'
    elif y==H-1:
        grid[y-1][x] = '*'
    else:
        grid[y+1][x] = '*'
        grid[y-1][x] = '*'

if W>1:
    if x==0:
        grid[y][x+1] = '*'
    elif x==W-1:
        grid[y][x-1] = '*'
    else:
        grid[y][x+1] = '*'
        grid[y][x-1] = '*'

for i in range(H):
    print(''.join(grid[i]))
