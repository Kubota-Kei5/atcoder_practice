# %%
N = int(input())
A = list(map(int, input().split()))

total = sum(A)
ans = 0
for x in A:
    total -= x
    ans += x * total

print(ans)
