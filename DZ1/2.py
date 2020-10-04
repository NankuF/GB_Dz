# базовые значения
second = 1
minute = 60
hour = 3600

# пользовательские значения
user_second = int(input('Введите время в секундах: '))
user_minute = user_second / minute
user_hour = user_second / hour
print(f'{user_hour:.0f}:{user_minute:.0f}:{user_second}')  # округление до целого числа в большую сторону

#print(f'{user_hour:.2f}:{user_minute:.2f}:{user_second}')  # с округлением до 2х после точки

# Вопрос: если секунда состоит из 3х чисел ( например 557), как сделать, чтобы выводилось 2 числа?
# т.е  не 557, а 55 или 56, для формата чч:мм:сс

# Инфу не нашел: https://www.python.org/dev/peps/pep-0498/
# https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-digit
