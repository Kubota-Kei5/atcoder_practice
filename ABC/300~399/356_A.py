N, L, R = map(int,input().split())
A = [i for i in range(1,N+1)]

print(*(A[0:L-1]+sorted(A[L-1:R],reverse=True)+A[R:]))