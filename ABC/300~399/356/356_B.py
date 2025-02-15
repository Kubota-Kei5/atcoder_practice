# %%
import numpy as np
N,M=map(int,input().split())
A=list(map(int,input().split()))

for i in range(N):
    X=list(map(int,input().split()))
    nX=np.array(X)
    A=A-nX

for i in range(M):
    if A[i]>0:
        print('No')
        exit()
    
print('Yes')