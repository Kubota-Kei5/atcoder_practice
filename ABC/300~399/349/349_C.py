# %%
S=str(input())
T=str(input())

upper_S=S.upper()
upper_T=T.upper()

Sl=list(upper_S)
Tl=list(upper_T)

S_cnt=0
T_cnt=0

for i in range(len(Sl)):
    if T[2]=='X':
        if Sl[i]==Tl[T_cnt]:
            T_cnt+=1
            if T_cnt==2:
                print("Yes")
                exit()
    else:
        if Sl[i]==Tl[T_cnt]:
            T_cnt+=1
            if T_cnt==3:
                print("Yes")
                exit()

print("No")
