class Car():
    # клас по созданию автомобиля

    def __init__(self, make, models, year):
        self.make = make
        self.models = models
        self.year = year
        self.gate = 0

    def description_name(self):
        desc = str(self.year) + " " + self.make + " " + self.models
        return desc.title()

    def faf(self):
        print('Пробег этого авто ' + str(self.gate) + " km!")

    def update(self, mm):
        self.gate = mm


my_car = Car("Mercedes", "benz", 1985, )


my_car.update(mm=33)
my_car.faf()
print(my_car.description_name())
