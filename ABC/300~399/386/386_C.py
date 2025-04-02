# %%
K = int(input())
S = input().strip()
T = input().strip()

# 長さの差が1より大きい場合は1回の操作では不可能
if abs(len(S) - len(T)) > 1:
    print("No")
    exit()

# 0回の操作で一致する場合
if S == T:
    print("Yes")
    exit()

# SとTの長さが同じ場合 → 文字の置換で一致させるケース
if len(S) == len(T):
    diff_count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            diff_count += 1
    if diff_count <= 1:
        print("Yes")
    else:
        print("No")
        
# SがTより短い場合 → Sに1文字挿入してTにする（Sの長さ + 1 == Tの長さ）
elif len(S) + 1 == len(T):
    pt = 0  # 挿入によるずれの数
    for i in range(len(S)):
        if S[i] != T[i + pt]:
            pt += 1
            if pt > 1:
                print("No")
                exit()
            # 挿入した後の文字が一致するか確認
            if S[i] != T[i + pt]:
                print("No")
                exit()
    print("Yes")
    
# SがTより長い場合 → Sから1文字削除してTにする（Sの長さ - 1 == Tの長さ）
elif len(S) - 1 == len(T):
    pt = 0  # 削除によるずれの数
    for i in range(len(T)):
        if S[i + pt] != T[i]:
            pt += 1
            if pt > 1:
                print("No")
                exit()
            if S[i + pt] != T[i]:
                print("No")
                exit()
    print("Yes")
