with open('file4.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line, end='')
        if line.startswith('One'):
            with open('file4_1.txt', 'w+', encoding='utf-8') as file2:
                print('Один - 1', file=file2)
        elif line.startswith('Two'):
            with open('file4_1.txt', 'a+', encoding='utf-8') as file2:
                print('Два - 2', file=file2)
        elif line.startswith('Three'):
            with open('file4_1.txt', 'a+', encoding='utf-8') as file2:
                print('Три - 3', file=file2)
        elif line.startswith('Four'):
            with open('file4_1.txt', 'a+', encoding='utf-8') as file2:
                print('Четыре - 4', file=file2)