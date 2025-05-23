#Creating Custom Exception:
class MyException(Exception):
    def __init__(self,message="Salary must be greater than 10000"):
        self.message=message
#Raising Custom Exception:
def inputSalary(sal):
     if sal <  10000:
         raise MyException("Salary must be greater than 10000:")
     print("salary is:"+str(sal))
     elif sal > 50000:
         raise MyException("Salary must be less than 50000:")
     print("salary is :"+str(sal))

#Using Custom Exception:
while(True):

    try:
         sal=int(input("Input your salary:\n"))
         inputSalary(sal)
    except MyException as e:
        print(e.message)
    else:
        break