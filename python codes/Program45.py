class Name:
    def dis(self,name=None,age=None):
       if name is not None and age is not None:
           print(f"Name is {name } and Age is {age}")
       elif name is not None and age is None:
           print(f"Name is {name }")
       elif name is None and age is not None:
           print(f"Age is {age }")
       else:
           print("It is not defined")

ob=Name()
ob.dis("Jatin",24)
ob.dis("jatin")
ob.dis(23)
ob.dis()