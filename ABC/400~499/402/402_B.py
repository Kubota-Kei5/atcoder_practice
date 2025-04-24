# %%
from collections import deque

Q= int(input())

wait=deque()

for i in range(Q):
    query = list(input())
    if len(query)==1:
        print(wait.popleft())
    elif len(query)==3:
        wait.append(query[2])


# %%
from collections import deque

Q = int(input())
wait = deque()

for _ in range(Q):
    parts = input().split()
    cmd = parts[0]

    if cmd == '1':
        x = parts[1]
        wait.append(x)
    elif cmd == '2':
        if wait:
            print(wait.popleft())
        else:
            pass
