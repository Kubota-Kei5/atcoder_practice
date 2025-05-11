# %%

N=int(input())
A = list(map(int, input().split()))

B = []
for i in range(N):
    B.append(A[i])
    while True:
        if len(B)<=1:
            break
        elif B[-1]!= B[-2]:
            break
        elif B[-1]==B[-2]:
            B.pop(-1)
            B[-1]+=1

print(len(B))

