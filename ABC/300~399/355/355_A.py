A = list(map(int, input().split()))

l=[1,2,3]
if A[0]==A[1]:
    print(-1)
else:
    for i in range(len(A)):
        l.remove(A[i])
    print(*l)