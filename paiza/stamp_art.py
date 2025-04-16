# B問題

# %%

H ,W, N = map(int, input().split())

A=[]
for i in range(H*N):
    a=input()
    A.append(a)

tile_list = []
for i in range(N):
    tile = A[i*H:(i+1)*H]
    tile_list.append(tile)

R, C = map(int, input().split())
tile_index_map = []
for _ in range(R):
    tile_index_map.append(list(map(int, input().split())))

ans = []

for row in range(R):
    for h in range(H):
        line = ''
        for col in range(C):
            tile_id = tile_index_map[row][col] - 1
            line += tile_list[tile_id][h]
        ans.append(line)

for line in ans:
    print(line)

# %%
