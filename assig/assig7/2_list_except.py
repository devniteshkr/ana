# 2) Write a program that creates a list of 5 elements of your choice
# Now take the index that the user want the data of and print the value at that
# location
# Exception handle the code to  terminate gracefully by printing
# Value not found if the index does not exists 

l=[]
x=int(input("Enter the no elements to create a list:: "))
for i in range(x):
    elements=int(input("Enter the elements of list :: "))
    l.append(elements)
print(l)

try:
    print(l[int(input("Enter the index whose values need to found:: "))])
except IndexError:
    print("value not found")