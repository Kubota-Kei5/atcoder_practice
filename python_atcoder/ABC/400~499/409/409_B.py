# %%
N=int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

ans = 0
for i, v in enumerate(A, start=1):
    if v >= i:
        ans = i
    else:
        break

print(ans)