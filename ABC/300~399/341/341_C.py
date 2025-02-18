# %%
H,W,N=map(int,input().split())
T=str(input())

grid=[list(map(str,input().split()))]

def judge_move(pos_i,pos_j,move,grid):
    if move=='L' and pos_j!=0:
        if grid[pos_i][pos_j-1]=='.':
            return pos_i,pos_j-1
        else:
            return False
    elif move=='R' and pos_j!=len(grid[0]):
        if grid[pos_i][pos_j+1]=='.':
            return pos_i,pos_j+1
        else:
            return False
    elif move=='U' and pos_i!=0:
        if grid[pos_i+1][pos_j]=='.':
            return pos_i+1,pos_j
        else:
            return False
    elif move=='D' and pos_i!=len(grid):
        if grid[pos_i-1][pos_j]=='.':
            return pos_i-1,pos_j
        else:
            return False
    else:
        return False
cnt=0
for h in range(H):
    for w in range(W):
        for t in T:
            if judge_move(h,w,t,grid)==False:
                break
            else:
                h,w=judge_move(h,w,t,grid)
        cnt+=1
            
print(cnt)
