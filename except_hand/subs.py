#Substring found
# string=input("Enter the string")
# sub=input("Enter the sub-string")
# try:
#     n=string.index(sub)
# except ValueError:
#     print("Sub-string not found")
# else:
#     print("String Found")

string=input("Enter the string: ")
sub=input("Enter the substring: ")
try:
    n=string.index(sub)
except ValueError:
    print("String not found")
else:
    print("String found")

