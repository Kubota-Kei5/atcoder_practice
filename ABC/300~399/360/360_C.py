# %%
N=int(input())
A=list(map(int,input().split()))
W=list(map(int,input().split()))

X=[0]*(N+1)
for i in range(N):
    if X[A[i]]==0:
        X[A[i]]=W[i]
    else:
        X[A[i]]=max(X[A[i]],W[i])

print(sum(W)-sum(X))