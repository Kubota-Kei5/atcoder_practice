def is_in_list(target,numbers):
    return target in numbers

n, d=map(int, input().split())
s=list(input())
position = []
for i in range(n):
    if s[i]=='@':
        position.append(i)
    else:
        pass

ate_pos = position[:-d]    

for j in range(n):
    if is_in_list(j,ate_pos):
        s[j]='@'
    else:
        s[j]='.'

print(*s, sep='')