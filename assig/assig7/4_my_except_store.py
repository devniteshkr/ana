# 4)Create the following program named "my_exception_store" with the menu below :

# Welcome User , What would you like to do today ?
#     1) Create a postive numbered list
#     Note : raise an exception if the users inserts a negative number OR user creates an empty list
#     2) Create a negative  numbered list
#     Note : raise an exception if the users inserts a positive number/Zero OR user creates an empty list
#     3) Create a heterogenous list
#     Note : raise an exception if the users creates a homogenous list (all elements of same datatype)

#     4) Check if the element is present in the list
#     Take the Input element that you would like to search
#     and which of the above three list that he want to search element from
#     Note : raise an exception if the element is not found in the list
#     with a message "Sorry, Element could not be found"

#     5) Refresh the program to start with blank lists
#     6) Exit

# Handle exceptions in the script for all operations
# and let the user continue till he chooses to exit from the program



class negative_number_received(Exception):
    pass

# definition
def  create_positive_numbered_list(my_int_list):
    """
    Note : raise an exception if the users inserts a negative number OR user creates an empty list 
    """

    for i in range(int(input("No of elements:"))):
        val = int(input("element please:")) 
        if val >0 :
            my_int_list.append(val)
        else:
            raise negative_number_received    
    print(my_int_list)            

# execution
my_int_list1=[]    
create_positive_numbered_list(my_int_list1)    



class positive_number_received(Exception):
    pass

# definition
def  create_negative_numbered_list(my_int_list):
    """
    Note : raise an exception if the users inserts a negative number OR user creates an empty list 
    """

    for i in range(int(input("No of elements:"))):
        val = int(input("element please:")) 
        if val <0 :
            my_int_list.append(val)
        else:
            raise positive_number_received
    print(my_int_list)            

# execution
my_int_list1=[]    
create_negative_numbered_list(my_int_list1)   





# my custom exception created 
class homogenous_list_error(Exception):
    pass

def value_provider(element):
    datatype_choice = int(input(f"Please choose a datatype of the {element} to be added \
        \n 1) int \n 2) float \n 3) str \n 4) tuple \n 5) list \n 6) set \n 7) dictionary \n "))

    if datatype_choice == 1:
        ret_val = int(input("Please enter an integer to be added "))
    if datatype_choice == 2:
        ret_val = float(input("Please enter a float to be added "))
    if datatype_choice == 3:
        ret_val = input("Please enter a string to be added ")
    if datatype_choice == 4:
        ret_val = tuple(input("Please enter a tuple to be added like 1,2 ").split(","))
    if datatype_choice == 5:
        ret_val = input("Please enter a list to be added like 1,2,3,4 ").split(",")
    if datatype_choice == 6:
        ret_val = set(input("Please enter a set to be added like 1,2 ").split(","))
    if datatype_choice == 7:
        my_temp_dict = {}
        keys = input("Please enter the keys of the dictionary to be added like key1,key2 ").split(",")
        for key in keys : 
            my_temp_dict[key] = value_provider('key'+key)
        ret_val = my_temp_dict
    return ret_val

def create_heterogenous_list(my_list):
    """    3) Create a heterogenous list 
    Note : raise an exception if the users creates a homogenous list (all elements of same datatype)
    """
    for cntr in range(0,int(input("Please enter number of elements to the heterogenous list"))):
        my_list.append(value_provider('Index'+str(cntr)))
    print(my_list)   

    # check if we are have a homogenous list  
    is_homogenous = True
    for subscript in range(1,len(my_list)):
        if  type(my_list[0]) != type(my_list[subscript]):
            is_homogenous = False
            break

    if is_homogenous:
        raise homogenous_list_error
    else:
        print("We received a Heterogenous list ")    

my_list = []        
create_heterogenous_list(my_list)
