# %%

N=list(input())

for i in reversed(range(1,len(N))):
    if N[i]=='A' and N[i-1]=='W':
        N[i]='C'
        N[i-1]='A'

print(''.join(N))
# %%
