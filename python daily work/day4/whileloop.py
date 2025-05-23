i=0
while i<10:
     print(i,end=" ")
     i=i+1
num=int(input("enter no"))
count=0
sum=0
while num!=0:
     count=count+1
     sum=sum+num%10
     num=num//10
print(" digit ",count)
print("sum=",sum)
     