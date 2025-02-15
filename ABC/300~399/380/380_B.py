s=list(input())

l=[]
for i in range(len(s)):
    if s[i]=='|':
        l.append(i)

a=[]
for j in range(1,len(l)):
    a.append(l[j]-l[j-1]-1)

print(*a)