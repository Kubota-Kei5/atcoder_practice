X=int(input())
cnt=0
for i in range(1,10):
    for j in range(1,10):
        if i*j==X:
            pass
        else:
            cnt+=i*j

print(cnt)