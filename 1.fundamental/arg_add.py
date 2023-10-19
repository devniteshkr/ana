from sys import argv
sum=0
args=argv[1:]
for x in args:
    y=int(x)
    sum=sum+y
print("Sum: ",sum)