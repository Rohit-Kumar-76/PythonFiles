#swap of two variables

x=float(input("enter a number"))
y=float(input("enter second no"))

print("value of x before swaping",x)
print("value of x before swaping",y)

# creating temparary variable
temp=x
x=y
y=temp
print('the value of x after swap ',format(x))
print('the value of y after swaping',format(y))
