N, C = map(int,input().split())
T = list(map(int, input().split()))

cnt = 0
t = 0

for i in range(N):
    if i ==0:
        cnt+=1
        t=i
    else:
        if T[i]-T[t]>=C:
            cnt+=1
            t=i
        else:
            pass

print(cnt)