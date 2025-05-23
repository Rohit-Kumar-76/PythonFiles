print(" choose one option")
print(" 1. addition ")
print(" 2. subtraction")
print(" 3. multiplication")
print(" 4  division")
num=int(input("Enetr one option"))
if num==1:
       x=int(input("enter a number "))
       y=int(input("enter second number"))
       print("sum=",x+y)
elif num==2:
       x = int(input("enter a number "))
       y = int(input("enter second number"))
       print("sub=", x - y)
elif num==3:
       x = int(input("enter a number "))
       y = int(input("enter second number"))
       print("div=", x / y)
elif num==4:
       x = int(input("enter a number "))
       y = int(input("enter second number"))
       print("mul=", x * y)
else :
    print("choose right option")