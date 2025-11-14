class Area:
    def display(self,a=None,b=None):
        if a is not None and b is not None:
            print(f"Area of a Rectangle is {a*b}")
        elif a is not None and b is None:
           print(f"Area of a Square is {a*a}") 
        else:
            print("No fields is fill")

ob=Area()
ob.display(2,6)
ob.display(3)
ob.display()
