# %%
K=int(input())
S=input()
T=input()
cnt=0

if len(S)==len(T): # 文字変更処理の場合
    for i in range(len(S)):
        if S[i]==T[i]:
            pass
        else:
            cnt+=1
    if cnt>1:
        print('No')
    else:
        print('Yes')
elif len(S)<len(T): # 文字削除の場合
    for i in range(len(S)):
        if S[i]==T[i]:
            pass
        else:
            T.replace(T[i],'')
    if S==T:
        print('Yes')
    elif S==T[:-1]:
        print('Yes')
    else:
        print('No')
else: # 文字挿入の場合
    for i in range(len(S)):
        if S[i]==T[i]:
            pass
        else:
            T=T[:i+1]+S[i]+T[i+1:]
    if S==T:
        print('Yes')
    else:
        print('No')
