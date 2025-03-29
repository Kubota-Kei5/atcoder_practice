# %%
N=int(input())
S=list(str(input()))
T=list(str(input()))

ans=0
for i in range(N):
    if S[i] == T[i]:
        pass
    else:
        ans+=1
        
print(ans)

# %%
