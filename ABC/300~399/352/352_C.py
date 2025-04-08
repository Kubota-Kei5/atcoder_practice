# %%
N = int(input())

max_head = 0
ans=0

for i in range(N):
    a,b = map(int, input().split())
    ans+=a
    max_head = max(max_head, b-a)

ans+=max_head
print(ans)