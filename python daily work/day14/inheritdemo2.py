class MyBase:
    def display(self):
        print("display from mybase")

#inheriting MyBase to Derive
class Derive(MyBase):
    def show(self):
        print("show from derive")
    def display(self): #method overriding
        print("display from derive")

class Derive2(Derive):
    def show(self):
        print("show from derive-2")
    def display(self): #method overriding
        print("display from derive-2")

#object cretaion
derive=Derive()
derive.show()
derive.display()

derive2=Derive2()
derive2.display()


