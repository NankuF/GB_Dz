with open('file2.txt', 'r', encoding='utf-8') as file:
    text = file.readlines()


print(f' Кол-во строк: {len(text)}')

string1= ((len(text[0].split())))
string2 =((len(text[1].split())))
string3 =((len(text[2].split())))

print(f' Кол-во слов в строке 1: {string1}')
print(f' Кол-во слов в строке 2: {string2}')
print(f' Кол-во слов в строке 3: {string3}')