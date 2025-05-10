# %%

from collections import deque
N,M = map(int, input().split())
A= list(map(int, input().split()))
A = deque(A)
# 1~Mのリストを作成
bad= [ i for i in range(1,M+1)]

# 1~Mの数字がすべて含まれないようなリストになるまでAをpopする
cnt=0
for i in range(N):
    if set(A)!=set(bad):
        print(cnt)
        exit()
    A.pop()
    cnt+=1

print(cnt)