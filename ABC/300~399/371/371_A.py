S = list(input().split())
l = ['A','B','C']


if S[0]=='<':
    if S[1]=='<':
        if S[2]=='<':
            print('B')
        else:
            print('C')
    else:
        print('A')
else:
    if S[1]=='<':
        print('A')
    else:
        if S[2]=='<':
            print('C')
        else:
            print('B')