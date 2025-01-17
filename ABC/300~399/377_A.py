S = input()
li = []
for i in S:
    li.append(i)

if ''.join(sorted(li))=='ABC':
    print('Yes')
else:
    print('No')