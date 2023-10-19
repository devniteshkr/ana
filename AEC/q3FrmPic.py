class Not_In_List_Exception(Exception):
    pass

class Already_In_List_Exception(Exception):
    pass

class student:
    list1=[]
   
    def en_name(self,name):
        if name not in self.list1:
            self.list1.append(name)
            print(*self.list1)
        else:
            
            raise Already_In_List_Exception

    def ch_name(self,name): 
        if name in self.list1:
            index=self.list1.index(name)
            new=input("Enter the new element: ")
            self.list1[index]=new
            print(*self.list1)
        else:
            raise Not_In_List_Exception
                    
    def dl_name(self,name):
        if name in self.list1:    
            self.list1.remove(name)    
            print(name,"<- deleted from list")
        else:
            raise Not_In_List_Exception
      
    
    
def main():
    s1=student()

    while True:
        
        
        x=int(input("Enter what you want to do: \n1. Enter Elements \n2. Update if already exists \n3. Delete from list \n4.Exit\n"))
        name=input("Enter the student's name: ")
        match x:
            case 1:
                s1.en_name(name)
            case 2:
                s1.ch_name(name)
            case 3:
                s1.dl_name(name)
            case 4:
                break
            case _:
                print("Invalid")
            
    
        
main()