import os

'''
if os.path.exists("test.txt"):

    file=open("test.txt","r")
    print("file opened")
else:
    file = open("test.txt", "w")
    print("file created")
'''

#file=open("test.txt","w")
file=open("../../new project/test.txt", "a")
data=input("enetr data to be written in file")
file.write(data)
file.close()
print("data written in file")

file=open("../../new project/test.txt", "r")
#data=file.read()
data=file.read(10)
print("read data from file")
print(data)

