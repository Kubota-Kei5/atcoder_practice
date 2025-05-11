# %%
H, W=map(int,input().split())
Si, Sj=map(int,input().split())
G=[list(str(input())) for _ in range(H)]
X=str(input())

#Exchange element_num
now_i=Si-1 
now_j=Sj-1

for x in X:
    if x=='L':
        if now_j-1>=0 and G[now_i][now_j-1]=='.':
            now_j-=1
    elif x=='R':
        if now_j+1!=W and G[now_i][now_j+1]=='.':
            now_j+=1
    elif x=='U':
        if now_i-1>=0 and G[now_i-1][now_j]=='.':
            now_i-=1
    elif x=='D':
        if now_i+1!=H and G[now_i+1][now_j]=='.':
            now_i+=1

print(f'{now_i+1} {now_j+1}')