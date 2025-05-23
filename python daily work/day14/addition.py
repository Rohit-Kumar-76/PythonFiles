class rohit():
    def getnum(self):
        self.num=num

    def getnum1(self):
        self.num1 = num1
    def setnum(self):
        return self.num
    def setnum1(self):
        return self.num1

class derive(rohit):
    def show(self):
        print("sum=",sum)

a=derive()
a.getnum()
a.show()
