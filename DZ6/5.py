class Stationery:
    title = 'Stationery'
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки Pen')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки Pencil')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки Handle')




test = Stationery()
print(test.title)
test.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()