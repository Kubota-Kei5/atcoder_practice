N = int(input())

S = [i for i in input()]
cnt = 0

for i in range(N-2):
    if S[i]=='#' and S[i+2]=='#' and S[i+1]=='.':
        cnt+=1
    else:
        pass

print(cnt)