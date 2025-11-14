class Person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        return f"Name is {self.name} , Id is {self.id}"
    
class Student(Person):
    def study(self):
       return f"{self.name} is studing"
    
s=Student("mukesh",22)
print(s.show())
print(s.study())
    
