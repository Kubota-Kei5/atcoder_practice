# %%
S = str(input())
N = len(S)
digits = list(map(int, S))

ans = 0

for i in range(N-1):
    diff = (digits[i] - digits[i+1] + 10) % 10
    ans += diff

ans += digits[-1]
ans += N
print(ans)