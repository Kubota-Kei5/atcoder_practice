# %%

N, M=map(int,input().split())
B=list(map(int,input().split()))
W=list(map(int,input().split()))
B.sort(reverse=True)
W.sort(reverse=True)

prefixB = [0] * (N+1)
for i in range(N):
    prefixB[i+1] = prefixB[i] + B[i]

prefixW = [0] * (M+1)
for i in range(M):
    prefixW[i+1] = prefixW[i] + W[i]

bestWUpTo = [0] * (M+1)
bestWUpTo[0] = 0
for j in range(1, M+1):
    bestWUpTo[j] = max(bestWUpTo[j-1], prefixW[j])

ans = 0
for i in range(N+1):
    j = min(i, M)
    cur = prefixB[i] + bestWUpTo[j]
    ans = max(ans, cur)
print(ans)