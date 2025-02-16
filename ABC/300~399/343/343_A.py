# %%
A,B=map(int,input().split())
C=A+B
for i in range(10):
    if i!=C:
        print(i)
        exit()