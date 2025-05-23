print("*"*23)
print(" 1 AREA OF CIRCLE    |")
print(" 2 AREA OF TRIANGLE  |")
print(" 3 AREA OF RECTANGLE |")
print(" 4  EXIT()           |")
print("*"*23)
num=int(input("Enter a option :"))
def circle(r):
    area=3.14*r*r
    return area
def traingle(h,b):
    area=1/2*h*b
    return area
def rectangle(w,l):
    area=l*w
    return area
if num==1:
    number=int(input("enetr radius:"))
    x=circle(number)
    print("Area of Circle is:",x)

elif num==2:
    num1 = int(input("enetr hight:"))
    num2 = int(input("enetr base :"))
    x=traingle(num1,num2)
    print("Area of Triangle is:",x)

elif num==3:
    num1 = int(input("enetr width:"))
    num2 = int(input("enetr lenght :"))
    x=rectangle(num1,num2)
    print("Area of Triangle is:",x)

elif num==4:
    exit(0)
else:
    print("wrong input!")