n, r=map(int, input().split())
a =[list(map(int,input().split())) for _ in range(n)]


for i in range(n):
    if a[i][0]==1:
        if 1600<=r<=2799:
            r+=a[i][1]
    else:
        if 1200<=r<=2399:
            r+=a[i][1]

print(r)