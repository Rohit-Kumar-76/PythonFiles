#class defn
class Employee:
    '''
    id=20
    name="Rohit"
    salary=24500 #static
    '''
    #default constr

    def __init__(self):
        self.__code = 100
        self.__name = "admin"
        self.__salary = 34500

        print("constr called")

    '''

    def __init__(self,code=100,name="admin",salary=24500):
        self.code = code
        self._name = name
        self.__salary = salary
        print("parametric constr called")
        '''

    #setter methods/mutators
    def setCode(self,code):
        self.code=code
    def setName(self,name):
        self._name=name
    def setSalary(self,salary):
        self.__salary=salary
    #getter method/inspectors
    def getCode(self):
        return self.code
    def getName(self):
        return self._name
    def getSalary(self):
        return self.__salary
    #behaviorial method/mutator
    def setEmpDetails(self,code,name,salary):
        self.code = code
        self._name = name
        self.__salary=salary
        print("details saved")
    # behaviorial method/inspector
    def displayEmpDetails(self):
        print("Employee details are:")
        print(self.code,"\t",self._name,"\t",self.__salary)

emp1=Employee()
emp1.displayEmpDetails()
emp2=Employee(2000)
emp2.displayEmpDetails()
emp3=Employee(code=5000,name="rohit",salary=45000)
emp3=Employee(code=int(input("en")),name=input("name"),salary=int(input("sal")))
emp3.displayEmpDetails()




