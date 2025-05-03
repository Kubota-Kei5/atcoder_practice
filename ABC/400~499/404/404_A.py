# %%
S=list(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)

unique_S = list(set(S))

for i in range(len(unique_S)):
    if unique_S[i] in alphabet:
        alphabet.remove(unique_S[i])

print(alphabet[0])
# %%
