# %%

N=int(input())
A=list(map(int,input().split()))
max_lr=0
for i in range(N-1):
    left=A[:i+1]
    right=A[i+1:]

    lu=set(left)
    ru=set(right)
    tmp_sum=len(lu)+len(ru)
    max_lr=max(max_lr,tmp_sum)

print(max_lr)

# %%
def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    N = int(input_data[0])
    A = list(map(int, input_data[1:]))

    prefix = [0]*N
    seen = set()
    for i in range(N):
        seen.add(A[i])
        prefix[i] = len(seen)

    suffix = [0]*N
    seen = set()
    for i in reversed(range(N)):
        seen.add(A[i])
        suffix[i] = len(seen)

    max_lr = 0
    for i in range(N-1):
        tmp_sum = prefix[i] + suffix[i+1]
        if tmp_sum > max_lr:
            max_lr = tmp_sum

    print(max_lr)

if __name__ == "__main__":
    solve()
# %%
