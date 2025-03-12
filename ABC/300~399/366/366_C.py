# %%
Q = int(input())
ball_count = {}  # ボールの個数を管理する辞書

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        ball_count[query[1]] = ball_count.get(query[1], 0) + 1
    elif query[0] == 2:
        ball_count[query[1]] -= 1
        if ball_count[query[1]] == 0:
            del ball_count[query[1]]
    else:
        print(len(ball_count))