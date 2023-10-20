# Excercise1: WAP to read a content from one file and print to other
 
file1=open("filepy.txt",'r')
file2=open("file2.txt",'w')

# for line in file1:
#     file2.write(line)

file2.write(file1.read())

file1.close()
file2.close()

file2 = open('file2.txt','r')
print(file2.read())
file2.close()

