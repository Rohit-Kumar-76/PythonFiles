
#class defn
class Employee:
    '''
    id=20
    name="Rohit"
    salary=24500 #static
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

#object cretaion
emp=Employee()
#print(emp)
emp.setCode(1000)
emp.setName("Rohit")
emp.setSalary(24500)
emp.displayEmpDetails()  #calling of methods
emp.setEmpDetails(2000,"Vishal",30500)
emp.displayEmpDetails()

print(emp.getCode())
print(emp.getName())
print(emp.getSalary())

emp2=Employee()
#emp2.setEmpDetails(3000,"Sandeep",23500)
emp2.setEmpDetails(
                    int(input("Enter Code:")),
                    input("Enter name:"),
                    float(input("Enter Salary:"))
                  )
emp2.displayEmpDetails()
print("_"*50)
print(emp2.code)
print(emp2._name)
#print(emp2.__salary)  #incorrect ,invalid bcz it's private

emp2.age=25;  #adding new property
print(emp2.age)


