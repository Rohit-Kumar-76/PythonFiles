class mybase:
    def display(self):
        print("this is rohit")
class derive(mybase):
    def show(self):
        print("rohit mehta")
class derive1(derive):
    def show(self):
        print("show d2")
    def display(self):
        print("from derive 2")

d=derive()
d.show()
d.display()

d2=derive1()
d2.display()

