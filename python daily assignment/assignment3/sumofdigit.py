#sum  of digits using while loop
num=int(input("Enter any number:"))
c=0
sum=0
while num!=0:
    c=c+1
    sum=sum+num%10
    number=num//10

print("Number of digits:",c)
print("Sum of digits:",sum)