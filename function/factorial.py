# num=int(input("Enter number: "))
# result=1
# while(num>=1):
#     result=num*result
#     num=num-1
# print("factorial of ",num,"is",result)


# def fact(num):
#     result=1
#     while(num>=1):
#         result=num*result
#         num=num-1
#     print("factorial of num","is",result)
# fact(int(input("Enter number")))


def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print("Factorial of 4 is :",factorial(4))
