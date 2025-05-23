#normal approach
print("*"*30)
#num = int(input("Enter a number: "))
num=5
factorial = 1
if num < 0:
   print(" Factorial does not exist for negative numbers")
elif num == 0 or num == 1:
   print("The factorial is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


print("*"*30)
# by using function
def fact(n):
    return 1 if (n==1 or n==0) else n*fact(n-1)

num=5
print("factorial of ",num,"is",fact(num))


print("*"*30)
# Python  program to find
# factorial of given number
# by using built in function
import math

def fact(n):
    return (math.factorial(n))


num = int(input("Enter the number:"))
f = fact(num)
print("Factorial of", num, "is", f)

