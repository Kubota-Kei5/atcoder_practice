# %%
S1,S2=map(str,input().split())

if S1=='sick' and S2=='sick':
    print(1)
elif S1=='fine' and S2=='fine':
    print(4)
elif S1=='sick' and S2=='fine':
    print(2)
elif S1=='fine' and S2=='sick':
    print(3)