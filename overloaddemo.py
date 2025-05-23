
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return  Point(x,y) #returning new object
    def __sub__(self, other):
        x=self.x-other.x
        y=self.y-other.y
        return  Point(x,y) #returning new object
    def __mul__(self, other):
        x=self.x*other.x
        y=self.y*other.y
        return  Point(x,y) #returning new object
p1=Point(20,10)
p2=Point(30,20)
print(p1)
print(p2)
print(p1+p2)
print(p1-p2)
print(p1*p2)