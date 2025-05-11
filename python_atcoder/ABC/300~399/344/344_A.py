# %%
S=str(input())
length_S=len(S)

tmp=[]

for i in range(length_S):
    if S[i]=="|":
        tmp.append(i)

print(S[0:tmp[0]]+S[tmp[1]+1:])