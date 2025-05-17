# %%
H,W,N = map(int, input().split())
garbage_map = [[0]*W for _ in range(H)]

for i in range(N):
    X,Y = map(int, input().split())
    X -= 1
    Y -= 1
    garbage_map[X][Y] += 1

Q=int(input())

def X_sum(garbage_map,x):
    X_sum = sum(garbage_map[x])
    return X_sum

def Y_sum(garbage_map,y):
    Y_sum = 0
    for i in range(H):
        Y_sum += garbage_map[i][y]
    return Y_sum


for i in range(Q):
    query = list(map(str, input().split()))
    if query[0] == '1':
        x=int(query[1])-1
        print(X_sum(garbage_map,x))
        garbage_map[x]=[0]*W
    elif query[0] == '2':
        y=int(query[1])-1
        print(Y_sum(garbage_map,y))
        for j in range(H):
            garbage_map[j][y]=0


# %%

from collections import defaultdict

H, W, N = map(int, input().split())

row_map = [defaultdict(int) for _ in range(H)]
col_map = [defaultdict(int) for _ in range(W)]
row_sum = [0] * H
col_sum = [0] * W

for _ in range(N):
    x, y = map(int, input().split())
    x -= 1; y -= 1
    row_map[x][y] += 1
    col_map[y][x] += 1
    row_sum[x] += 1
    col_sum[y] += 1

Q = int(input())
for _ in range(Q):
    t, v = map(str, input().split())
    v = int(v) - 1

    if t == '1':
        print(row_sum[v])
        for y, cnt in row_map[v].items():
            col_sum[y] -= cnt
            del col_map[y][v]
        row_map[v].clear()
        row_sum[v] = 0

    elif t == '2':
        print(col_sum[v])
        for x, cnt in col_map[v].items():
            row_sum[x] -= cnt
            del row_map[x][v]
        col_map[v].clear()
        col_sum[v] = 0
