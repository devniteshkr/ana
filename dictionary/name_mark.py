d={}
n=int(input("Enter no of student: "))
i=1
while i<=n:
    name=input("Enter name of student: ")
    marks=input("Enter the marks obtained: ")
    d[name]=marks
    i=i+1
print("Name of Student","\t\t"," % of marks" )
for x in d:
    print("\t",name,"\t\t",marks,"%")
