first_day = int(input('Ваш результат в первый день, в километрах: '))  # допустим 2 км
target = int(input('Ваша цель, в километрах: '))  # допустим 3 км
day_count = 1
progress = first_day * 0.1  # 2 * 10% = 0.2 км - ежедневный прогресс
progress_count = first_day  # к какому значению прибавляем наш прогресс
while progress_count < target:
    day_count += 1
    progress_count += progress
#    print(f'{day_count=}, {progress_count=:.2f}')  # проверка выполнения
else:
    print(f'рез-т достигнут за {day_count} дней')
