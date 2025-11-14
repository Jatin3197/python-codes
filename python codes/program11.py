#User input Calculator
a=int(input("Enter a first number :"))
b=int(input("Enter a second number :"))

print("Press1= Sum  Press2= Sub Press3= mul Press4 =div")

c=int(input())

if c==1:
 print(f"Sum of two number is {a+b}")
if c==2:
 print(f"Substraction of two number is {a-b}")
if c==3:
 print(f"Multiplication of two number is {a*b}")
if c==4:
 print(f"Division of two number is {a//b}")
