t=0
print("print prime numbers between 1 to 100")
print("1 is neither prime nor prime number")
for i in range(1,101):
    for j in range(1,i+1):
        if i%j==0:
            t=t+1
    if t==2:
        print(i,end=" ")
    t=0