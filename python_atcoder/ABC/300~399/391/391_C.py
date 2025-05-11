# %%
# Retry




# %%
# 解法：巣箱iにいる鳩の数n_pigeons_at[i]と，鳩iがいる巣箱pos[i]，複数の鳩がいる巣の個数n_mulを管理する．クエリ1で鳩が移動するたびに，これらの値を更新する．更新にはO(1)かかる．クエリ2では，n_mulを出力する．全体ではO(Q)かかる．
N, Q = map(int, input().split())
# 複数の鳩がいる巣の個数
n_mul = 0
# 巣箱iにいる鳩の数n_pigeons_at[i]
n_pigeons_at = [1] * (N + 1)
# 鳩iがいる巣箱pos[i]
pos = [i for i in range(N + 1)]

for _ in range(Q):
    s = input()
    if s[0] == "1":
        _, p, h_new = map(int, s.split())
        h_old = pos[p]

        n_pigeons_at[h_old] -= 1
        if n_pigeons_at[h_old] == 1:
            n_mul -= 1

        n_pigeons_at[h_new] += 1
        if n_pigeons_at[h_new] == 2:
            n_mul += 1
        pos[p] = h_new
    if s[0] == "2":
        print(n_mul)