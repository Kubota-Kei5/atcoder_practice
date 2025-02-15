# %%
N=int(input())
A=[]
for i in range(N):
    X=list(map(int,input().split()))
    A.append(X)
add=1
now=1

while add<N+1:
    if now>=add:
        now=A[now-1][add-1]
    else:
        now=A[add-1][now-1]
    add+=1

print(now)


# %%
