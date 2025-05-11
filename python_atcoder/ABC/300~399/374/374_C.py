# %%
N=int(input())
K=list(map(int,input().split()))

K_sorted=sorted(K,reverse=True)

groupA=[]
groupB=[]

for i in range(1,N+1):
    if i==1:
        groupA.append(K_sorted[i-1])
    elif i==2:
        groupB.append(K_sorted[i-1])
    else:
        if sum(groupA)<=sum(groupB):
            groupA.append(K_sorted[i-1])
        else:
            groupB.append(K_sorted[i-1])

print(max(sum(groupA),sum(groupB)))

# %%

N=int(input())
K=list(map(int,input().split()))

K_sorted=sorted(K)

groupA=[]
groupB=[]

for i in range(1,N+1):
    if i==1:
        groupA.append(K_sorted[i-1])
    elif i==2:
        groupB.append(K_sorted[i-1])
    else:
        if sum(groupA)<=sum(groupB):
            if sum(groupA)+sum(K_sorted[-(N-i):])<=sum(groupB):
                groupB.append(K_sorted[i-1])
                groupA.append(K_sorted[-(N-i):])
                break
            else:
                groupA.append(K_sorted[i-1])
        else:
            groupB.append(K_sorted[i-1])

print(max(sum(groupA),sum(groupB)))

# %%

list=[1,2,3,4,5]

print(list[-2:])
# %%

N=int(input())
K=list(map(int,input().split()))

K_sorted=sorted(K,reverse=True)

groupA=[]
groupB=[]

for i in range(1,N+1):
    if i==1:
        groupA.append(K_sorted[i-1])
    elif i==2:
        groupB.append(K_sorted[i-1])
    else:
        if sum(groupA)<=sum(groupB):
            if K_sorted[i-1]>sum(K_sorted[-(N-i):]):
                groupB.append(K_sorted[i-1])
                groupA.append(K_sorted[-(N-i):])
                break
            else:
                groupA.append(K_sorted[i-1])
        else:
            groupB.append(K_sorted[i-1])

print(max(sum(groupA),sum(groupB)))