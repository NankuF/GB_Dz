time = int(input('Enter time in seconds: '))
hours = time // 3600
minutes = hours1 = (time % 3600)//60
seconds = minutes1 = time % 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')

# # базовые значения
# second = 1
# minute = 60
# hour = 3600
#
# # пользовательские значения
# user_second = int(input('Введите время в секундах: '))
# user_minute = user_second / minute
# user_hour = user_second / hour
# print(f'{user_hour:.0f}:{user_minute:.0f}:{user_second}')  # округление до целого числа в большую сторону

#print(f'{user_hour:.2f}:{user_minute:.2f}:{user_second}')  # с округлением до 2х после точки
#
# # Вопрос: если секунда состоит из 3х чисел ( например 557), как сделать, чтобы выводилось 2 числа?
# # т.е  не 557, а 55 или 56, для формата чч:мм:сс
#
# # Инфу не нашел: https://www.python.org/dev/peps/pep-0498/
# # https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-digit

#
# #Task 2
# #Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# # и выведите в формате чч:мм:сс. Используйте форматирование строк.
# time = int(input('Enter time in seconds: '))
# hours = time // 3600
# minutes = (time // 60) - (hours * 60)
# seconds = time % 60
# print(f'{hours:02}:{minutes:02}:{seconds:02}')

# second = int(input('Введите количество секунд '))
#
# hours = (second // 3600) % 24
# minutes = (second // 60) % 60
# second2 = second % 60  # остаток от минуты т.е сколько секунд не влезло в минуту
# print(f'{hours:02}:{minutes:02}:{second2:02}')

