# %
def solve(S):
    cnt = 0
    i = 0
    expected = 'i'
    
    while i < len(S):
        if S[i] == expected:
            expected = 'o' if expected == 'i' else 'i'
            i += 1
        else:
            # 期待する文字と一致しない場合は文字を挿入
            cnt += 1
            expected = 'o' if expected == 'i' else 'i'
    
    # 最後がiで終わる必要がある場合は追加
    if expected == 'i':
        cnt += 1
        
    return cnt

S = input()
print(solve(S))

# %%

S=input()
cnt=0
for i in range(len(S)-1):
    if S[i]=='i' and S[i+1]=='o':
        pass
    elif S[i]=='o' and S[i+1]=='i':
        pass
    else:
        cnt+=1

if S[-1]=='i':
    cnt+=1

print(cnt)
# %%
def min_insertions_to_io(S: str) -> int:
    inserts = 0
    expected_char = 'i'
    final_length = 0

    for c in S:
        if c != expected_char:
            inserts += 1
            final_length += 1
            expected_char = 'o' if expected_char == 'i' else 'i'

        final_length += 1
        expected_char = 'o' if expected_char == 'i' else 'i'

    if final_length % 2 == 1:
        inserts += 1
        final_length += 1

    return inserts

if __name__ == "__main__":
    S = input().strip()
    result = min_insertions_to_io(S)
    print(result)
