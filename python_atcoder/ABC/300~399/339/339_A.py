# %%
from collections import deque
S=str(input())

ans=deque([])
for s in reversed(S):
    if s!='.':
        ans.insert(0,s)
    else:
        print(''.join(ans))
        exit()
# %%
