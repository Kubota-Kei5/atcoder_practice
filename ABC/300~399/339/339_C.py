# %%
N=int(input())
A=list(map(int,input().split()))

stop_index=0
stop_value=0
for i in range(len(A)):
    if A[i]<0:
        stop_index=i
        stop_value=A[i]
        break

if stop_index==0:
    print(abs(stop_value))
elif sum(A[0:stop_index+1])>=0:
    print(0)
else:
    print(abs(sum(A[0:stop_index+1])))