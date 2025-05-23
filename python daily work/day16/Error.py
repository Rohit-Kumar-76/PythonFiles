
try:

    num1=int(input("Enter the numerator:"))
    num2=int(input("Enetr the denomerator:"))
    res=num1/num2
    print("result:",res)


except ValueError as ve:

    print(ve)

except ZeroDivisionError as zde:
    print(zde)

except Exception as ex:
    print(ex,"Exeption Clouse")

finally:
    print("finally will execute always")
    print("it is use to free resources occupied by the try block")

print("program End")