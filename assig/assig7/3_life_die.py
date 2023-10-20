# 3) Create program that takes age of the user as input
# and prints number of days that user has lived for
# Exception handle the code such that if the user has lived for more than
# 100001 days then user should get the message
# , you lived for so long , may be you will die soon:)



class expiry_date(Exception):
    pass

age = int(input("age of the user"))
no_of_days_lived = age*365

#Exception handle the code such that if the user has lived for more than 100001 days
if no_of_days_lived > 100001 :
        # raise an exception with you lived for so long , may be you will die soon:)
        print("you lived for so long , may be you will die soon:)")
        raise expiry_date
else:
    print(no_of_days_lived)  