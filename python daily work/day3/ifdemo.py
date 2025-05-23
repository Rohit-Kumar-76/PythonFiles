#number=int(input("Enter any number"))
'''
if number>0:
    print("Entered value is:")
    print(number)
else:
    print("enter only positive number")

if number%2==0:
    print("number is even")
else:
    print("number is odd")

print("after if-else")
'''
number1=int(input("Enter First number: "))
number2=int(input("Enter Second number: "))
number3=int(input("Enter Third number: "))
#logic to find max value
#using normal if statement
'''
if number1>number2 and number1>number3:
    print("max is:",number1)
if number2>number1 and number2>number3:
    print("max is:",number2)
if number3>number1 and number3>number2:
    print("max is:",number3)
'''
#using nested if statement
'''
if number1>number2:
    if number1>number3:
        print("max is:",number1)
    else:
        print("max is:", number3)
else:
    if number2>number3:
        print("max is:", number2)
    else:
        print("max is:", number3)
'''
#using  else if statement
if number1>number2 and number1>number3:
    print("max is:", number1)
elif number2>number3:
    print("max is:", number2)
else:
    print("max is:", number3)


