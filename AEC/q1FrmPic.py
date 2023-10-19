list1=list(input("Enter elements in list 1: ").strip().split(" "))[:4]#strip removes the endline char like-> \n after every line
list2=list(input("Enter elements in list 2: ").strip().split(" "))[:4]


x=int(input("""What do you wna to do? 
            \n1. Make ditionary of both lists 
            \n2. Add new element in list 1 
            \n3. Delete an element from list 2 \n"""))


def add_new(new):
    list1.append(new)
    print(*list1)
    
    
def d_Elem(dEx):
    if dEx in list2:
        print(*list2)
        list2.remove(dEx)
    print(*list2)
    
def mk_dic(list1,list2):
    # print(*list1)
    dict1={}
    # ln1=len(list1)
    # ln2=len(list2)
    for keys in list1:
        # print(keys)
        for values in list2:
            dict1[keys]=values
    print(dict1)
        
match x:
    case 1:
        mk_dic(list1,list2)
    case 2:
        new=input("Enter new element  to be added in list 1: ")
        add_new(new)
    case 3:
        dEx=input("Enter element to be deleted: ")
        d_Elem(dEx)
    case _:
        print("Invalid choice")
    