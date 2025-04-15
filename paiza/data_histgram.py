# S問題

# %%
S=list(map(str, input().split()))

alpha=list("abcdefghijklmnopqrstuvwxyz")
alpha_dict = dict()
for i in range(len(alpha)):
    alpha_dict[alpha[i]] = 0

print(alpha_dict)


intnum=''
int_lsit=[str(i) for i in range(10)]


def main():
    isJoined = False
    for i in S:
        if i in alpha_dict and isJoined == False:
            alpha_dict[i] += 1
        elif i in int_lsit:
            intnum += str(i)
            isJoined = True
        elif i =='(': 
            main()
        elif i == ')':

            isJoined = False
    return alpha_dict


for key, value in alpha_dict.items():
    if value != 0:
        print(key + " " + str(value))    


if __name__ == "__main__":
    main()
# %%
from collections import defaultdict

s = input()
n = len(s)

def parse(i):
    alpha_dict = defaultdict(int)
    num = 0

    while i < n:
        char = s[i]

        if char.isdigit():
            num = num * 10 + int(char)
            i = i + 1

        elif char == '(':
            i = i + 1
            sub_dict, i = parse(i)
            multiplier = num if num != 0 else 1
            for key in sub_dict:
                alpha_dict[key] += sub_dict[key] * multiplier
            num = 0 

        elif char == ')':
            i = i + 1
            return alpha_dict, i

        elif char.isalpha():
            multiplier = num if num != 0 else 1
            alpha_dict[char] += multiplier
            num = 0
            i = i + 1

    return alpha_dict, i


result_dict, _ = parse(0)


alphabet = []
for i in range(ord('a'), ord('z') + 1):
    alphabet.append(chr(i))

for ch in alphabet:
    if ch in result_dict:
        print(ch, result_dict[ch])
    else:
        print(ch, 0)

# %%
