# %%
N, a, b = map(str, input().split(" "))
N=int(N)
S = str(input())

for i in range(N):
    if S[i]==a:
        pass
    else:
        S=S.replace(S[i], b)

print(S)
# %%
