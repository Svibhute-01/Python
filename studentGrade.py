student=list()
grade=list()
n=int(input("Enter number of students:"))
i=0
while i<n:
    s=input("Add student:")
    student.append(s)
    g=int(input("Enter grade"))
    grade.append(g)
    i+=1

print("Student:",student)
print("Grade:",grade)
sum=0
for i in grade:
    sum=sum+i

average=sum/n

print("\nAvarage of grade of student is",average,"\n")
print("----------------------------------------------------")

ans=input("Do you want to update grade of any student?y/n")
if(ans=='y'):
 name=input("Enter name:")
 index=student.index(name)
 newGrade=int(input("Update grade:"))
 grade[index]=newGrade
 print("Students:",student)
 print("Garde:",grade)

sum=0
for i in grade:
    sum=sum+i

average=sum/n

print("Avarage of grade of student is",average)