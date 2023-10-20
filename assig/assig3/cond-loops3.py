# -------------------------
# Exercises 
# -------------------------

# Loops and Conditionals 
# ----------------------
# # Solve the following using either while/do while loops

# 3) Take a number from the user and print all Even numbers from 1 to that number eg : 10 2 4 6 8 10

num=int(input("Enter a number"))
for x in range(num+1):
    if (x%2==0):
        print(x)