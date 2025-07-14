#Parent/Super/Base Class
class Animal:
    def speak(self):
        print("Animal is speaking")

    def eat(self):
        print("Animal is eating")

#Child/Sub/Derived
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

    def fetch(self):
        print("Dog is fetching a ball")

a =Animal()
a.speak()



d = Dog()
