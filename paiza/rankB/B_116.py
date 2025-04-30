# B問題

# %%
# 入力
H, W, T = map(int, input().split())

# ギフトリストを [初期ギフト, 現在ギフト] の２要素で初期化
male   = [[f'M{i}', f'M{i}'] for i in range(H+1)]
female = [[f'F{j}', f'F{j}'] for j in range(W+1)]

# 位置と方向を保持 (direction: 0=正方向, 1=逆方向)
mpos = [[i, 0, 0] for i in range(H+1)]
fpos = [[0, j, 0] for j in range(W+1)]

def move(mpos, fpos):
    # 男性：横移動
    if mpos[1][2] == 0:  # 右向き
        if mpos[1][1] == W:
            for i in range(1, H+1):
                mpos[i][2] = 1
                mpos[i][1] -= 1
        else:
            for i in range(1, H+1):
                mpos[i][1] += 1
    else:  # 左向き
        if mpos[1][1] == 0:
            for i in range(1, H+1):
                mpos[i][2] = 0
                mpos[i][1] += 1
        else:
            for i in range(1, H+1):
                mpos[i][1] -= 1

    # 女性：縦移動
    if fpos[1][2] == 0:  # 下向き
        if fpos[1][0] == H:
            for j in range(1, W+1):
                fpos[j][2] = 1
                fpos[j][0] -= 1
        else:
            for j in range(1, W+1):
                fpos[j][0] += 1
    else:  # 上向き
        if fpos[1][0] == 0:
            for j in range(1, W+1):
                fpos[j][2] = 0
                fpos[j][0] += 1
        else:
            for j in range(1, W+1):
                fpos[j][0] -= 1

    return mpos, fpos

def present_change(mpos, fpos, male, female):
    for i in range(1, H+1):
        for j in range(1, W+1):
            if mpos[i][0] == fpos[j][0] and mpos[i][1] == fpos[j][1]:
                # 現在ギフトだけを交換
                male[i][1], female[j][1] = female[j][1], male[i][1]
                break
    return male, female

# Tターン実行
for _ in range(T):
    mpos, fpos = move(mpos, fpos)
    male, female = present_change(mpos, fpos, male, female)

# 出力
for i in range(1, H+1):
    print(male[i][1][0] + ' ' + male[i][1][1])
for j in range(1, W+1):
    print(female[j][1][0] + ' ' + female[j][1][1])