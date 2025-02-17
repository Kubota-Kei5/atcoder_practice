# %%
N=int(input())

P=list(map(int,input().split()))
l=[]
for i in range(N):
    l.append({P[i]:i+1})

print(l)

Q=int(input())

for i in range(Q):
    query=list(map(int,input().split()))
    comp=101
    for j in range(N):
        if l[j][0]==query[0] or l[j][0]==query[0]:
           comp=min(comp,l[j][1])
    print(comp) 
