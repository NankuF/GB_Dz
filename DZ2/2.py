my_list = []
print('Введите "!", чтобы прервать ввод значений')
while True:
    user_value = input('Введите значение:')
    stop = user_value
    if stop == '!':
        break
    elif user_value != '!':
        my_list.append(user_value)
print(my_list)
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
print(' '.join([i for i in my_list]))





# a = [i for i in input().split()]
# for i in range(1, len(a), 2):
#     a[i - 1], a[i] = a[i], a[i - 1]
# print(' '.join([i for i in a]))
