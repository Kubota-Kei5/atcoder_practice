# %%
N=int(input())
for i in range(N):
    ans=[]
    A=list(map(int,input().split()))
    for j in range(N):
        if A[j]==1:
            ans.append(j+1)
    print(*ans)