# %%
x1,y1,z1,x2,y2,z2 =list(map(int, input().split()))
x3,y3,z3,x4,y4,z4 =list(map(int, input().split()))

if x1<=x3<x2 and y1<=y3<y2 and z1<=z3<z2:
    print('Yes')
elif x1<x4<=x2 and y1<y4<=y2 and z1<z4<=z2:
    print('Yes')
else:
    print('No')