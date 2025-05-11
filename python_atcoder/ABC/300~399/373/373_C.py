# %%

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_A = max(A)
max_B = max(B)
ans = max_A + max_B
print(ans)