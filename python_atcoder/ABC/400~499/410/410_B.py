# %%
N, Q = map(int, input().split())
X = list(map(int, input().split()))
B= [0] * N
ans =[]

for i in range(Q):
    if X[i] >=1:
        B[X[i]-1] += 1
        ans.append(X[i])
    else:
        for j in range(N):
            if B[j]==min(B):
                B[j]+=1
                ans.append(j+1)
                break

print(*ans)
