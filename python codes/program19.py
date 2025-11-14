marks=[]
total=0
for i in range(0,5):
    list=float(input())
    marks.append(list)
    total=total+marks[i]
per=(total/500)*100
print(f"Total Marks of a student :{total}")
print(f"Total Percentage of a student :{per}")