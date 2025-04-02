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
else:
    min_cnt = min(min_sweet, min_salty)
    print(min_cnt)