# %%
S=list(input())

ans=set()
for width in range(1,len(S)+1):
    for i in range(len(S)-width+1):
        ans.add(tuple(S[i:i+width]))    

print(len(ans))