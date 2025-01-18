# %%
X = int(input())
a=1
cnt=0
for i in range(1,X+1):
    a=a*i
    cnt+=1
    if a==X:
        print(cnt)
        break
# %%
