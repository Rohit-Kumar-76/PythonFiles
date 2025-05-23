class Student:
    count=0 #static data field
    def __init__(self):
        Student.count=Student.count+1
        print("object created:"+str(Student.count))
    @staticmethod
    def displayCount():
        print("Total Object cretated:" + str(Student.count))
    def __del__(self):
        class_name=self.__class__.__name__
        print(class_name," object destroyed")


#object creation
s1=Student()
s1.displayCount()  #valid in python
Student.displayCount() #preferred this syntax
s2=Student()
s3=Student()
Student.displayCount()

