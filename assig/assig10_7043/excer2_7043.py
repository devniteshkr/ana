# -----------------------------------------------------------------------
# EXERCISE on lambda and Higher Order Functions
# -----------------------------------------------------------------------
# 1)  Convert following functions from function_definitions.py into lambda 
#     and call them 
# 2)  Create my calculator exercise in functional style 
# """            

# # Solution:
# # exercise : create my calculator exercise in functional style 
# """
# Addition/Squaring/exponenation should be done as part of single function named 
# "my_calculator"
# which takes in type of operation, number1,number2 as input 
# and outputs the answer based on the operation

def hof(func,param1,param2= None):
    if param2 is None:
        return func(param1)
    else: 
        return func(param1,param2)
    

my_addition = lambda first_number,second_number : first_number+second_number
my_square = lambda first_number, second_number = None : first_number**2
my_exponenation = lambda first_number,second_number : first_number**second_number

def my_calculator():
    print("****************** MENU ************************")
    print("1: Addition")
    print("2: Square")
    print("3: Exponentation ")
    choice = int(input ("Please select your choice"))

    if choice == 1 :
        first_num = int(input("Please enter First number:"))
        second_num = int(input("Please enter Second number:"))
        #returned_value = my_addition(first_num,second_num)
        returned_value = hof(my_addition,first_num,second_num)
        print("The Addition of the numbers is ",returned_value)

    elif choice == 2 :
        first_num = int(input("Please enter First number:"))
        #returned_value = my_square(first_num)
        returned_value = hof(my_square,first_num)
        print("The Square of the number is ",returned_value)
    elif choice == 3 :
        first_num = int(input("Please enter First number:"))
        second_num = int(input("Please enter Second number:"))
        #returned_value = my_exponenation(first_num,second_num)
        returned_value = hof(my_exponenation,first_num,second_num)
        print("The exponenation of the numbers is ",returned_value)

my_calculator()