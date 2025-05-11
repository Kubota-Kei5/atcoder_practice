# %%
from collections import deque
N=int(input())
S=str(input())
end=0

for i in range(N-1,-1,-1):
    if S[i]==1:
        end=i
        break
zero_locate=deque()
zero_locate.append(end)
cnt=0
for j in range(end-1,-1,-1):
    if S[j]==0:
        zero_locate.append(j)
    elif zero_locate:
        cnt+=zero_locate.pop()-j

print(cnt)

# %%
