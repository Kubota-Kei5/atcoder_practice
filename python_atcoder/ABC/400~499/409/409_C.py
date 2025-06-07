# %%
N,L=map(int, input().split())
D=list(map(int, input().split()))

# pos[n]にある点iを格納
pos = [[] for _ in range(L)]

cur = 0
pos[cur].append(1)

for i, d in enumerate(D, start=2):
    cur = (cur + d) % L
    pos[cur].append(i)

if L%3!=0:
    print(0)
    exit()

k=L//3

ans=0
for i in range(k):
    a = pos[i]
    b = pos[(i + k) % L]
    c = pos[(i + 2 * k) % L]
    if a and b and c:
        ans += len(a) * len(b) * len(c)

print(ans)

# %%
