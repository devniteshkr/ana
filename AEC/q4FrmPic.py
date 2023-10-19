#for running change directory int terminal to the currednt direcctory rather than paretn directory

import os
print("quote txt will now be read")
# with(open('quote.txt',"r")as file1):
#     print(file1.read())
# print(os.path.realpath('new.txt'))
# print(os.path.realpath('q4FrmPic.py'))
try:
    file1=open('new.txt',"r")
    print("Reading...\n",file1.read())
except FileNotFoundError as e:#'as e' not needed
    print("File not present",e.strerror)#'e.strerror' not needed
# file1 = open('my_first_file.txt','rt')
# print(file1.read())