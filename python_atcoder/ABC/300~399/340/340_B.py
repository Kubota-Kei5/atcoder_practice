# %%
Q=int(input())
A=[]
for i in range(Q):
    query=list(map(int,input().split()))

    if query[0]==1:
        A.append(query[1])
    else:
        print(A[-query[1]])