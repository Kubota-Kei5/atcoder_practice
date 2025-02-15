l=[]
for i in range(8):
    l.append(str(input()))
row={i for i in range(8)}
col={i for i in range(8)}
for i in range(8):
    for j in range(8):
         if l[i][j]=='#':
            row.discard(i)
            col.discard(j)

print(len(row)*len(col))