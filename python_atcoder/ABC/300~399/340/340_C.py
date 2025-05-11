# %%
import math
from collections import deque

a=[]
a.append(int(input()))
d=deque(a)
spend=0

while d:
    x=d.popleft()
    if x>=2:
        spend+=x
        floor_x=math.floor(x/2)
        ceil_x=math.ceil(x/2)

        if floor_x != x:
            d.append(floor_x)
        if ceil_x != x:
            d.append(ceil_x)

print(spend)
# %%
import math
from collections import deque

a=[]
a.append(int(input()))
d=deque(a)
spend=0

while d:
    x=d.popleft()
    if x>=2:
        spend+=x
        d.append(math.floor(x/2))
        d.append(math.ceil(x/2))

print(spend)