# %%
Q = int(input())
X = [list(map(int,input().split())) for _ in range(Q)]

l=[0]

for i in range(Q):
    if X[i][0]==1:
        l.append(X[i][1])
    elif X[i][0]==2:
        del l[1]
    elif X[i][0]==3:
        k=X[i][1]
        print(sum(list(l)[:k]))
        # print(sum(l[:k]))
# %%
import numpy as np

Q = int(input())
X = [list(map(int, input().split())) for _ in range(Q)]

l = np.array([0]) 

for i in range(Q):
    if X[i][0] == 1:
        l = np.append(l, X[i][1])
    elif X[i][0] == 2:
        if len(l) > 1:
            l = np.delete(l, 1)
    elif X[i][0] == 3:
        k = X[i][1]
        print(np.sum(l[:k]))

# %%
import numpy as np

Q = int(input())
X = [list(map(int, input().split())) for _ in range(Q)]

l = []  # ここではリストを使用
prefix_sum = [0]  # 累積和のリスト

for i in range(Q):
    if X[i][0] == 1:
        value = X[i][1]
        l.append(value)
        prefix_sum.append(prefix_sum[-1] + value)  # 累積和を更新
    elif X[i][0] == 2:
        if len(l) > 1:
            l.pop(1)  # 2番目の要素を削除
            prefix_sum = [0] + list(np.cumsum(l))  # 累積和を再計算
    elif X[i][0] == 3:
        k = X[i][1]
        print(prefix_sum[k])  # 累積和を使って部分和を高速に計算
# %%
