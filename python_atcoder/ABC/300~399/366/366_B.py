# %%
N=int(input())
S=[list(input()) for _ in range(N)]
M=0
for i in range(len(S)):
    M=max(M,len(S[i]))

for i in range(len(S)):
    while len(S[i])!=M:
        S[i].append('*')

def abstract_text(list,num):
    ans=[]
    for i in reversed(range(len(list))):
        ans.append(list[i][num])
    output=''.join(ans).rstrip('*')
    return print(output)

for j in range(M):
    abstract_text(S,j)
# %%

# %%
