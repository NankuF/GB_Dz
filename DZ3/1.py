# Вариант 1
def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print('Division by zero')


user_num1 = int(input('Input number: '))
user_num2 = int(input('Input number: '))

print(round(division(user_num1, user_num2)))
