# %%
import pandas as pd

N=int(input())
S=list(map(int, input().split()))

S.sort()

rank=1
ans=[]
cnt=0
for i in range(N):
    if S[i] == S[i-1]:
        cnt+=1
    else:
        ans.append(cnt)
        
# %%
import pandas as pd

N = int(input())
S = list(map(int, input().split()))

df = pd.DataFrame(S)
df.columns = ['S']
df['rank'] = df['S'].rank(method='min', ascending=False)
df['rank'] = df['rank'].astype(int)

rank_list = df['rank'].tolist()

for i in range(len(rank_list)):
    print(rank_list[i])


# %%
