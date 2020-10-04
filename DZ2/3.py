# Времена года через список
user_number = int(input('Введите число месяца: '))

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
while 0 < user_number < 13:
    if user_number in winter:
        print('Зима')
        break
    elif user_number in spring:
        print('Весна')
        break
    elif user_number in summer:
        print('Лето')
        break
    elif user_number in autumn:
        print('Осень')
        break
else:
    print('Такого месяца не существует')

# Времена года через словарь
seasons = {
    1: 'Зима',
    2: 'Зима',
    3: 'Весна',
    4: 'Весна',
    5: 'Весна',
    6: 'Лето',
    7: 'Лето',
    8: 'Лето',
    9: 'Осень',
    10: 'Осень',
    11: 'Осень',
    12: 'Зима',
}
user_number = int(input('Введите число месяца: '))

while 0 < user_number < 13:
    if user_number in seasons:
        print(seasons.get(user_number))
        break
else:
    print('Такого месяца не существует')
