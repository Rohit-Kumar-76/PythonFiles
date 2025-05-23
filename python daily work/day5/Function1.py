
#function without return value and without parameter
def pattern():
    for i in range(1, 6):  # outer loop
        for sp in range(1, 6 - i):  # inner loop
            print(" ", end=" ")  # will print * with space
        for star in range(1, 2 * i - 1 + 1):
            print("*", end=" ")
        print()  # will add new line

#function with return value and with parameter

def add_values(x,y):
    "function to add two number"
    z=x+y
    return z
#function with return value and without parameter
def subtract_values():
    "function to subtract two number"
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return num1-num2

#function without return value and with parameter
def multiply_values(x,y):
    "function to multiply two numbers"
    result=x*y
    print("Multiplication is:",result)

#pattern() #function calling
if __name__=="__main__":
    #pattern()
    #calling way-1 with return value
    #result=add_values(50,40) #calling of add_values
    #print("sum is :",result)
    '''
    print("Sum is:",add_values(60,90))  #calling way-2 with return value
    num1=int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Sum is:", add_values(num1, num2))
    print("Enter values for subtraction:")
    print("Difference is:", subtract_values())
    '''
    multiply_values(3,5) #valid
    print(multiply_values(5,6))#logically incorrect but valid


