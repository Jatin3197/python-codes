#Armstrong Number
n=int(input("Enter a number :"))
t=n
s=0
while n>0:
  rem=n%10
  s=s+rem**3
  n=n//10
  
if t==s:
  print(f"{s} is a Armstrong number")
else:
  print(f"{s} is not a Armstrong number")