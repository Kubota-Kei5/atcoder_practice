# %%
S=str(input())
major='0'
for i in range(3):
    if S[0]==S[1]==S[2]:
        major=S[0]
    elif S[0]==S[1] and S[1]!=S[2]:
        major=S[0]
    elif S[0]!=S[1] and S[1]==S[2]:
        major=S[1]
    elif S[0]==S[2] and S[2]!=S[1]:
        major=S[0]

for i in range(len(S)):
    if S[i]!=major:
        print(i+1)
        exit()
# %%
