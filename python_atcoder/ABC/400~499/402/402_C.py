# %%
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

ingredient = [[] for _ in range(N+1)]

dislike_cnt = [0] * M

for j in range(M):
    data = list(map(int, input().split()))
    k = data[0]
    dislike_cnt[j] = k
    for idx in range(1, k+1):
        a = data[idx]
        ingredient[a].append(j)

B = list(map(int, input().split()))

available = 0
for b in B:
    for j in ingredient[b]:
        dislike_cnt[j] -= 1
        if dislike_cnt[j] == 0:
            available += 1
    print(available)
