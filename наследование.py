class Car():
    # клас по созданию автомобиля

    def __init__(self, make, models, year):
        self.make = make
        self.models = models
        self.year = year
        self.gate = 33

    def description_name(self):
        desc = str(self.year) + " " + self.make + " " + self.models
        return desc.title()

    def faf(self):
        print('Пробег этого авто ' + str(self.gate) + " km!")

    def update(self, mm):
        self.gate = mm


class Battery():
    def __init__(self, baerr=100):
        self.baerr = baerr

    def howmuchbattery(self):
        print("Энергоемкость баттареи будет " + str(self.baerr) + " klv")


class Electrocar(Car):

    def __init__(self, make, models, year):
        super().__init__(make, models, year)
        self.baerr = Battery()

    def description_name(self):
        desc = str(self.year) + " " + self.make
        return desc.title()


tesla = Electrocar("Tesla", "s", 2017)
tesla.baerr.howmuchbattery()


