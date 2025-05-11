# %%
N, M, Q = map(int, input().split())

auth     = [ set() for _ in range(N) ]
all_auth = [False] * N

for _ in range(Q):
    query = list(map(int, input().split()))
    t = query[0]
    u = query[1] - 1

    if t == 1:
        p = query[2]
        auth[u].add(p)

    elif t == 2:
        all_auth[u] = True

    elif t == 3:
        p = query[2]
        if p in auth[u] or all_auth[u]:
            print("Yes")
        else:
            print("No")