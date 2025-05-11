N, K =map(int,input().split())
A = list(map(int,input().split()))
l=[]
for i in range(N):
    if A[i]%K==0:
        l.append(A[i]//K)
        
print(*l)