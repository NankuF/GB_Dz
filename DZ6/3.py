class Worker:
    name = input('Name: ')
    surname = input('Surname: ')
    position = input('Position: ')
    _income = {"wage": 5000, "bonus": 2000}


class Position(Worker):
    def get_full_name(self):
        # Работает как с Worker.name, так и с self.name
        self.fullname = print(f'ФИО работника: {Worker.name} {Worker.surname}\nДолжность: {self.position}')

    def get_total_income(self):
        self.d_values = Worker._income.values()
        self.total_income = print(f'Доход с учетом премии: {sum(self.d_values)}р')
        # or return self.b


test = Position()
test.get_full_name()
test.get_total_income()
# or print(test.get_total_income())
