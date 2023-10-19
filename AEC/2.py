#Taking Input of user data from user
def enterdata():
    try:
        username=input("Please enter user name : ")
        user_details["username"]=username
        age=int(input(f"Please enter {username}'s age: "))
        user_details["age"]=age
        #Taking input of all the favourite subjects of the user
        lst=[]
        favourite_subject=0
        while favourite_subject!='1':
            favourite_subject=input(f"Enter all the favourite subject of the {username}, to stop entering press'1' :")
            if favourite_subject!='1':
                lst.append(favourite_subject)
            else:
                favourite_subject='1'
        user_details["favourite_subject"]=lst
        #Taking input of all the places visted by the user
        lst2=[]
        place_visited=0
        while place_visited!='1':
            place_visited=input(f"Enter all the places visited by {username}, to stop entering press'1' :")
            if place_visited!='1':
                lst2.append(place_visited)
            else:
                 place_visited='1'
        user_details["place_visited"]=lst2  
        print("Data added sucessfully")
    except Exception as e:
        print("Error occured, ",e)
    
#Display User record
def displayall():
    print(user_details)
    
user_details={}
choice=0
#Choice for opetaions
while choice!=2:
    #exception handling with try and except block
    try:
        choice=int(input("""
                         1. add user data
                         2. display all data
                         3. quit
                         choice : """))
        match choice:
            case 1:
                enterdata()
            case 2:
                displayall()
            case 3:
                print("You have quit")
            case _:
                print("Invalid Choice")
    except Exception as e:
        print("error occured, ",e)