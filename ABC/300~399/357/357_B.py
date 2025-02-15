# %%
S=str(input())
L=len(S)
upper_cnt=0
for i in range(L):
    if S[i].isupper():
        upper_cnt+=1

if L-upper_cnt<upper_cnt:
    print(S.upper())
else:
    print(S.lower())            
# %%
