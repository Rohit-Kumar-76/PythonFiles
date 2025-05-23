#figure one
print("figure one")
for i in range(1,6):
    #for j in range(1,i+1):
     for i in range(i):
        print("*",end=" ")
     print()
# opposite figure
print("----------")
for i in range(1,6):
    for j in range(1,7-i):
        print("*",end=" ")
    print()

# mirror effect
for i in range(1, 6):
    for sp in range(1, 6 - i):
        print(" ", end=" ")
    for st in range(1,i+1):
        print("*",end=" ")
    print()

# revese of three
print("reverse of three")
for i in range(1, 6):
    for sp in range(1,i):
        print(" ", end=" ")
    for st in range(1,7-i):
        print("*",end=" ")
    print()
print("no printing")
for i in range(1,6):
     for i in range(1,i+1):
        print(i,end=" ")
     print()


print("revers of upper figure")
for i in range(1,6):
    for i in range(5,i-1,-1):
        print(i,end=" ")
    print()
print("--A to E---")

for i in range(1,6):
     for i in range(1,i+1):
        print(chr(64+i),end=" ")
     print()

print("------------")
#reverse of upper figure
for i in range(1, 6):
    for sp in range(1,i):
        print(" ", end=" ")
    for st in range(1,7-i):
        print(chr(64+st),end=" ")
    print()

#traingle
print("half daimond")
for i in range(1,6):
    for sp in range(1,6-i):
        print(" ",end=" ")
    for st in range(1,i*2):
        print("*",end=" ")
    print()






