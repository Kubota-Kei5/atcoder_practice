# %%
N=int(input())
A=int(input())
T=list(map(int,input().split()))

pre=0

for i in range(N):
    ans=max(pre,T[i])+A
    print(ans)
    pre=ans


