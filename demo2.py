import numpy as np

#list = [23,12,34,32,14,15,3,45,23]
'''
arr1 = np.array(list)
print("array:",arr1)
print ("Maximum : ",arr1.max())
print ("Mean : ",arr1.mean())
print ("Minimum : ",arr1.min())
print ("Sum : ",arr1.sum())
print ("Median : ",np.median(arr1))
print ("STD Devi. ",np.std(arr1))
print(arr1)
print ("Sorted Array : ",np.sort(arr1))
print ("Sorted Index : ",np.argsort(arr1))
'''

#2-D array sorting
'''
list1 = [[1,5,4],[7,6,10],[3,4,2],[9,8,15.5]]
arr1  = np.array(list1)
print("Before sorting:")
print(arr1)
print("After sorting:")
#print (np.sort(arr1,axis=0))
print (np.sort(arr1,axis=1))
print(arr1.var())
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
print(arr1.dtype)
print(arr1.itemsize)
print(arr1.data)
'''
arr=np.zeros((3,5),float)
print(arr)
arr=np.ones((4,4),int)
print(arr)
arr=np.arange(10)
print(arr)
arr=np.random.random(10)
print(arr)
arr=np.eye(3,3,dtype=int)
print(arr)
arr.var()





