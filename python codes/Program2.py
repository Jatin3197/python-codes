#Fabonacci Series
n=int(input("Enter a number :"))
a=0
b=1
for i in range(1,n-1):
  fab=a+b
  print(f"Fabonacci of a given number is {fab}")
  a=b
  b=fab