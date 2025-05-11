n,m=map(int, input().split())
a=list(map(int, input().split()))

l=[]
for i in range(1,n+1):
    l.append(i)

x=set(l)-set(a)

print(len(x))
print(*x)