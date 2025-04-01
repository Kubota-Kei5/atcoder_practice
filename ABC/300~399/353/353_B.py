# %%
N, K=map(int,input().split())
A=list(map(int, input().split()))

cnt=0
seats=K

for i in range(N):
    if seats<A[i]:
        cnt+=1
        seats=K-A[i]
    else:
        seats-=A[i]

print(cnt+1)