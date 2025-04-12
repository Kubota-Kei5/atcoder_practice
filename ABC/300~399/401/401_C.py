# %%
N, K = map(int, input().split())

MOD = 10**9
A=[1]*K
tmp=K
for i in range(K,N+1):
    A.append(tmp)
    tmp=(tmp*2-A[-K-1]) % MOD

ans=A[-1] 
print(ans)