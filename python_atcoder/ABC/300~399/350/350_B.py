# %%
N,Q=map(int,input().split())

T=list(map(int,input().split()))

teeth=[1]*(N+1)

for i in range(Q):
    if teeth[T[i]] == 1:
        teeth[T[i]]=0
    else:
        teeth[T[i]]=1

ans=sum(teeth)-1 #0_indexedにしているためindex=0の分を引く
print(ans)