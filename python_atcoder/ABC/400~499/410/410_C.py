# %%
N,Q=map(int, input().split())
A=[i for i in range(1,N+1)]
offset = 0

for _ in range(Q):
    q=list(map(int, input().split()))
    if q[0] == 1:
        p = (q[1] - 1 + offset) % N
        x= q[2]
        A[p] = x
    elif q[0] == 2:
        p = (q[1] - 1 + offset) % N
        print(A[p])
    else:
        k = q[1] % N
        offset = (offset + k) % N
# %%
A=[1,2,3,4,5,6,7,8,9,10]

print(A[3:])
print(A[:3])
A = A[3:] + A[:3]

print(A)


# %%
