class Cat():
    def __init__(self, name, weith, age, color):
        self.name = name
        self.weith = weith
        self.age = age
        self.color = color

    def voice(self):
        print(self.name + " подает голос,")

    def jump(self):
        print(self.color + "прыгает высоко на дерево")


my_cat = Cat(" Мурчик!", 7, 12, " цвета белого")




my_cat.voice()
print(my_cat.color + my_cat.name)
