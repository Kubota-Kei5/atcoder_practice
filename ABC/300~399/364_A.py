N = int(input())
S=[input() for _ in range(N)]

for i in range(N-1):
    if S[i]=="sweet" and S[i+1]=="sweet":
        if i==N-2:
            print('Yes')
            break
        else:
            print('No')
            break
else:
    print('Yes')