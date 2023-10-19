#creating class user management
class user_management():
    #Default constructor
    def __init__(self,username):
        self.__username=username
    def __str__(self):
        return f"username: {self.__username}"
    
    #setter function
    def set_username(self,username):
        self.__username=username
    
    #getter function
    def get_username(self):
        return self.__username

#Display all usernames
def displayall():
    lst=[]
    for a in user_name.values():
        names=a.get_username()
        lst.append(names)
    print(lst)

#check if the username already exists
def checkuser(name):
    if len(user_name)==0:
        return 2
    else:
        for elements in user_name.values():
            if elements.get_username==name: #Username already exist
                return 1
            else: #user does not exist
                return 2
        
#Enter new user
def enternewuser():
    try:
        name=input("Enter name of the new user : ")
        a=user_management(name)
        status=checkuser(name)
        if status==2:
            user_name[name]=a
            print("username added sucessfully")
        else:
            print("user already exists ")
    except Exception as e:
        print("Error occured, ",e)

#Update name of the current user to new one
def updateuser():
    try:
        name=input("Enter name of the user : ")
        up_name=input("Enter new name of the user : ")
        status=checkuser(name)
        if status==1:
            print("User does not exist")
        else:
            for elements in user_name.values():
                if elements.get_username==name:
                    elements.set_username(up_name)
            print("name updates sucessfully")
    except Exception as e:
        print("Error occured, ",e)

#delete already existing user
def deleteuser():
    try:
        name=input("Enter name of the user : ")
        status=checkuser(name)
        if status==1:
            print("User does not exist")
        else:
            for key,value in user_name.items():
                if value.get_username==name:
                    user_name.pop(key)
            print("name deleted sucessfully")
    except Exception as e:
        print("Error occured, ",e)
        
        
user_name={}
choice=0
#taking command from user to perform  desired operations
while choice!=5:
    try:
        choice=int(input("""
                         1. Enter new user name
                         2. Update username
                         3. Delete user name
                         4. Display all users
                         5. Quit
                         choice : """))
        match choice:
            case 1:
                enternewuser()
            case 2:
                updateuser()
            case 3:
                deleteuser()
            case 4:
                displayall()
            case 5:
                print("You have quit")
            case _:
                print("Invalid choice")
    except Exception as e:
        print("Errpr occured, ",e)
