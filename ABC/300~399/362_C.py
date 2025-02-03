# %%
N=int(input())

L=[]
R=[]
X=L
for i in range(N):
    l,r=map(int,input().split())
    L.append(l)
    R.append(r)

# 重要なポイント：
# sum(L)>0もしくはsum(R)<0のときsum(X)=0の条件を満たすXは存在しない
# sum(X)=0に対して今どれくらいの差分があるのか
# 差分を埋めるためにはL[i]とR[i]をどう扱えばいいのか