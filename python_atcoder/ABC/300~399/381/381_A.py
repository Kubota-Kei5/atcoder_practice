N = int(input())
S = str(input())

left = S[:N//2]
mid = S[N//2]
right = S[N//2+1:]

if N%2==0:
    print('No')
elif left == '1'*(N//2) and mid == '/' and right == '2'*(N//2):
    print('Yes')
else:
    print('No')