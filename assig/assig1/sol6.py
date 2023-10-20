''' Take the source, destination, fare in INR, discount_rate percentage from the user and display the 
string ex: "fare from mumbai to pune is 300 INR with has a discount of 5% '''

source_fair = str(input("Enter the source: "))
dest_fair = str(input("Enter the dest: "))
total_fare = float(input("Enter the total fare "))
discount = float(input("Enter the discount raise percentage: "))
actual_fare = total_fare - (total_fare * discount / 100)
print("fare from " ,source_fair,"to",dest_fair,"is" , actual_fare ,"INR with has a discount of ", discount  )
