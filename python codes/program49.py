class Person:
    def __init__(self,name,age):
        self.name=name
        self._address="Unknown"
        self.__salary=5000

    def show_salary(self):
        return self.__salary
    
    def set_salary(self,new_salary):
        if new_salary>0:
            self.__salary=new_salary
        else:
            print("Invalid salary")

p1=Person("jatin",24)
print(p1.name)
print(p1.show_salary())
p1.set_salary(7000)
print(p1.show_salary())

        
    