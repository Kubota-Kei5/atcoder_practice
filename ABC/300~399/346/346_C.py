# %%
import bisect

N,K=map(int, input().split())

A=list(map(int, input().split()))

unique_A=list(set(A))
point=bisect.bisect_right(sorted(unique_A), K)

sigma=(K*(K+1))/2

ans=sigma-sum(unique_A[:point])
print(int(ans))