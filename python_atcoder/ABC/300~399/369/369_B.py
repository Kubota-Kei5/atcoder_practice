N=int(input())
X=[]
right=0
left=0
lstart=0
rstart=0
cnt=0
for i in range(N):
    a,s=map(str,input().split())
    X.append([int(a),s])

for i in range(N):
    if X[i][1]=='L' and lstart==0:
        lstart+=1
        left=X[i][0]
    elif X[i][1]=='R' and rstart==0:
        rstart+=1
        right=X[i][0]
    elif X[i][1]=='L':
        cnt+=abs(left-X[i][0])
        left=X[i][0]
    elif X[i][1]=='R':
        cnt+=abs(right-X[i][0])
        right=X[i][0]

print(cnt)