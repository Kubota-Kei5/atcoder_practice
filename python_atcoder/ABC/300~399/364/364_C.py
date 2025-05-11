# %%
N,X,Y=map(int,input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

def sweet_strategy(N,X,A):
    sweet=0
    A.sort(reverse=True)
    for i in range(N):
        sweet += A[i]
        if sweet >= X:
            sweet_cnt = i + 1
            return sweet_cnt
    return

def salty_strategy(N,Y,B):
    salty=0
    B.sort(reverse=True)
    for i in range(N):
        salty += B[i]
        if salty >= Y:
            salty_cnt = i + 1
            return salty_cnt
    return

min_sweet = sweet_strategy(N,X,A)
min_salty = salty_strategy(N,Y,B)
if min_sweet is None and min_salty is None:
    print(N)
elif min_sweet is None:
    min_sweet = N
elif min_salty is None:
    min_salty = N
else:
    min_cnt = min(min_sweet, min_salty)
    print(min_cnt)

# %%
# 累積和と二分探索で探索回数を短縮
# こっちでAC

from itertools import accumulate
from bisect import bisect_right

N,X,Y=map(int,input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

sorted_A=sorted(A,reverse=True)
sorted_B=sorted(B,reverse=True)

def sweet_strategy(X,sorted_A):
    prefix_A = list(accumulate(sorted_A))
    if prefix_A[-1] > X:
        index_sweet = bisect_right(prefix_A, X)
        sweet_cnt= index_sweet + 1
        return sweet_cnt
    else:
        sweet_cnt = None
        return sweet_cnt

def salty_strategy(Y,sorted_B):
    prefix_B= list(accumulate(sorted_B))
    if prefix_B[-1] > Y:
        index_salty = bisect_right(prefix_B, Y)
        salty_cnt = index_salty + 1
        return salty_cnt
    else:
        salty_cnt = None
        return salty_cnt
    
min_sweet = sweet_strategy(X,sorted_A)
min_salty = salty_strategy(Y,sorted_B)

if min_sweet is None and min_salty is None:
    print(N)
else:
    if min_sweet is None:
        min_sweet = N
    if min_salty is None:
        min_salty = N
    min_cnt = min(min_sweet, min_salty)
    print(min_cnt)
# %%
