N = int(input())
H = list(map(int,input().split()))

l=[]
for i in range(1,N):
    if H[i]>H[0]:
        l.append(i+1)

if len(l)==0:
    print(-1)
else:
    print(l[0])