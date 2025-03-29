# %%
N=int(input())
A=list(map(int,input().split()))

sorted_A=sorted(A)
tmp={}
before=0
ans=0
for i in range(N):
    if sorted_A[i] not in tmp:
        tmp[sorted_A[i]]=1
        before=ans
        ans=sorted_A[i]
    else:
        tmp[sorted_A[i]]+=1
        ans=before

if ans==0:
    print(-1)
else:
    print(ans)

# %%
from collections import Counter

N = int(input())
A = list(map(int, input().split()))

freq = Counter(A)

unique_nums = []
for x in freq:
    if freq[x] == 1:
        unique_nums.append(x)

if len(unique_nums) == 0:
    print(-1)
else:
    print(A.index(max(unique_nums))+1)