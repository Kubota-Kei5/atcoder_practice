# %%
n=int(input())
p=list(map(int, input().split()))
q=list(map(int, input().split()))

ans=[]
for i in range(n):
    for j in range(n):
        if q[j]==i+1:
            ans.append(q[p[j]-1])
            break

print(*ans)

# %%
n=int(input())
p=list(map(int, input().split()))
q=list(map(int, input().split()))

q_index = {q[i]: i for i in range(n)}
ans = [q[p[q_index[i+1]] - 1] for i in range(n)]

print(*ans)