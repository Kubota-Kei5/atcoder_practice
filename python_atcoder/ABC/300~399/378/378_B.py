# %%
N = int(input())
x=[]
for i in range(N):
    q,r=map(int,input().split())
    x.append([q,r])

Q = int(input())
y=[]
for i in range(Q):
    t,d=map(int,input().split())
    y.append([t,d]) 

for i in range(Q):
    t=y[i][0]
    d=y[i][1]
    q=x[t-1][0]
    r=x[t-1][1]
    if d<=r:
        print(r)
    elif d<=q+r:
        print(q+r)
    elif d<=(d//q)*q+r:
        print((d//q)*q+r)
    else:
        print(((d//q)+1)*q+r)