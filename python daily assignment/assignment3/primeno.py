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







if number>1:
    for i in range(2,number):
        if number % i == 0:
            print(number,"is not a prime no")
            print(i,"times",number//i,"is",number)
            break
        else:
            print(number,"is a prime number")

else:
    print(number,"is not a prime number")