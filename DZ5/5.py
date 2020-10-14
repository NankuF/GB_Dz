with open('file5.txt', 'w+', encoding='utf-8') as f:
    print(input('input numbers: '), file=f)

with open('file5.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()  # таким образом данные стали списком

c = int(text[0][0]) + int(text[0][2]) + int(text[0][4])
print(c)
