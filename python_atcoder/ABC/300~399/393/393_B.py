# %%
S=str(input())
cnt=0
for i in range(len(S)-2):
    for j in range(i+1,len(S)-1):
        k=2*j-i
        if k<len(S) and S[i]=='A' and S[j]=='B' and S[k]=='C':
            cnt+=1

print(cnt)