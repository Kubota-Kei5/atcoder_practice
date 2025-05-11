# %%
S=list(input())

appear_cnt = [0]*101
unique_chars=list(set(S))

for i in range(len(unique_chars)):
    appear = S.count(unique_chars[i])
    appear_cnt[appear] += 1
 
 
for i in range(len(appear_cnt)):
    if appear_cnt[i] != 2 and appear_cnt[i] != 0:
        print("No")
        exit()

print("Yes")


