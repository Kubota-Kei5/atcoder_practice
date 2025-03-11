# %%
N=int(input())

list=[]
sumRate=0
for i in range(N):
    userName,rate=input().split()
    sumRate+=int(rate)
    list.append(userName)


# 合計値をNで割った余りを求める
mod=sumRate%N

sorted_list=sorted(list)

print(sorted_list[mod])