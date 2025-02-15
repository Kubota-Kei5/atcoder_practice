A=list(map(int, input().split()))
B=sorted(A)

if B[2]==B[0]*B[1]:
    print('Yes')
else:
    print('No')
