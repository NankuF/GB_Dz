from math import factorial as fact
from itertools import count


def gen():
    n = int(input('input: '))
    for el in count(n):
        yield fact(el)

x = 0
for el in gen():
    if x > 15:
        break
    else:
        x +=1
        print(el)
