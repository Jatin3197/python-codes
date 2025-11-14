#Largest number among 3 Numbers
a=int(input("Enter a first number :"))
b=int(input("Enter a second number :"))
c=int(input("Enter a third number :"))

if a>b and a>c:
  print(f"{a} is greater")
elif b>a and b>c:
  print(f"{b} is greater")
else:
  print(f"{c} is greater")
