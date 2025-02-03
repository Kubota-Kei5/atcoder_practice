# %%
X=[]
Y=[]
for i in range(3):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)

A=(X[0]-X[1])**2+(Y[0]-Y[1])**2
B=(X[1]-X[2])**2+(Y[1]-Y[2])**2
C=(X[0]-X[2])**2+(Y[0]-Y[2])**2

Z=[]
Z.append(A)
Z.append(B)
Z.append(C)

if max(Z)==sum(Z)-max(Z):
    print('Yes')
else:
    print('No')
# %%
