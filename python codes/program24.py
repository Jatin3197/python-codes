li=[]
n=int(input("Enter a number :"))
for i in range(0,n):
    list=int(input())
    li.append(list)
choice=int(input("Enter a choice: "))
if choice==1:
 avg=sum(li)/len(li)
 print(f"Average of a list is {avg}")
elif choice==2:
 sum=sum(li)
 print(f"Sum of a list is {sum}")
elif choice==3:
 max=max(li)
 print(f"Maximum of a list is {max}")
else:
 min=min(li)
 print(f"Minimum of a list is {min}")
