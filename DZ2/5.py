my_list = []
print('Для выхода введите 0 или отрицательное число')
while True:
    try:
        user_number = int(input('Введите позицию рейтинга: '))
    except ValueError:  # Ошибка возникнет если нажать Enter или '-' во время ввода позиции рейтинга
        print('Ошибка ввода!')
    else:
        stop = user_number
        if stop <= 0:
            break
        elif user_number > 0:
            my_list.append(user_number)
            my_list.sort(reverse=True)
            print(my_list)

print('Ваша таблица рейтинга:', my_list)