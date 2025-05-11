# %%
import itertools

dict = {}
a = list(map(int,input().split()))
name = ['A','B','C','D','E']

for i in range(len(name)):
    dict[name[i]] = a[i]

multipoint_list = []
name_list = []

for i in range(5):
    tmp_list = list(itertools.combinations(name,i+1))
    for j in tmp_list:
        multipoint=1
        name_list.append(''.join(list(j)))
        for k in j:
           multipoint += dict[k]
        multipoint_list.append(multipoint)
        

ans_dict = {}

for i in range(len(name_list)):
    ans_dict[name_list[i]] = multipoint_list[i]

ans_dict = sorted(ans_dict.items(), key=lambda x: x[1], reverse=True)

for i in range(31):
    print(ans_dict[i][0])
# %%
import itertools
import pandas as pd

dict = {}
a = list(map(int,input().split()))
name = ['A','B','C','D','E']

for i in range(len(name)):
    dict[name[i]] = a[i]

multipoint_list = []
name_list = []
len_name_list = []
multipoint=1

for i in range(5):
    tmp_list = list(itertools.combinations(name,i+1))
    for j in tmp_list:
        name_list.append(''.join(list(j)))
        len_name_list.append(len(j))
        for k in j:
           multipoint += dict[k]
        multipoint_list.append(multipoint)
        multipoint=1

df = pd.DataFrame({'name': name_list, 'len': len_name_list, 'multipoint': multipoint_list})
df_sorted = df.sort_values(['multipoint','len','name'], ascending=[False,True,True])

for i in range(31):
    print(df_sorted.iloc[i]['name'])
    # print(f'{df_sorted.iloc[i]["name"]} {df_sorted.iloc[i]["multipoint"]}')

# print(df_sorted)
# print(multipoint_list)
# print(name_list)
# print(len_name_list)

# %%
# これでAC
import itertools

points_map = {}
scores = list(map(int, input().split()))
names = ['A', 'B', 'C', 'D', 'E']

for i in range(len(names)):
    points_map[names[i]] = scores[i]

ans_dict = {}

for i in range(1, 6):
    for combo in itertools.combinations(names, i):
        subset_name = ''.join(combo)
        total_score = sum(points_map[ch] for ch in combo)
        ans_dict[subset_name] = total_score

sorted_ans = sorted(ans_dict.items(), key=lambda x: (-x[1], x[0]))

for i in range(31):
    print(sorted_ans[i][0])