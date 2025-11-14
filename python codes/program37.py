class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def eat(self):
        super().eat()
        print("Dog is Eating")

d=Dog()
d.eat()