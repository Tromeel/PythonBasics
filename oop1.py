class Dog:
    def __init__(self,name,breed,age,colour):
        self.name= name
        self.breed= breed
        self.age= age
        self.colour= colour

    def sound(self):
        print(self.name, "is barking")

dog1 =Dog("Vic","German Shepherd",5,"White")
print(dog1.name,dog1.breed,dog1.age,dog1.colour)
dog1.sound()
print()

dog2 =Dog("Spike","Siberian Husky",2,"Grey")
print(dog2.name,dog2.breed,dog2.age,dog2.colour)
dog2.sound()
print()

dog3 =Dog("Russ","Chihuahua",4,"Brown")
print(dog3.name,dog3.breed,dog3.age,dog3.colour)
dog3.sound()


