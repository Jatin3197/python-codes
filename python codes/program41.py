class Parent1:
    def show(self):
        print("This is a parent1")

class Parent2:
    def print(self):
        print("This is a parent2")

class Child(Parent1,Parent2):
    def display(self):
        print("This is a child")

ob=Child()
ob.show()
ob.print()
ob.display()