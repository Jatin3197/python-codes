class SMS:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        return f"Name is {self.name} , Id is {self.id}"
    
class Student(SMS):
    def __init__(self,name,id,course):
     super().__init__(name,id)
     self.course=course
    
    def stushow(self):
       return f"Name is {self.name} ,Id id {self.id} ,Course is {self.course} "
    
s=Student("mukesh",22,"MCA")
print(s.show())
print(s.stushow())
    