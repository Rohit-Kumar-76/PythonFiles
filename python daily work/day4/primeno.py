#for cheacking prime no


number=int(input("enetr a nomber"))
flag=True
for num in range(2,number//2+1):
    if number%num==0:
        flag=False
        break

if flag==True:
   print("Number is prime")
else:
   print("Number is non-prime")