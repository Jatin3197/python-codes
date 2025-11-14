class Parent1:
    def show(self):
        print("This is a parent1")

class Parent2(Parent1):
    def display(self):
        print("This is a Parent2")

class Parent3(Parent2):
    def print(self):
        print("This is a Parent3")

ob=Parent3()
ob.show()
ob.display()
ob.print()