# %%
from itertools import combinations

N=int(input())
A=list(map(int, input().split()))

X=[i for i in range(1, len(A)+1)]

comb = list(combinations(X, 2))

ans=0

for i in range(len(comb)):
    i,j=comb[i]
    i-=1
    j-=1
    ans+=A[i]*A[j]

print(ans)
