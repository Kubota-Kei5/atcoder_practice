# %%
s=str(input())
t=str(input())
cnt=0
n=min(len(s),len(t))
for i in range(n):
    if s[i]==t[i]:
        pass
    else:
        cnt=i
        break

if len(s)!=len(t) and cnt==0:
    print(n+1)
elif len(s)==len(t) and cnt==0:
    print(0)
else:
    print(cnt+1)
# %%
