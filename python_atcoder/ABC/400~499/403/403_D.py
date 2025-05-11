# %%
N, D = map(int, input().split())
A=list(map(int, input().split()))

unique_A = list(set(A))
unique_A.sort()

diff = []

rm_int=[]
for i in range(len(unique_A)-1):
    diff=abs(unique_A[i+1] - unique_A[i])
    if diff ==D:
        rm_int.append(unique_A[i])

ans=0
for i in range(len(rm_int)):
    ans+=A.count(rm_int[i])
    
print(ans)