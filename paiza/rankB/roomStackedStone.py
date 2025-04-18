# %%

N=int(input())

stone_map = [list(map(int, input().split())) for _ in range(N)]

init_stone_map = [[0 for _ in range(N)] for _ in range(N)]

mid = (N//2)+1

for i in range(mid):
    for j in range(mid):
        init_stone_map[i][j]=min(i+1,j+1)

for i in range(mid):
    for j in range(mid,N):
        init_stone_map[i][j]=init_stone_map[i][N-j-1]

for i in range(mid, N):
    init_stone_map[i]=init_stone_map[N-i-1]
    
ans=0

for i in range(N):
    for j in range(N):
        ans+=stone_map[i][j]-init_stone_map[i][j]

print(ans)