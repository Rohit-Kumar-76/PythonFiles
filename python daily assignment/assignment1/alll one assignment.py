option = 0
while option!=9:
    print("which one you whant to see solution")
    print(" 1  program for printing msg")
    print(" 2 program for area of circle")
    print(" 3 program for radius of circle")
    print(" 4 program for area of tringle")
    print(" 5 program for swaping  ")
    print(" 6 program for addition of 4 digit")
    print(" 7  program for larset number")
    print(" 8  program for total salary")
    print(" 9  for exit program")
    option = int(input("enter one  option:."))

    if option==1:
        print('''"Hello From python"''')
        print("'Hello from python'")
        print("\n")
        # area of circle
    elif option==2:
        radius = float(input("enter the radius:-"))
        area =3.14 * (radius * radius)
        print("area of circle is :", area)
        print("\n")

        # radius of circle
    elif option == 3:
        d = float(input("enter the daimeter of circle:-"))
        r = d / 2
        print("radius of circle:", r)
        print("\n")

        # area of tringle
    elif option == 4:
        base = float(input("enter the base of tringle:-"))
        hight = float(input("enter the hight of tringle:-"))
        area = 1 / 2 * (base) * (hight)
        print("area of tringle is :", area)
        print("\n")

        # swap of two variables
    elif option == 5:
        x = float(input("enter a number"))
        y = float(input("enter second no"))
        print("value of x before swaping", x)
        print("value of x before swaping", y)
        # creating temparary variable
        temp = x
        x = y
        y = temp
        print('the value of x after swap ', format(x))
        print('the value of y after swaping', format(y))
        print("\n")

        # addition
    elif option == 6:
        num = int(input("enter the four digit no"))
        num2 = int(input("enter the second no"))
        sum = num + num2
        print("sum =", sum)
        print("\n")
        # largest no
    elif option == 7:
        x = int(input("enter the no"))
        y = int(input("enter the second no"))
        z = int(input("enter the third no"))
        if x > y & y > z:
            print("largest mo is :", x)
        elif y > x & x > z:
            print("greatest no is :", y)
        else:
            print("greater no is :", z)
            print("\n")

        # hra and da and total salary
    elif option == 8:
        s = int(input("tell me your sellary: "))
        if s <= 2000:
            hra = s / 100 * (20)
            da = s / 100 * (10)
            t = float(hra + da + s)
            print("total=", t)
            print("\n")
        elif s > 2000 & s <= 5000:
            hra = (s / 100) * (30)
            da = (s / 100) * (20)
            t = hra + da + s
            print("total=", t)
            print("\n")

        elif s > 5000 & s <= 10000:
            hra = s / 100 * (400)
            da = s / 100 * (30)
            t = float(hra + da + s)
            print("total=", t)
            print("\n")
        elif s > 10000:
            hra = s / 100 * (50)
            da = s / 100 * (50)
            t = float(hra + da + s)
            print("total=", t)
            print("\n")
    elif option == 9:
        break;

    else:
        print("wrong input ! choose right option")