class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def show(self):
        print(f"Name is {self.name} and Age is {self.age}")

n=input("Enter a name:")
a=int(input("Enter a Age:"))
p1=person(n,a)
p1.show()
        