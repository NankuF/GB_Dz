# Сообщение: День Великой Коммунистической Революции настал! Cинхрофазатрон работает НЕПРЕРЫВНО!!!
user_text = input('Ваше сообщение: ')
my_list = user_text.split()

for el in my_list:
    if len(el) > 10:
        index = my_list.index(el)
        el = el[:10]
        my_list.insert(index, el)
        my_list.pop(index + 1)

for ind, el in enumerate(my_list, start=1):
    print(ind, el)
