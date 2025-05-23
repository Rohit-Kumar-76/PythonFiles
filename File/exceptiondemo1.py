
try:
    num1=int(input("Enter numerator value:"))
    num2=int(input("Enter denomerator value:"))
    result=num1/num2
    print("result is :",result)
except ValueError as ve:
    print(ve)
except ZeroDivisionError as zde:
    print(zde)
except Exception as ex:
    print(ex,"exception clause")

finally:
    print("finally will execute always")
    print("it is used to free resources occupied by the try block ")
print("Program ended")
