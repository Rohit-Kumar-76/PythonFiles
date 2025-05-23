class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return "{:<10}{:<10}".format(self.name,self.age)

class human:
  def add(self,name,age):
    list1={name,age}

  def veiw(self,name,age):
    print(list1)


x=input("enetr name:")
y=int(input("enetr age"))
p1 =Person(x,y)
p1=human()
p1.add(x,y)
p1.veiw(x,y)


print(p1)
