S=str(input())
a = S.count('00')
other=len(S)-(2*a)

if a==0:
    print(len(S))
else:
    print(a+other)