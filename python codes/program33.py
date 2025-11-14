class Cal:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def add(self):
        return self.x + self.y
    
    def sub(self):
        return self.x - self.y
    
    def mult(self):
        return self.x * self.y
    
    
    def div(self):
        return self.x // self.y
    
n1=int(input("Enter a first Number "))
n2=int(input("Enter a second Number "))
s1=Cal(n1,n2)  
add=s1.add()
print(f"Sum is {add}")

sub=s1.sub()
print(f"Sum is {sub}")

mult=s1.mult()
print(f"Sum is {mult}")

div=s1.div()
print(f"Sum is {div}")