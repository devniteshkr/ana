# -------------------------
# Exercises 
# -------------------------

# Loops and Conditionals 
# ----------------------
# # Solve the following using either while/do while loops
# 2) Take a number from the user and print all Odd numbers from 1 to that number  eg : 10 o/p 1 3 5 7 

num=int(input("Enter a number"))
for x in range(num+1):
    if (x%2!=0):
     print(x)

