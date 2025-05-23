
num=int(input("Enter no to sum"))
count=0
sum=0
while num!=0:
     count=count+1
     sum=sum+num%10
     num=num//10
print(count," digit and sum is ",sum)