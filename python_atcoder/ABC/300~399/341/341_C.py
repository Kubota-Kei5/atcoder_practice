# %%
H,W,N=map(int,input().split())
T=str(input())

grid = [list(input().strip()) for _ in range(H)]


def judge_move(pos_i, pos_j, move, grid):
    if move == 'L' and pos_j != 0:
        if grid[pos_i][pos_j - 1] == '.':
            return pos_i, pos_j - 1
    elif move == 'R' and pos_j != W - 1:
        if grid[pos_i][pos_j + 1] == '.':
            return pos_i, pos_j + 1
    elif move == 'U' and pos_i != 0:
        if grid[pos_i - 1][pos_j] == '.':
            return pos_i - 1, pos_j
    elif move == 'D' and pos_i != H - 1:
        if grid[pos_i + 1][pos_j] == '.':
            return pos_i + 1, pos_j
    return None

cnt=0
for i in range(H):
    for j in range(W):
        if grid[i][j] != '.':
            continue
        h,w=i,j
        valid=True
        for t in T:
            new_pos = judge_move(h, w, t, grid)
            if new_pos is None:
                valid=False
                break
            h, w = new_pos
        if valid:
            cnt+=1

print(cnt)
