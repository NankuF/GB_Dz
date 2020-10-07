def my_func(n1, n2, n3):
    a = [n1, n2, n3]
    a.sort()
    a.pop(0)
    b = sum(a)
    return b


print(my_func(10, 17, 24))
