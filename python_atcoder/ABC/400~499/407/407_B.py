# %%
X, Y = map(float, input().split())

prob = 0

for i in range(1,7):
    for j in range(1,7):
        if X <= i + j or Y <= abs(i - j):
            prob += 1

print(prob/36)

# %%
