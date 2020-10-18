from itertools import cycle
from time import sleep


class TrafficLight:
    __color = ['red', 'yellow','green']

    def running(self):
        iter = cycle(self.__color)
        while True:
            print(next(iter))
            sleep(7)
            print(next(iter))
            sleep(2)
            print(next(iter))
            sleep(4)



test = TrafficLight()
test.running()
