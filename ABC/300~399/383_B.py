from itertools import combinations

h,w,d=map(int,input().split())
s=[list(input()) for _ in range(h)]
floors=[]

for i in range(h):
    for j in range(w):
        if s[i][j]=='.':
            floors.append((i,j))
        else:
            continue

max_humidified=0

for (x1,y1),(x2,y2) in combinations(floors,2):
    humidified=set()
    for x,y in floors:
        if abs(x-x1)+abs(y-y1)<=d or abs(x-x2)+abs(y-y2)<=d:
            humidified.add((x,y))
    max_humidified=max(max_humidified, len(humidified))

print(max_humidified)