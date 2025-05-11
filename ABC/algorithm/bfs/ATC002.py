# https://atcoder.jp/contests/atc002/tasks/abc007_3
# %%
from collections import deque

R,C=map(int, input().split())
sy, sx=map(int, input().split())
gy, gx=map(int, input().split())

grid=[ list(str(input())) for _ in range(R)]

visited=[[-1]*C for _ in range(R)]

def bfs(sy, sx, gy, gx, grid, visited):
    sy-=1
    sx-=1
    gy-=1
    gx-=1
    visited[sy][sx]=0
    Q = deque([])
    Q.append([sy, sx])
    while Q:
        y,x = Q.popleft()

        if (y,x) == (gy, gx):
            return visited[y][x]
        
        for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny,nx = y+i, x+j
            if 0<=ny<R and 0<=nx<C and visited[ny][nx]==-1 and grid[ny][nx]==".":
                visited[ny][nx]=visited[y][x]+1
                Q.append([ny,nx])

    return -1

if __name__ == "__main__":
    print(bfs(sy, sx, gy, gx, grid, visited))