n=int(input("Enter a number to find factorial:"))
fact=1
for i in range (1,n+1):
    fact=fact*i
print("factorial of ",n,"is",fact)
