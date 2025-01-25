n,q=map(int,input().split())

h_li=[]
t_li=[]
for i in range(q):
    h,t=map(str,input().split())
    h_li.append(h)
    t_li.append(int(t))
l=1
r=2
cnt=0
for i in range(q):
    if h_li[i]=='L':
      if t_li[i]<r<l:
        cnt+=n-l+t_li[i]
        l=t_li[i]
      elif l<r<t_li[i]:
        cnt+=n-t_li[i]+l
        l=t_li[i]
      else:
        cnt+=abs(l-t_li[i])
        l=t_li[i]
    else:
      if t_li[i]<l<r:
        cnt+=n-r+t_li[i]
        r=t_li[i]
      elif r<l<t_li[i]:
        cnt+=n-t_li[i]+r
        r=t_li[i]
      else:
        cnt+=abs(r-t_li[i])
        r=t_li[i]

print(cnt)
      
# %%
