# %%
N, C = map(int,input().split())
T = list(map(int, input().split()))
diff = []
for i in range(N):
    diff = T[i]-T[i-1]
    diff.append()