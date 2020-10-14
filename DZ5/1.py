with open('file1.txt', 'w+') as file1:
    c = 0
    while True:
        a = print(input('input text: '), file=file1)
        file1.seek(0)
        b = file1.readlines()
        if b[-1].startswith('stop'):
            break

# не знаю как сделать остановку по пустой строке