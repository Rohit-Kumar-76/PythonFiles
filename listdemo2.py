#pow3=list()
'''
for n in range(10):
    pow3.append(3**n)
'''
#pow3=[3**n for n in range(10)]
'''
pow3=[3**n for n in range(10) if n%2==1]
print(pow3)
'''

print("----------------")

#mylist=list(input("input space seprated list values:").split(" "))

mylist=list(
           int(num) for num in
           input("input space seprated list values:").split(" ")
           )

print(mylist)
