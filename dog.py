class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def voice(self):
        print(self.name + " собака подает голос")

    def jump(self):
        print(self.name + " собака прігает")


my_dog = Dog("Лорд", 15)
my_dog_2 = Dog("fds", 11)

print(my_dog.age)
print(my_dog.name)

my_dog.voice()
my_dog.jump()
