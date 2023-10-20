# Exercise : Questions based on functions , loops, conditionals
# ------------------
# # ***********************************************************
# # Problem 2
# # ***********************************************************

# Addition/Squaring/exponenation should be done as part of single function named 
# "my_calculator"
# which takes in type of operation, number1,number2 as input 
# and outputs the answer based on the operation


def my_calculator():
    print("**********  Menu   ********")
    print("1.Addition")
    print("2.Squaring")
    print("3.Exponention")
    
    ch=int(input("Enter your choice: "))
    
    if(ch==1):
        num1,num2=[int(x) for x in input("Enter two numbers :: ").split()]
        sum=num1+num2
        print("Sum:",sum)
        
    elif(ch==2):
        num1=int(input("Enter the number :: "))
        square=num1*num1
        print("Square of",num1,"is :: ",square)
        
    elif(ch==3):
        num1,pow1=[int(x) for x in input("Enter number and power_value to find the exponent :: ").split()]
        exponent=num1**pow1
        print("Exponential value of given ",num1,"is :: ",exponent)
my_calculator()