# ------------------------------------------------
# Exercise : Exceptions
# -------------------------------------------------

# 1) Write a program that creates a dictionary like this 
# {
#     1: "red" , 2: "Blue" , 3: "Orange"
# }
# Now take the key as input from the user and print its corresponding colour 
# (Exception handle the code to terminate gracefully by printing 
# Colour not found if the key doesnot exists )

d={}
x=int(input("Enter the number of elements to create a dictionary:: "))
for i in range(x):
    key=int(input("Enter the key  :: "))
    value=input("Enter the value :: ")
    d[key]=value
try:
    print(d[int(input("Enter the key whose values need to be found:: "))])
except KeyError:
    print("Color not found")