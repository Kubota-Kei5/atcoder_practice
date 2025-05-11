# %%
from collections import deque
Q=int(input())

d=deque([0]*100)

for i in range(Q):
    query=list(map(int,input().split()))
    a=query[0]
    if len(query)==2:
        b=query[1]
        d.append(b)
    else:
        print(d[-1])
        d.pop()