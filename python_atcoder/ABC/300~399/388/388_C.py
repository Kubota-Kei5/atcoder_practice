# %%
from bisect import bisect_left

N=int(input())
A=list(map(int,input().split()))

cnt=0
for i in range(N-1):
    x=bisect_left(A, A[i]*2)
    cnt+= (N-x)

print(cnt)