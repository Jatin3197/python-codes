#Reverse of a digit
n=int(input("Enter a number :"))
rev=0
while n>0:
  rem=n%10
  n=n//10
  rev=rev*10+rem
print(f"Reverse of a digit is {rev}")