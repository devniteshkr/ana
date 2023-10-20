# """
# 3)  Create a program named "my_set_store" which support following operations on two sets
#     provided by user 

# for ex: 
# 	A = {1,2,3,4,5}
# 	B = {18,19,20,21}
# is provided by the user

# Operations supported by our program are :
# 	1: Union
# 	2: Intersection 
# 	3: A-B
# 	4: B-A
# 	5: Take a element from user and Display if that element is a member of set B 
# 	6: Display number of elements in the set A
#     7: Display number of elements in the set B
# 	8: Add an element taken from the user to the set A
# 	9: Add multiple elements taken from the user to the set A
# 	10: Remove an element taken from the user from set A
# """
# Sample code template for my set store
def set_union(setA,setB) :
	return setA.union(setB)

def set_intersection(setA,setB) :
	return setA.intersection(setB) 

def set_minus(setA,setB) :
	return setA.difference(setB)

def is_member_of_set(setB) :
    member=print(input("Enter a member to check in set"))
    return setB.issubset(member)

def set_display(setA):
	return len(setA) 
		
def set_add_element(setA,member):
	return setA.add(member)

def set_add_elements(setA,members):
	return setA.update(members)

def set_remove_element(setA,member):
	return setA.remove(member) 

def my_set_store():
	print("\n Welcome to Our Set Store !!! ")

	setA= set(input("Please enter comma seperated elements for the set A  :: ").split(","))
	setB= set(input("Please enter comma seperated elements for the set B :: ").split(","))
 
	while(True):
		print("\n*************** Menu **********************")
		print("Operations supported by our program are :")
		print("	1: Union")
		print("	2: Intersection ")
		print("	3: A-B")
		print("	4: B-A")
		print("	5: Take a element from user and Display if that element is a member of set B ")
		print("	6: Display number of elements in the set A")
		print(" 7: Display number of elements in the set B")
		print("	8: Add an element taken from the user to the set A")
		print("	9: Add multiple elements taken from the user to the set A")
		print("	10: Remove an element taken from the user from set A")
		print(" 11: Exit")

		choice = int(input("Please enter your choice "))

		if choice   ==1:
			print(set_union(setA,setB))  
		elif choice ==2:
			print(set_intersection(setA,setB))
		elif choice ==3:
			print(set_minus(setA,setB))
		elif choice ==4:
			print(set_minus(setB,setA))
		elif choice ==5:
			print(is_member_of_set(setB)) 
		elif choice ==6:
			print(set_display(setA))
		elif choice ==7:
			set_display(setB)
		elif choice ==8:
			print(set_add_element(setA))
		elif choice ==9:
			print(set_add_elements(setA))
		elif choice ==10:
			print(set_remove_element(setA))
		elif choice ==11:
			break
		else:
			print("Invalid Input , Please Try Again !!!!  ")  
			
my_set_store()