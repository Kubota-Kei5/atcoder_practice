# https://atcoder.jp/contests/abc231/tasks/abc231_c

# %%

from bisect import bisect_left

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

X = [int(input()) for _ in range(Q)]

for i in range(Q):
    ix = bisect_left(A, X[i])
    ans= N - ix
    print(ans)

# %%
import bisect
a = [2, 3, 5, 7, 13, 17, 19]
print(bisect.bisect_left(a, 1))
print(bisect.bisect_right(a, 11))
print(bisect.bisect(a, 11))

# %%
