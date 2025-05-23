#class defn
class Employee:

    def __init__(self):
        self.__code = 100
        self.__name = "admin"
        self.__salary = 34500
        self.__dpid=34
        self.__bloudg="B+"

        print("constr called")

    def setCode(self,code):
        self.__code=code
    def setName(self,name):
        self.__name=name
    def setSalary(self,salary):
        self.__salary=salary
    def setBloudgroup(self,bloudg):
        self.__bloudg=bloudg
    def setDpid(self,dpid):
        self.__dpid=dpid


    def getCode(self):
        return self.__code
    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary
    def getBloudgroup(self):
        return self.__bloudg
    def getDpid(self):
        return self.__dpid


    def setEmpDetails(self,code,name,salary,dpid,bloudg):
        self.__code = code
        self.__name = name
        self.__salary=salary
        self.__dpid=dpid
        self.__bloudg=bloudg
        print("details saved")


    def displayEmpDetails(self):
        print("Employee details:")
        print(self.__code,"\t",self.__name,"\t",self.__salary,"\t",self.__dpid,"\t",self.__bloudg)


emp1=Employee()
emp1.displayEmpDetails()
id=int(input("eneter Id:"))
name=input("Enetr Name:")
sal=float(input("enetr Salary:"))
dpcode=int(input("Enetr department id:"))
bg=input("enetr bloudgroup:")
emp1.setEmpDetails(id,name,sal,dpcode,bg)
emp1.displayEmpDetails()





