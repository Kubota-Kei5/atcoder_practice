# %%
# 解法：巣箱iにいる鳩の数n_pigeons_at[i]と，鳩iがいる巣箱pos[i]，複数の鳩がいる巣の個数n_mulを管理する．クエリ1で鳩が移動するたびに，これらの値を更新する．更新にはO(1)かかる．クエリ2では，n_mulを出力する．全体ではO(Q)かかる．
N, Q = map(int, input().split())

# 鳩iがいる巣箱pos[i]
pos = [i for i in range(N + 1)]

for _ in range(Q):
    query=list(map(int,input().split()))
    q=query[0]
    a=query[1]
    if len(query)==3:
        b=query[2]
    
    if q == 1:
        pos[a]=b
        # n_pigeons_at[]
    elif q == 2:
        for i in range(N+1):
            if pos[i]==b:
                pos[i]=a
            elif pos[i]==a:
                pos[i]=b
    else:
        print(pos[a])

# %%
import sys

input = sys.stdin.read
data = input().split()
index = 0

N = int(data[index])
Q = int(data[index + 1])
index += 2

pos = {i: i for i in range(1, N + 1)}
box = {i: i for i in range(1, N + 1)}

result = []
for _ in range(Q):
    q = int(data[index])
    a = int(data[index + 1])
    
    if q == 1:
        b = int(data[index + 2])
        index += 3
        pos[a] = b
    elif q == 2:
        b = int(data[index + 2])
        index += 3
        box[a], box[b] = box[b], box[a]
    else:
        index += 2
        result.append(str(box[pos[a]]))

sys.stdout.write("\n".join(result) + "\n")