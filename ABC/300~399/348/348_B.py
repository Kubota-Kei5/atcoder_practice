# %%
import math
N=int(input())

X=[]
Y=[]

max_distance=[0]*N
point=[101]*N

for i in range(N):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)

for i in range(N):
    for j in range(N):
        if i==j:
            continue

        distance=math.sqrt((X[i]-X[j])**2+(Y[i]-Y[j])**2)
        
        if max_distance[i]<distance:
            max_distance[i]=distance
            point[i]=j+1
        elif max_distance[i]==distance:
            point[i]=min(point[i],j+1)


for i in range(N):
    print(point[i])
