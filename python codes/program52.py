class Employee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary

class Manager(Employee):
    def show_salary(self):
        print(f"{self.name}'s salary is {self._salary}")


m1=Manager("Rohan",80000)
m1.show_salary()



        
    