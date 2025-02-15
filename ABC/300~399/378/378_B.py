# %%
N=int(input())
x=[]
for i in range(N):
    a,b=map(int,input().split())
    x.append([a,b])

Q=int(input())
y=[]
for i in range(Q):
    a,b=map(int,input().split())
    y.append([a,b])

for j in range(Q):
    d=y[j][1]
    q=x[y[j][0]-1][0]
    r=x[y[j][0]-1][1]
    
    if d<=r:
        print(r)
    elif d%q==r:
        print(d)
    else:
        for i in range(30):
            if d<i*q+r:
                print(i*q+r)
                break
            else:
                pass

# %%
a=2
print(a//5)
# %%
