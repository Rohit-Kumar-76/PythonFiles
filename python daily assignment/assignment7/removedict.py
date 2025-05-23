myDict = {'a':1,'b':2,'c':3,'d':4}
print(myDict)
a=input("enetr a key")
myDict[a]
if a in myDict:
    del myDict[a]
print(myDict)