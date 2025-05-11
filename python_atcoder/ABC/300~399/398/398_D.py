N,R,C=map(int,input().split())
S=input()

sy,sx=R,C
smoke_map=set()
smoke_map.add((0,0))
ans=''
for s in S:
    if (R,C) in smoke_map:
        ans.append('1')
    else:
        ans.append('0')

    if s=='N':
        new_smoke=(-1,0)
        smoke_map.add(new_smoke)
        for i in range(len(smoke_map)):
            smoke_map[i]=(smoke_map[i][0]-1,smoke_map[i][1])
    elif s=='S':
        new_smoke=(1,0)
        smoke_map.add(new_smoke)
        for i in range(len(smoke_map)):
            smoke_map[i]=(smoke_map[i][0]+1,smoke_map[i][1])
    elif s=='E':
        new_smoke=(0,1)
        smoke_map.add(new_smoke)
        for i in range(len(smoke_map)):
            smoke_map[i]=(smoke_map[i][0],smoke_map[i][1]+1)
    elif s=='W':
        new_smoke=(0,-1)
        smoke_map.add(new_smoke)
        for i in range(len(smoke_map)):
            smoke_map[i]=(smoke_map[i][0],smoke_map[i][1]-1)

print(ans)
