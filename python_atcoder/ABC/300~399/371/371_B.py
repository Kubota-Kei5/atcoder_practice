# %%
n,m = map(int, input().split())
A=[]
B=[]

for i in range(m):
    a,b=map(str,input().split())
    A.append(int(a))
    B.append(b)

# 各家の男の子の人数をカウント
l=[0]*n

for i in range(m):
    if B[i]=='M' and l[A[i]-1]==0:
        print('Yes')
        l[A[i]-1]+=1
    else:
        print('No')

# %%
