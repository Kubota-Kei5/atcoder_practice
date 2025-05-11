# %%

def min_substring_with_duplicate(N,A):
    last_index = {}
    min_len = N+1

    for i, val in enumerate(A):
        if val in last_index:
            j = last_index[val]
            length = i - j + 1
            min_len = min(min_len, length)
        last_index[val] = i

    if min_len == N+1:
        print(-1)
    else:
        print(min_len)

N = int(input())
A = list(map(int, input().split()))
ans = min_substring_with_duplicate(N,A)
