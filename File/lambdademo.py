
increment=lambda num,incr=5:num+incr

result=increment(50)
print(result)
print(increment(50,30))

print("--------------------------")
mylist=[1,2,3,4,5,6,7,8,9,10,11,12]

evenlist=list(filter(lambda num :num%2==0,mylist))
print(evenlist)


