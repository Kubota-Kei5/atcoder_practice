# %%
input_int = list(map(int, input().split(" ")))
sorted_li = sorted(input_int)

if sorted_li[0]+sorted_li[1] == sorted_li[2]:
    print("Yes")
elif sorted_li[0]== sorted_li[1] == sorted_li[2]:
    print("Yes")
else:
    print("No")