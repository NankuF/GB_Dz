profit = int(input('Введите вашу выручку: '))
costs = int(input('Введите ваши издержки: '))
if profit > costs:
    print('Прибыльный месяц')
    ror = (profit / costs) * 100
    print(f'Рентабельность = {ror:.0f}%')
    worker = int(input('Сколько у вас сотрудников? '))
    profit_1_worker = profit / worker
    print(f'Прибыль фирмы в расчете на одного сотрудника = {profit_1_worker:.2f} рублей')
else:
    print('Ваша фирма понесла убыток!')
