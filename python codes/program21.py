#convert list to tuple
t=()
print("Ten Numbers are")
for i in range(0,10):
    li=list(t)
    lis=int(input())
    li.append(lis)
    li.sort()
    t=tuple(li)
print(f"sorted elements={t}")
