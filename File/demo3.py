import numpy as np
#slicing
list1 = [1,2,3,4,5,6]
arr1 = np.array(list1)
print(arr1) #[1,2,3,4,5,6]
print(arr1[:2])  #[1,2]
print (arr1[-3:])  #[4,5,6]
print (arr1[1::2])  #[2,4,6]
print (arr1[::-1])  #[6,5,4....1]


list2 = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]]
arr2  = np.array(list2)
print(arr2)  #[[1,2],[3,4],[5,6],[7,8]]
print (arr2[:,0])  #
print (arr2[:,1])  #
print (arr2[1,:])  #
print (arr2[1::2,:]) #



