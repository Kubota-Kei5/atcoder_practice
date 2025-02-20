# %%
import math
H,W,N=map(int,input().split())

grid=[['.']*W]*H 

cnt=0

for i in range(math.ceil(N/4)):
    
    if cnt!=N:
        pass
        cnt+=1
    else:
        print(grid)
