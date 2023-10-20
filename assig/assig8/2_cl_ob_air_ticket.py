# -------------------------------------------
# Exercise 02 : Classes and objects -- try creating this in oops world
# -------------------------------------------
 
# Create a class that captures airline tickets. 
# Each ticket lists the departure and arrival cities, a flight number, and a seat assignment. 
# A seat assignment has both a row and a letter for the seat within the row (such as 12F). 

# main method:
# Make two examples of tickets being sold to passengers.
# display tickets booked details 


import random
import string

class Airline:
    
    list=[]
    airline_name="INDIGO AIRLINES"
    def __init__(self,dcity,acity,p_name):
        
        letters = string.ascii_uppercase
        self.departure_cities=dcity
        self.pass_name=p_name
        self.arrival_cities=acity
        self.flight_number= random.randrange(4, 10)
        self.seat_assign=str(random.randrange(2, 3))+random.sample(letters, 1)[0]
        
    def get_departure(self):
      return self.departure_cities
    def get_seat(self):
      return self.seat_assign 
    
    def get_arrival(self):
      return self.arrival_cities
     
    def get_flight(self):
      return self.flight_number 
    
    def set_arrival(self,rcv_arri):
        
        self.arrival_cities=rcv_arri 
    def set_departure(self,rcv_depar):
        
        self.departure_cities=rcv_depar   
    
    def set_flight(self,rcv_flight_num):
        
        self.flight_number=rcv_flight_num
        
    def set_seat(self,rcv_seat):
        
        self.seat_assign=rcv_seat
    
             
        
         
       



def main():
    
    ticket=int(input("Enter How Many Tickets You want :")) 
    i=0
   
    while i<ticket:
        print("******Enter Your Details****** ")
        departure=input("Enter Departure city :") 
        aarrival=input("Enter Arrival  city :") 
        name=input("Enter Your name :") 
        obj=Airline(departure,aarrival,name)
        Airline.list.append(obj)
        i+=1
        
    for i in  Airline.list:
        print("welcomes to the ",i.airline_name)
        print("Your Name is : ",i.pass_name)
        print("your destination is : ",i.get_arrival())
        print("you Departured from : ",i.get_departure())
        print("your Flight number : ",i.get_flight())
        print("your Seat number  : ",i.get_seat())
        print("************************ ")




if __name__=="__main__":
    main()        