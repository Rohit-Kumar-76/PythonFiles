number=int(input("Enter the number to check for prime:")) #20
flag=True
for num in range(2,number//2+1):  #2,10
    if number%num==0:
        flag=False
        break
        #print(num)

if flag==True:
    print("Number is prime")
else:
    print("Number is non-prime")

