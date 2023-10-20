#Excercise2: WAP to copy the content from one file to other but each line is pretended by HPCSA


list=[]
file1=open("filepy.txt","r")
for x in file1:
    list.append(x)
file1.close()
 
# file2=open("filepy.txt",'w')
# file2.close()

file2=open("filepy.txt","w")
for x in list:
    file2.write(f'HPCSA{x}')

file2.close()

file2 = open("filepy.txt",'r')
print(file2.read())
file2.close()




