# %%
def check_brackets(s):
    stack = []
    pairs = {'(': ')', '<': '>', '[': ']'}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        elif stack and pairs.get(stack[-1]) == char:
            stack.pop()
        else:
            return "No"

    return "Yes" if not stack else "No"  # スタックが空ならYes、残ってたらNo

N = input()
print(check_brackets(N))