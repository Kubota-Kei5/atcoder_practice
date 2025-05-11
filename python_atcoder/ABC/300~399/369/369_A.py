a = sorted(map(int,input().split()))
x_cnt=0

for x in range(-100,200):
    a.append(x)
    a.sort()
    if a[1]-a[0]==a[2]-a[1]:
        x_cnt+=1
        a.remove(x)
    else:
        a.remove(x)
print(x_cnt)