n=int(input("Enter a number :"))
t=0
for i in range(1,n+1):
    if n%i==0:
      t=t+1
if t==2:
    print(f"{n} is a prime number")
elif n==1:
    print(f"{n} is neither a prime number nor a composite number")
else:
    print(f"{n} is not a prime number")