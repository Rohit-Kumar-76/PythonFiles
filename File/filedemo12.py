import  os

'''
if os.path.exists("test.txt"):
    file=open("test.txt","r")
    print("file opened successfully!!!!!!")
else:
    #print("File does not exits")
    file = open("test.txt", "w")
    print("File created successfully ")
'''
#writing data in file

#file=open("test.txt","w")
'''
file=open("test.txt","a") #appned mode writing
data=input("Enter data to be written in file:")
file.write(data)
file.close()
print("Data written in file!!!!")
'''
#Reading data from file
file=open("test.txt","r");
#data=file.read()
#data=file.read(20)
#reading data from file line by line
'''
data=file.readline()
print("Data from file:")
while data:
    print(data)
    data = file.readline()
'''

#reading data from file using readlines()
data=file.readlines()
print("Data from file:")
print(data)












