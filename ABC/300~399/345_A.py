# %%
S=str(input())

if S[0]!='<' or S[len(S)-1]!='>':
    print('No')
else:
    for i in range(1,len(S)-1):
        if S[i]=='=':
            pass
        else:
            print('No')
            break
    print('Yes')