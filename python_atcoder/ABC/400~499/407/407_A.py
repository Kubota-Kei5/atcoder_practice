# %%
import math
A, B = map(int, input().split())

X = math.ceil(A / B) - (A/B)
Y = (A/B) - math.floor(A / B)

if X < Y:
    print(math.ceil(A / B))
else:
    print(math.floor(A / B))
# %%
