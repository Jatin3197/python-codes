class Shape:
    def area(self):
        print("It is from Shape class")

class Circle(Shape):
    def area(self):
        print("Area of a circle=3.14*r*r")


class Rectangle(Shape):
    def area(self):
        print("Area of a rectangle=l*b")

class Square(Shape):
    def area(self):
        print("Area of a square=s*s")

shapes=[Shape(),Circle(),Rectangle(),Square()]
for s in shapes:
   s.area()
