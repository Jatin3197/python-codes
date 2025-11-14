class Parent:
    string="jatin Jaiswal"
    def show(self):
        return self.string
class Child(Parent):
    def print(self):
        print(" it is from child class")

c=Child()
print(c.show())
c.print()
