# B問題

# %%
from itertools import combinations

N, M = map(int, input().split())
C=list(map(int, input().split()))
S=list(map(int, input().split()))
d=list(map(int, input().split()))
index=[i for i in range(N)]
comb_list = list(combinations(index, M))

