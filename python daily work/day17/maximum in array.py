import numpy as np
'''
list=[23,12,3,5,6,86,14,16,19]
arr1=np.array(list)
print("array:",arr1)
print("Maximu:",arr1.max())
print("mean:",arr1.mean())
print("Minimum:",arr1.min())
print("Sum:",arr1.sum())
print("Median:",np.median(arr1))
print("STD devi:",np.std(arr1))
print("Sorted array:",np.sort(arr1))
print("sorted index:",np.argsort(arr1))

'''
'''
#2-D array
list1=[[1,2],[7,6],[3,4],[2,6]]
arr=np.array(list1)
print(np.array(list1))
print(np.sort(arr,axis=0))# axis=0 is sorting data in vertically and axis=1 is horizontaly
print(arr.var())
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
print(arr.itemsize)
print(arr.data)
'''
arr=np.zeros((3,2),int)
print(arr)
arr=np.ones((4,4),int)
print(arr)
arr=np.arange(10)
print(arr)
arr=np.random.random(10)
print(arr)
ar=np.eye(3,3,dtype=int)
print(ar)