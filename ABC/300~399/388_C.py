# %%
#　binary search
N=input()
A=list(map(int,input().split()))
cnt=0

for i in range(N-1):
    for j in range(i,N-1):
        if A[i]*2<A[j]:
            cnt+=1