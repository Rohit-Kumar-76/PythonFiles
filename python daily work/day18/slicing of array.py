import numpy as n
list1=[1,2,3,4,5,6]
ar=n.array(list1)
print(ar[-3:])
print(ar[:2])
print(ar[::-1])


print("+"*30)

list2=[[1,2],[3,4],[5,6],[7,8]]
ar=n.array(list2)
print(ar)
print("------------")
print(ar[:,0])
print("============")
print(ar[:,1])
print("x"*20)
print(ar[1:,])
print("--"*10)
print(ar[1::2,:])