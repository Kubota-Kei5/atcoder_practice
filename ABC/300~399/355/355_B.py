N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

Ad={}
Bd={}
for i in range(N):
    Ad[A[i]]=1
for i in range(M):
    Bd[B[i]]=2

Ad.update(Bd)
l=sorted(Ad.items())

for i in range(N+M-1):
    if l[i][1]==l[i+1][1]==1:
        print('Yes')
        exit()

print('No')