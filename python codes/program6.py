#Palindrome Number
n=int(input("Enter a number :"))
t=n
s=0
while n>0:
  rem=n%10
  n=n//10
  s=s*10+rem
if t==s:
  print(f"{s} is a palindrome number")
else:
  print(f"{s} is not a palindrome number")