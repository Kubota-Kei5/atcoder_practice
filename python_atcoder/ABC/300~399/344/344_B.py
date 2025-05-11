# %%
l = []
for i in range(105):
    A = int(input())
    l.append(A)
    if A==0:
        break
for j in reversed(l):
    print(j)