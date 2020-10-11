from itertools import count, cycle

# 6.1
# try:
#     for el in count(int(input('Введите значение от -х до 9: '))):
#         if el > 10:
#             break
#         else:
#             print(el)
# except ValueError:
#     print('Введите только целые числа!')

# 6.2
lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
c = 0
for el in cycle(lst):
    if c > 20:
        break
    else:
        print(el)
    c +=1
