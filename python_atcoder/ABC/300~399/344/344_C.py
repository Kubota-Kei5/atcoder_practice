# %%
import bisect

N=int(input())
A=list(map(int, input().split()))
M=int(input())
B=list(map(int, input().split()))
L=int(input())
C=list(map(int, input().split()))
Q=int(input())
X=list(map(int, input().split()))

ABC=set()

for a in A:
    for b in B:
        for c in C:
            ABC.add(a+b+c)

for xi in X:
    if xi in ABC:
        print("Yes")
    else:
        print("No")