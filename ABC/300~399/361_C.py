# %%
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

min_diff = A[N-1]-A[0]

for i in range(K):
    min_diff = min(min_diff, A[i+(N-K-1)]-A[i])

print(min_diff)
