N, M = map(int, input().split())
H = list(map(int, input().split()))

cnt=0

for i in range(N):
    if H[i]<=M:
        cnt+=1
        M-=H[i]
    else:
        break
print(cnt)