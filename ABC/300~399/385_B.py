# %%
h, w, x, y =map(int, input().split())
s =[input() for _ in range(h)]
t = str(input())
x=x-1
y=y-1
home=[]
for i in t:
    if i=='U':
        if s[x-1][y]=='.':
            x-=1
        elif s[x-1][y]=='@':
            x-=1
            home.append((x,y))
        else:
            continue
    elif i=='D':
        if s[x+1][y]=='.':
            x+=1
        elif s[x+1][y]=='@':
            x+=1
            home.append((x,y))
        else:
            continue
    elif i=='L':
        if s[x][y-1]=='.':
            y-=1
        elif s[x][y-1]=='@':
            y-=1
            home.append((x,y))
        else:
            continue
    elif i=='R':
        if s[x][y+1]=='.':
            y+=1
        elif s[x][y+1]=='@':
            y+=1
            home.append((x,y))
        else:
            continue

print(x+1,y+1,len(set(home)))

# %%
