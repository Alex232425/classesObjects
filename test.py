class Kistocki():
    def __init__(self, price, dlinna, razmer):
        self.dlinna = dlinna
        self.razmer = razmer
        self.price = price


    def jump(self):
        goa = str(self.dlinna) + " " + str(self.razmer)
        return goa


class Kote(Kistocki):

    def __init__(self, price, dlinna, razmer):
        super().__init__(price, dlinna, razmer)


my = Kote(250, 1200, "ther")

print(" Дичь полная " + str(my.price) + " " + str(my.dlinna) + my.razmer)
print(my.jump())
