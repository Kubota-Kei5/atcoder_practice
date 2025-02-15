# %%
N=input()
A=list(map(int,input().split()))
sorted_list=sorted(A,reverse=True)

for i in range(len(A)):
    if A[i]==sorted_list[1]:
        print(i+1)
        exit()
# %%
