# %%
N = int(input())
P = list(map(int, input().split()))

D = []
for i in range(N - 1):
    if P[i+1] > P[i]:
        D.append(1)
    else:
        D.append(-1)

signs = []
lengths = []
current_sign = D[0]
current_count = 1

for i in range(1, len(D)):
    if D[i] == current_sign:
        current_count += 1
    else:
        signs.append(current_sign)
        lengths.append(current_count)

        current_sign = D[i]
        current_count = 1

signs.append(current_sign)
lengths.append(current_count)

ans = 0

for j in range(len(signs) - 2):
    s1, s2, s3 = signs[j],   signs[j+1],   signs[j+2]
    a,  b,  c  = lengths[j], lengths[j+1], lengths[j+2]

    if s1 == 1 and s2 == -1 and s3 == 1:
        ans += a * c

print(ans)