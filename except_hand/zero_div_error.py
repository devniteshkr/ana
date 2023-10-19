# print("Hello")
# print(10/0)
# print("Hi")

try:
    x=int(input("Enter the first number: "))
    y=int(input("Enter second number: "))
    print(x/y)
except ZeroDivisionError:
    print("Can't divide with zero")
except ValueError:
    print("please provide integer value")