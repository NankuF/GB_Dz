class Car:
    name = 'any'
    speed = int(input('Speed: '))
    color = 'any'
    is_police = bool

    def go(self):
        print('Car go')

    def stop(self):
        print('Car stop')

    def turn(self, direction):
        print(f'Car turn {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля: {self.speed} км/ч')
        print('------------')


class TownCar(Car):
    def show_speed(self):
        print(f'Towncar speed: {self.speed} км/ч') if self.speed <= 60 else print('Towncar speed: Превышение скорости!')
        print('------------')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Workcar speed: {self.speed} км/ч') if self.speed <= 40 else print('Workcar speed: Превышение скорости!')
        print('------------')


class PoliceCar(Car):
    pass


test = Car()
test.go()
test.stop()
test.turn('left')
test.show_speed()

test_sportcar = SportCar()
test_sportcar.show_speed()

test_town_car = TownCar()
test_town_car.show_speed()

test_work_car = WorkCar()
test_work_car.show_speed()

test_policecar = PoliceCar()
test_policecar.go()
test_policecar.stop()
test_policecar.turn('right')
test_policecar.show_speed()
