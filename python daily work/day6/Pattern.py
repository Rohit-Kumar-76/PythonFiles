

for i in range(1,6): #outer loop
    for sp in range(1,6-i): #inner loop
        print(" ",end=" ") #will print * with space
    for star in range(1,2*i-1+1):
        print("*",end=" ")
    print() #will add new line