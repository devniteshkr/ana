n=int(input("Enter no of student"))
d={}
for x in range(n):
    name=input("Enter name of student: ")
    marks=input("Enter marks obtained: ")
    d[name]=marks
while True:
    name=input("Enter student name to get marks: ")
    marks=d.get(name,-1)
    if marks == -1:
        print("Student not found")
    else:
        print("{} g0t {} marks: ".format(name,marks))
    option=input("Do you want to find other students marks: ")
    if option=="No"or"no"or"NO":
        break
print("Thanks for using application")
