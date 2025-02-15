N = int(input())
S = [str(input()) for _ in range(N)]

cnt=0
for i in range(N):
    if S[i]=='Takahashi':
        cnt+=1

print(cnt)