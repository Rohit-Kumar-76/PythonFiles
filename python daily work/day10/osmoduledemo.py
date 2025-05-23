import  os

print(os.system("dir"))

#os.system("cls")
#print(os.system("cd\\"))
#print(os.environ)

#os.mkdir("dir1") #dir1 will be created in CWD,path is relative

#dir2 will be created in D:\PythonCode,path is absolute
os.mkdir("D:/PythonCode/dir2")

os.mkdir("dir1/dir3")

