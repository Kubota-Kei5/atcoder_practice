N, M=map(int,input().split())

S=[str(input()) for _ in range(N)]
T=[str(input()) for _ in range(M)]

def find_pattern_positions(S, T, N, M):
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            if all(S[i + di][j:j + M] == T[di] for di in range(M))
                print(f'{i+1} {j+1}')
            return 

find_pattern_positions(S,T,N,M)