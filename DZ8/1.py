import random


# # --------------------------
# #     9 43 62          74 90
# #  2    27    75 78    82
# #    41 56 63     76      86
# # --------------------------

class Line:

    def __init__(self):
        self.lst = []
        self.newlist = []
        while len(self.lst) < 20:
            self.lst.append(random.randrange(1, 30))
            self.newlist = [el for el in self.lst if self.lst.count(el) < 2]
        self.newlist = sorted(random.sample(self.newlist, 5))

            

    def __str__(self):
        return ' '.join([str(el) for el in self.newlist])


class Line2(Line):
    def __init__(self):
        super().__init__()  # не срабатывает супер и переопределение метода,приходится дублировать код
        self.lst = []
        self.newlist = []
        while len(self.lst) < 20:
            self.lst.append(random.randrange(30, 61))
            self.newlist = [el for el in self.lst if self.lst.count(el) < 2]
        self.newlist = sorted(random.sample(self.newlist, 5))


class Line3(Line):
    def __init__(self):
        super().__init__()
        self.lst = []
        self.newlist = []
        while len(self.lst) < 20:
            self.lst.append(random.randrange(61, 99))
            self.newlist = [el for el in self.lst if self.lst.count(el) < 2]
        self.newlist = sorted(random.sample(self.newlist, 5))


class Ticket():
    def ticket(self):
        return f'Билет Пользователя\n-----------------\n{line}\n{line2}\n{line3}\n----------------'


class Line_comp(Line):
    pass


class Line_comp2(Line2):
    pass


class Line_comp3(Line3):
    pass


class Ticket_comp(Ticket):
    def ticket(self):
        return f'Билет компьютера\n-----------------\n{line_comp}\n{line_comp2}\n{line_comp3}\n-----------------'


line = Line()
line2 = Line2()
line3 = Line3()
ticket = Ticket()
line_comp = Line_comp()
line_comp2 = Line_comp2()
line_comp3 = Line_comp3()
ticket_comp = Ticket_comp()
print(ticket.ticket())
print(ticket_comp.ticket())
