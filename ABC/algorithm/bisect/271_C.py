# https://atcoder.jp/contests/abc271/tasks/abc271_c

# %%
def can_form_sequence(x, available_numbers, total_count):
    existing = len(set(range(1, x + 1)) & available_numbers)
    missing = x - existing
    remaining = total_count - existing

    return (remaining // 2) >= missing


def main():
    N = int(input())
    A = set(map(int, input().split()))

    left = 0
    right = N + 1

    while right - left > 1:
        mid = (left + right) // 2
        if can_form_sequence(mid, A, N):
            left = mid
        else:
            right = mid

    print(left)


if __name__ == "__main__":
    main()
