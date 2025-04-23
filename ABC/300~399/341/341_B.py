# %%
N=int(input())

A=list(map(int, input().split()))

change_rate= []
for _ in range(1,N):
    s,t=map(int,input().split())
    change_rate.append((s,t))

get_money=0

for i in range(0,N-1):
    get_money=(A[i]//change_rate[i][0])*change_rate[i][1]
    A[i+1]+= get_money

print(A[-1])