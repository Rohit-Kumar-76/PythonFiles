class student:
    count=0
    def __init__(self):
        student.count=student.count+1
        print("object is created:-"+str(student.count))
    @staticmethod
    def displaycount():
        print("Total object created:_"+str(student.count))
    def __del__(self):
        class_name=self.__class__.__name__
        print(class_name,":-object destroyed")

s1=student()
s1.displaycount()
student.displaycount()
s2=student()
s3=student()
student.displaycount()

