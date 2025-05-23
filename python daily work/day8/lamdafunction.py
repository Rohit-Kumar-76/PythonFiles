#lambda function

increment=lambda num,incr=5:num+incr
print(increment(10))
print(increment(10,20))

#using lamda function within a function
def increment():

 return lambda num,incr=5:num+incr

f=increment()
res=f(10)
print(res)


# using lambda function with filter
mylist=[1,2,3,4,5,6,7,8,9,10]
#mylist = [1, 3, 4,6, 7, 8, 11, 10, 12]
new_list =list(filter(lambda x: (x%2 == 0) , mylist))
print(new_list)
