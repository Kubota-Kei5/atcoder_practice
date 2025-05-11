A = list(map(int, input().split()))

card_num_cnt = [0] * 14

for a in A:
    card_num_cnt[a] += 1

ans_list=[]
for i in range(1, 14):
    if card_num_cnt[i] >= 2:
        ans_list.append(i)

sorted_ans_list = sorted(ans_list)

if len(sorted_ans_list) >= 2:
    if sorted_ans_list[-1]>=3:
        print('Yes')
    else:
        print('No')
else:
    print('No')
# %%
from collections import Counter

def can_make_full_house(cards):
    freq = Counter(cards)
    three_or_more = []
    two_or_more   = []
    
    for rank, count in freq.items():
        if count >= 3:
            three_or_more.append(rank)
        if count >= 2:
            two_or_more.append(rank)
    
    for rankA in three_or_more:
        for rankB in two_or_more:
            if rankA != rankB:
                return True
    
    return False

cards = list(map(int, input().split()))
if can_make_full_house(cards):
    print('Yes')
else:
    print('No')

# %%
