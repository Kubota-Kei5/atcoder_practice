# %%
N = int(input())
l=[]
for i in range(1,N+1):
    if i%3==0:
        l.append('x')
    else:
        l.append('o')

print(*l, sep='')
# %%
