class Student:
    def __init__(self,rollno,name,age,gender,course,marks):
        self.rollno=rollno
        self.name=name
        self.age=age
        self.gender=gender
        self.course=course
        self.marks=marks
    def show(self):
        print(f"Rollno of a student is {self.rollno}")
        print(f"Name of a student is {self.name}")
        print(f"Age of a student is {self.age}")
        print(f"Gender of a student is {self.gender}")
        print(f"Course of a student is {self.course}")
        print(f"Course of a student is {self.marks}")

a=int(input("Enter a Roll no. "))
b=input("Enter a name ")
c=int(input("Enter a age "))
d=input("Enter a Gender ")
e=input("Enter a course ")
f=int(input("Enter a marks "))

s1=Student(a,b,c,d,e,f)
s1.show()
        
    