# %%
X = int(input())
ans=[]
A=X//2
if X%2==0:
    add_str='-'*(A-1)
    ans.append(add_str)
    ans.append('==')
    ans.append(add_str)
else:
    add_str='-'*(A)
    ans.append(add_str)
    ans.append('=')
    ans.append(add_str)

print(''.join(ans))
# %%
