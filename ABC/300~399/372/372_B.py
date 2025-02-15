# %%
M=int(input())
A=[]
i=10

while True:
    if M==0:
        break
    if 3**i>M:
        i-=1
        continue
    M-=3**i
    A.append(i)

print(len(A))
print(*A)
# %%
