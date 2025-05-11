input_int = list(map(int, input().split(" ")))
unique_li = list(set(input_int))

if len(unique_li) == 2:
    print("Yes")
else:
    print("No")