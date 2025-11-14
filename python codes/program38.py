class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def bark(self):
        print("dog barks")

class Cat(Animal):
    def mew(self):
        print("cat mew")

d=Dog()
d.sound()
d.bark()

c=Cat()
c.sound()
c.mew()