# %%
S=list(input().strip())
T=list(input().strip())

pt=0
ans=[]
for i in range(len(S)):
    while S[i]!=T[i+pt]:
        pt+=1
    ans.append(i+pt+1)

print(*ans)