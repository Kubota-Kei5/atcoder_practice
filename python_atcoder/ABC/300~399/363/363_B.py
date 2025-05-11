# %%
N, T, P=map(int,input().split())
L=list(map(int,input().split()))

def count_longhair(list,T):
    cnt=0
    for l in list:
        if l>=T:
            cnt+=1
    return cnt

day=0
if count_longhair(L,T)>=P:
    print(0)
    exit()
else:
    longhair_num=count_longhair(L,T)

while longhair_num<P:
    L=[x+1 for x in L]
    longhair_num=count_longhair(L,T)
    day+=1

print(day)