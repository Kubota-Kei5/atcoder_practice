# %%
S=str(input())
S_li=[s for s in S]

A='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
A_li=[a for a in A]

pos=[]
for a in A:
    for s in S:
        if a==s:
            pos.append(S.index(s))

cnt=0
for i in range(len(pos)-1):
    cnt+=abs(pos[i]-pos[i+1])

print(cnt)
# %%
