#%%
T=list(str(input()))
U=list(str(input()))

question_pos=[]
for i in range(len(T)):
    if T[i]=="?":
        question_pos.append(i)

alphabet = list("abcdefghijklmnopqrstuvwxyz")

for i in alphabet:
    for j in alphabet:
        for k in alphabet:
            for l in alphabet:
                tmp_T=T.copy()
                tmp_T[question_pos[0]]=i
                tmp_T[question_pos[1]]=j
                tmp_T[question_pos[2]]=k
                tmp_T[question_pos[3]]=l
                for x in range(len(T)-len(U)+1):
                    if "".join(tmp_T[x:x+len(U)+1])==U:
                        print("Yes")
                        exit()
print("No")

# %%
T=list(str(input()))
U=list(str(input()))

question_pos=[]
for i in range(len(T)):
    if T[i]=="?":
        question_pos.append(i)

alphabet = list("abcdefghijklmnopqrstuvwxyz")

for i in alphabet:
    for j in alphabet:
        for k in alphabet:
            for l in alphabet:
                tmp_T=T.copy()
                tmp_T[question_pos[0]]=i
                tmp_T[question_pos[1]]=j
                tmp_T[question_pos[2]]=k
                tmp_T[question_pos[3]]=l
                if "".join(U) in "".join(tmp_T):
                    print("Yes")
                    exit()
print("No")
