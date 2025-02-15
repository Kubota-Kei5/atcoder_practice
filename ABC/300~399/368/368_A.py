N, K = map(int,input().split())
a = list(map(int,input().split()))

for i in range(K):
    a=[a[-1]]+a[:-1]

print(*a)