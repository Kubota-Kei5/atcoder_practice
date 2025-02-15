num_list = list(map(int, input().split()))

cnts = [0]*5

for i in num_list:
    cnts[i]+=1

ans = 0
for cnt in cnts:
    ans += cnt//2

print(ans)