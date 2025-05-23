class MyBase:
    def display(self):
        print("display from mybase")

#inheriting MyBase to Derive
class Derive(MyBase):
    def show(self):
        print("show from derive")

#object cretaion
derive=Derive()
derive.show()
derive.display()


