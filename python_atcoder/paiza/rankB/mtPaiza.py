# %%

H,W = map(int, input().split())

picture = [list(map(int, input())) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if picture[i][j] == 1:
            top_h = i
            top_w = j
            break
    else:
        continue
    break

ans=0

for i in range(top_h, H):
    for j in range(top_w, W):
        if picture[i][j] == 0:
            ans+=j-top_w
            break
        elif j == W-1:
            ans+=j-top_w
            break
    for k in reversed(range(0, top_w)):
        if picture[i][k] == 0:
            ans+=top_w-k
            break
        elif k==0:
            ans+=top_w-k
            break

print(ans)

# %%

H, W = map(int, input().split())
picture = [list(map(int, input().strip())) for _ in range(H)]

found = False
for i in range(H):
    for j in range(W):
        if picture[i][j] == 1:
            top_h = i
            top_w = j
            found = True
            break
    if found:
        break

ans = 0

left = top_w
while left > 0 and picture[top_h][left - 1] == 1:
    left -= 1

right = top_w
while right + 1 < W and picture[top_h][right + 1] == 1:
    right += 1

for i in range(top_h, H):
    if all(picture[i][j] == 0 for j in range(left, right + 1)):
        break
    for j in range(left, right + 1):
        if picture[i][j] == 1:
            ans += 1

print(ans)
