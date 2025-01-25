import math
n=int(input())

x_pos=0
y_pos=0
xl=[]
yl=[]
cost=0

for i in range(n):
    x,y=map(int,input().split())
    xl.append(x)
    yl.append(y)

for i in range(n):
    cost+=math.sqrt((x_pos-xl[i])**2+(y_pos-yl[i])**2)
    x_pos=xl[i]
    y_pos=yl[i]

cost+=math.sqrt((x_pos-0)**2+(y_pos-0)**2)
print(cost)