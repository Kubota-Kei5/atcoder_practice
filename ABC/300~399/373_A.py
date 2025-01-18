l = [input() for _ in range(12)]
cnt = 0
for i in range(12):
    if len(l[i])==i+1:
        cnt+=1
    else:
        pass

print(cnt)