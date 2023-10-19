#Take input
stir=input("PLease enter data to be written in the file: ")
with open("mydata.txt",'w') as fh:
    fh.write(stir)
    print("dATA Aadded")