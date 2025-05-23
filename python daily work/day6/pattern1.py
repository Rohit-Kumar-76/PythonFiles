#basic behaviou

for i in range(1,6):#outer loop
    for j in range(1,6):
        print("*",end=" ")
    print()
print(" \n second patter")

# another way
print("figure one")
for i in range(1,6):
    #for j in range(1,i+1):
     for i in range(i):
        print("*",end=" ")
     print()
print("  \n")

print(" ")
for i in range(1,6):
    for j in range(6,1,-1):
        for k in range(1,i+1):
         print("*",end=" ")
    print()
print("next figure")
print("figure two")
for i in range(1,6):
    for j in range(1,7-i):
        print("*",end=" ")
    print()
print("figure three")
 # opposite structure
for i in range(1, 6):
    for sp in range(1, 6 - i):
        print(" ", end=" ")
    for st in range(1,i+1):
        print("*",end=" ")

    print()
print("figure four")
print("\n")
#reverse or this
for i in range(1, 6):
    for sp in range(1,i):
        print(" ", end=" ")
    for st in range(1,7-i):
        print("*",end=" ")
    print()

print("figure five")
print("\n")
for i in range(1, 6):
    for sp in range(1,6-i):
        print(" ", end=" ")
    for st in range(1,2*i):
        print("*",end=" ")
    print()
print("figure six")
for i in range(1,6):
    for sp in range(1,i):
        print(" ", end=" ")
    for st in range(1,2*i):
        print("*",end=" ")
    print()