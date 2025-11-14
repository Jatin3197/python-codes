class Calculator:
    def add(self,a=None,b=None):
        if a is not None and b is not None:
            return a+b
        elif a is not None:
            return a 
        else:
            print("No fields is fill")

ob=Calculator()
print(ob.add(21,45))
print(ob.add(23))
ob.add()
