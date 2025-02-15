n, k = map(int, input().split())
s=str(input())

l=['O' for i in range(k)]
a=''.join(l)
print(s.count(a))