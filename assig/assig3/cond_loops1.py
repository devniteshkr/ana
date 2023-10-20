# -------------------------
# Exercises 
# -------------------------

# Loops and Conditionals 
# ----------------------
# # Solve the following using either while/do while loops
# 1) Take a number from the user and print sum from 1 to that number for eg: 10 o/p : 55
# 2) Take a number from the user and print all Odd numbers from 1 to that number  eg : 10 o/p 1 3 5 7 9
# 3) Take a number from the user and print all Even numbers from 1 to that number eg : 10 2 4 6 8 10


n=int(input("Enter a number:"))
sum=0
i=1
while (i<=n):
    sum=sum+i
    i=i+1
print("Sum: ",sum)
    
    
    