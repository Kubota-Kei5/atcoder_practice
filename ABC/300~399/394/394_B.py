# %%
N=int(input())
S=[]
ans=['']*50

for i in range(N):
    s=str(input())
    ans[len(s)-1]=s
    
print(''.join(ans))
# %%
