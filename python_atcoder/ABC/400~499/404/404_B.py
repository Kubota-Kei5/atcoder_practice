# %%
import numpy as np

def main():
    N = int(input())
    S = [list(input().rstrip()) for _ in range(N)]
    T = [list(input().rstrip()) for _ in range(N)]

    S_arr = np.array(S)
    T_arr = np.array(T)

    ans = float('inf')
    for k in range(4):
        rotated = np.rot90(S_arr, -k)
        diff = int((rotated != T_arr).sum())
        ans = min(ans, k + diff)

    print(ans)

if __name__ == "__main__":
    main()