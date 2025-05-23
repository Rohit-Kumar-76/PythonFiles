import numpy as np

list1 = [[1,2,3],[3,4,5],[5,6,7]]
list2 = [[2,3,4],[3,5,4],[6,8,5]]
#creating 2D array using numpy
arr1 = np.array(list1)
arr2 = np.array(list2)

print (arr1)
print (arr2)
print("Matrics Sum:")
print (arr1+arr2)
print("Matrics Difference:")
print (arr1-arr2)
print("Matric Element by Multiplication:")
print (arr1*arr2)
print("Matric Multiplication:")
print (arr1.dot(arr2))
print("Matric Transpose:")
print (arr1.transpose())
print("+++++++++++++++++++++++++++++++++")
arr3 = np.array([1,2,3,4,5,6])
print (arr3**3)
print(arr1)
print(np.invert(arr1))
#print(np.invert(arr2).dot(arr1))
