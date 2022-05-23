class Home():
    def __init__(self, street, number):
        self.street = street
        self.number = number
        self.age = 11

    def build(self):
        print("Строительство дома на улице " + self.street + ", " + str(self.number))

    def age_of_house(self, year):
        self.age += year



class Two_tower(Home):

    def __init__(self, street, number):
     super().__init__(street, number)


    def location(self):
        goa = '- дома находяться на разных локациях по улице' + " " + self.street
        return goa



жк_Могилев = Two_tower('Накимовая', 11)

жк_Могилев.build()
print("Его возраст будет, " + str(жк_Могилев.age) + " лет")

жк_Могилев.age_of_house(5)
print(жк_Могилев.age)

print(жк_Могилев.location())


