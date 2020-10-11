# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while
# и арифметические операции.
user_number = int(input('Введите число: '))
remainder = user_number % 10
user_number //= 10
while user_number > 0:
    if user_number % 10 > remainder:
        remainder = user_number % 10
    user_number //= 10
print(remainder)


# Исходный вид решения
# a = int(input())
# m = a%10
# a = a//10
# while a > 0:
#     if a%10 > m:
#         m = a%10
#     a = a//10
# print(m)

# Решение с комментариями и принтами
# user_number = int(input('Введите число: '))  # берем число 9876
# remainder = user_number % 10  #  число после запятой, т.е 6
# user_number = user_number // 10  # целое число, т.е 987
# print(user_number, remainder)
# while user_number > 0:  # 987>0
#     if user_number % 10 > remainder:  # 987 / 10 = 98.7; 7 > 4
#         print(user_number, remainder)
#         remainder = user_number % 10  # 987/10 = 98.7 , 7 записывается в remainder
#         print(user_number, remainder)
#     user_number = user_number // 10  # 987/10 =98.7, 98 записывается в user number
#     print(user_number, remainder)
# print(remainder)
