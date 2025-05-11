# %%
N=int(input())
A=list(map(int,input().split()))
dict={}
ans=[]    
for i in range(N):
    if A[i] not in dict:
        ans.append(-1)
        dict[A[i]]=i+1
    else:       
        ans.append(dict[A[i]])
        dict[A[i]]=i+1

print(*ans)