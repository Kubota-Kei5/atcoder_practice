N, D = map(int, input().split(" "))
S = str(input())

print(N-(S.count('@')-D))