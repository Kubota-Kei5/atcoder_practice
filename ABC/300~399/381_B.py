# %%
s = list(input())
t=len(s)
cnt=0
if t%2==0:
    cnt+=1

for i in range(1,t//2+1):
    if s[2*i-2]==s[2*i-1]:
        cnt+=1
    else:
        break

a=[0 for _ in range(t)]
for j in range(t):
    for k in range(t):
        if s[j]==s[k]:
            a[j]+=1
for l in range(t):
    if a[l]==2:
        cnt+=1

if cnt==t/2+1+t:
    print('Yes')
else:
    print('No')

# %%
