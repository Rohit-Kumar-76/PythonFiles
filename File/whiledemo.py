
'''
i=1
while i<=10:
    #print("hello from python-",i)
    print(i,end=" ")
    i=i+1
    #i+=1

print("\nafter loop")
'''
#logic to count number of digits using while loop
number=int(input("Enter any number:")) #1234
count=0
sum=0
while number!=0:
    count=count+1 #4
    sum=sum+number%10
    number=number//10  #number=0

print("Number of digits:",count)
print("Sum of digits:",sum)















