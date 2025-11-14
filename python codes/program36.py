class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Professor(Person):
    def isProfessor(self):
        return f"Name is {self.name} Age is {self.age}"
    
p=Professor("Radha Raman",34)
print(p.isProfessor())
        
    