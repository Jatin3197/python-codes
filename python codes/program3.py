#Sum of a digit
n=int(input("Enter a number :"))
s=0
while n>0:
 rem=n%10
 n=n//10
 s=s+rem
print(f"Sum of a given number is {s}")
 