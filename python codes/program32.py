class Area:
    pi = 3.14
    
    def __init__(self, radius=0, side=0):  # default values so both won't be required always
        self.radius = radius
        self.side = side

    def Circle(self):
        return self.pi * self.radius**2
    
    def Square(self):
        return self.side**2


# Input
n = int(input("Enter a Radius: "))
a = int(input("Enter a Side: "))

# Create objects
p1 = Area(radius=n)   # radius given
area_circle = p1.Circle()
print("Area of a Circle:", area_circle)

p2 = Area(side=a)     # side given
area_square = p2.Square()
print("Area of a Square:", area_square)
