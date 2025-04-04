# %%
import math
H,W,N=map(int,input().split())


def main(H,W,N):
    grid=[['.']*W]*H 

    cnt=0

    for i in range(math.ceil(N/4)):
        
        if cnt!=N:
            pass
            cnt+=1
        else:
            print(grid)
# %%
def white_walk(pos, direction):
    if direction=='N':
        direction='E'
        pos[1]+=1
    elif direction=='E':
        direction='S'
        pos[0]+=1
    elif direction=='S':
        direction='W'
        pos[1]-=1
    elif direction=='W':
        direction='N'
        pos[0]-=1

    pos[0] %= H
    pos[1] %= W

    return pos,direction

def black_walk(pos, direction):
    if direction=='N':
        direction='W'
        pos[1]-=1
    elif direction=='E':
        direction='N'
        pos[0]-=1
    elif direction=='S':
        direction='E'
        pos[1]+=1
    elif direction=='W':
        direction='S'
        pos[0]+=1
    
    pos[0] %= H
    pos[1] %= W
    
    return pos, direction


def main(N,grid,pos,direction):
    for i in range(N):
        if grid[pos[0]][pos[1]]=='.':
            grid[pos[0]][pos[1]]='#'
            pos,direction=white_walk(pos, direction)
        else:
            grid[pos[0]][pos[1]]='.'
            pos,direction=black_walk(pos, direction)
    
    return grid

if __name__ == "__main__":
    H,W,N=map(int,input().split())
    grid=[['.']*W]*H 
    pos=[0,0]
    direction='N'
    result=main(N,grid,pos,direction)
    for row in result:
        print(''.join(row)) 