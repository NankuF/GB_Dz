class Road:
    """
    Если хотим динамически изменять значения длины и ширины в mass_asphalt
    _length = int(input('Введите длину: '))
    _width = int(input('Введите длину: '))
   """
    # Просто передаем значения в экземпляр класса
    _length = 20
    _width = 5000

    def mass_asphalt(self, kg, depth, length=_length, width=_width):
        tons = kg / 1000
        depth = 1 * depth
        return length * width * tons * depth


test = Road()
print(f'Length {test._length}m')
print(f'Width {test._width}m')
print(f'Необходимо {test.mass_asphalt(25, 5)} тонн асфальта')
