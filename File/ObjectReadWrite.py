import  pickle
data = {'a': [1, 2.5, 3, 4 + 6j],
        'b': ("character string"),
        'c': {None, True, False}
        }
#writing object in file,serialization
file=open("dictonary.bin","wb")
pickle.dump(data ,file,pickle.HIGHEST_PROTOCOL)
file.close()
print("object saved in file")
#reading object from file,deserialization

file=open("dictonary.bin","rb")
data=pickle.load(file)
print("Data from file:")
print(data)
file.close()
