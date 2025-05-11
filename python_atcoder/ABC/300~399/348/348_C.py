# %%
N=int(input())

dict = {}

for i in range(N):
    a,c=map(int,input().split())
    if c in dict:
        dict[c] = min(dict[c], a)
    else:
        dict[c] = a

max_value = max(dict.values())
print(max_value)