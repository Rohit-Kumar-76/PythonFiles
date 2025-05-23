#Creating Custom Exception Class:
class SalaryException(Exception):
    def __init__(self,message="Salary must be greater than 10000"):
        self.message=message

#Raising Custom Exception:
def inputSalary(sal):
    if sal<10000:
        raise SalaryException() #raise is used to generate exception forcefully
    elif sal > 50000:
            raise SalaryException("Salary should be less than 50000")  # raise is used to generate exception forcefully
    print("salary is:"+str(sal))

#Using Custom Exception:
while(True):
    try:
        sal=int(input("Input your salary:\n"))
        inputSalary(sal)
    except SalaryException as e:
            print(e.message)
    else:
        break
