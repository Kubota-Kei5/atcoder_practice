N=int(input())

P=list(map(int,input().split()))
l={}
for i in range(N):
    l.update([(P[i],i+1)])

Q=int(input())

for i in range(Q):
    query=list(map(int,input().split()))
    a=l[query[0]]
    b=l[query[1]]
    if a<b:
        print(query[0])
    else:
        print(query[1]) 
