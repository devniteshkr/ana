#Creating empty list. (To be appended later)
lst1=[]
lst2=[]

#Adding list elementwise and printing the result
def addlist(lst1,lst2):
    lst3=[]
    for i in range(5):
        a=lst1[i]+lst2[i]
        lst3.append(a)
    print("Added list is, ",lst3)

#Subtracting list elementwise and printing the result    
def subtractlist(lis1,list2):
    lst3=[]
    for i in range(5):
        a=lst1[i]-lst2[i]
        lst3.append(a)
    print("Subtracted list is , " ,lst3)
    
#Removes the dupplicate elements abd store it in new list
def removeduplicate(lst1,lst2):
    lst3=[]
    for i in range(5):
        a=lst1.pop()
        print(a)
        b=len(lst3)
        for i in range(b):
            if a!=lst3[i]:
                lst3.append(a)
    for i in range(5):
        a=lst2.pop()
        for i in range(len(lst3)):
            if a!=lst3[i]:
                lst3.append(a)
    print(lst3)
    
#Exception Handling
try:
    for i in range(5):
        a=int(input(f"Dear user, Please enter no: {i+1} elements of list 1 : "))
        lst1.append(a)
    
    for i in range(5):
        a=int(input(f"Dear user, Please enter no: {i+1} elements of list 2 : "))
        lst2.append(a)

except Exception as e:
    print("Error occured, ",e)
    choice=4
choice=0
#while loop for taking inpput from user and performing desired operstions
while choice!=4:
    choice=int(input("""
                     1. add elemets of two list
                     2. substract elements of two list
                     3. remove the duplicate elements from two lists
                     4. quit
                     choice : """))
    match choice:
        case 1:
            addlist(lst1,lst2)
        case 2:
            subtractlist(lst1,lst2)
        case 3:
            removeduplicate(lst1,lst2)
        case 4:
            print("You have quit")
        case _:
            print("Invalid choice")