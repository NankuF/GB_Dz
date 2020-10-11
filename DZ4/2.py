lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

gen_list = [el for index, el in enumerate(lst) if lst[index] > lst[index - 1]]

print(gen_list)
