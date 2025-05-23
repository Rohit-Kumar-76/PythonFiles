#using and operator
num1=20
num2=25
result=num1<30 and num2<50
print(result)

#using or operator
x='b'
result= x=='a' or x=='e' or x=='i' or x=='o' or x=='u'
print(result)

#using not operator
flag=False
print(not flag)

#Identity Operator
x=10
y="10"

print(x is y)
print(x is not y)

#bitwise operator
x=10
y=15
'''
result=x&y
print(result)
print(x|y)
print(x^y)
print(x>20 | y<30)

x=x^y
y=x^y
x=x^y
print(x,",",y)
'''
x=10
y=15
result=y+(~x+1)
print(result)






