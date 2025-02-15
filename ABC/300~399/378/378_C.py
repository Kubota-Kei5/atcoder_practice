# %%
from collections import defaultdict
N,M=map(int,input().split())
X=list(map(int,input().split()))
A=list(map(int,input().split()))

ans=defaultdict(int)
cnt=0

for i in range(M):
    ans[X[i]-1]=A[i]

for i in range(N-1):
    if ans[i]==0:
        print(-1)
        exit()
    elif ans[i]>1:
        cnt+=ans[i]-1
        ans[i+1]+=ans[i]-1
        ans[i]=1

if ans[N-1]==1:
    print(cnt)
else:
    print(-1)
# %%
# N,M=map(int,input().split())
# X=list(map(int,input().split()))
# A=list(map(int,input().split()))

# list=[0]*N
# pertial_list=[]
# start=0
# for i in range(M):
#     list[X[i]-1]=A[i]

# for i in range(N):
#     if list[i]==0 and list[i+1] >= 1:
#         pertial_list.append(list[start:i+1])

# length=len(pertial_list)

# for i in range(length):
#     sum(length)==