# %%
S=list(input())
T=list(input())
X=[]
for i in range(len(S)):
    if S[i]!=T[i]:
        S[i]=T[i]
        X.append(''.join(S))

print(len(X))
[print(X[i]) for i in range(len(X))]