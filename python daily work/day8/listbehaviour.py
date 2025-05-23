

#list compprehension
#example 1
pow3=list()

for x in  range(1,10):
    pow3.append(3**x)

print(pow3)

#example 2
pow3=[3**x for x in range(10)]
print(pow3)
#example 3
pow3=[3**x for x in range(10) if x%2==1]
print(pow3)
