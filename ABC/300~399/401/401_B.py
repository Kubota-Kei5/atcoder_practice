# %%
N= int(input())

cnt=0
isLogin=False

for i in range(N):
    S=str(input())

    if S=="login":
        isLogin=True
    elif S=="logout":
        isLogin=False
    elif S=="private":
        if isLogin!=True:
            cnt+=1

print(cnt)        



