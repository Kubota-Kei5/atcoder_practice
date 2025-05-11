# %%
# WCだったコード
N=int(input())
A=list(map(int, input().split()))
r=A[1]/A[0]
cnt=0
is_geometric=True
for i in range(1,len(A)-1):
    if A[i+1]/A[i]!=r:
        is_geometric=False
        break

if is_geometric:
    print('Yes')
else:
    print('No')
# %%
# ACだったコード
N=int(input())
A=list(map(int, input().split()))
r=A[1]/A[0]

l=[]
l.append(A[0])
l.append(A[1])
for i in range(1,len(A)-1):
    l.append(A[i]*r)

if A==l:
    print('Yes')
else:
    print('No')