# %%
N=int(input())
A=[]
B=[]

for i in range(N):
    a = list(input())
    A.append(a)

for i in range(N):
    b = list(input())
    B.append(b)

for i in range(N):
    for j in range(N):
        if A[i][j] != B[i][j]:
            print(f'{i+1} {j+1}')