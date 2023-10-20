# -----------------------------------------------------------------------
# EXERCISE on lambda and Higher Order Functions
# -----------------------------------------------------------------------
# 1)  Convert following functions from function_definitions.py into lambda function and call them



def my_add(fun1,funParam1,funParam2):
    print("Addtion",fun1(funParam1,funParam2))

my_add(lambda a,b : a+b ,1,2)



def my_square(fun1,funParam1):
    print("Square",fun1(funParam1))
    
my_square(lambda a : a**2 ,5)



def expo(fun1,p1,p2):
    print("Exponent",fun1(p1,p2))

expo(lambda a,b : a**b ,2,3)



def my_uppercase_func(f1,v1):
    print("Upper",f1(v1))

my_uppercase_func(lambda a :a.upper() ,"qwerty")



raise_sal=lambda sal,rise :sal*rise/100 
print(raise_sal(2000,20))


height=lambda h : round((h/20.48),2) 
print(height(30))
    

def to_rupee(f1,p1):
    print(f1(p1))
to_rupee(lambda a : a*82 ,int(input("Enter rupees")))
       



def get_fare_details(source, destination, fare_in_INR, discount_rate_percentage):
    return "Fare from" + source +" to " + destination + " is " + str(fare_in_INR- (fare_in_INR*discount_rate_percentage/100) ) + " INR with has a applied discount of " + str(discount_rate_percentage)+ "%"