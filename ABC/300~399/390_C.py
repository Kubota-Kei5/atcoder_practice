h,w=map(int,input().split())
S=[]
for i in range(h):
    S.append(list(str(input())))

x=[]
y=[]
for i in range(h):
    for j in range(w):
        if S[i][j]=='#':
            x.append(i)
            y.append(j)

top=min(x)
bottom=max(x)
left=min(y)
right=max(y)

for i in range(top, bottom + 1):
    for j in range(left, right + 1):
        if S[i][j] == '?':
            S[i][j] = '#'

for i in range(top,bottom+1):
    for j in range(left,right+1):
        if S[i][j]!='#':
            print('No')
            exit()

print('Yes')