# %%
N ,K = map(int, input().split())
A = list(map(int, input().split()))

ans=1
limit = 10**K
for i in range(N):
    ans*= A[i]
    if ans < limit:
        pass
    else:
        ans =1

print(ans)