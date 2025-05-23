mylist1=[10,20,30,40,50,60,70,80,90,100] #list with some initial data
print(mylist1)
'''
mylist2=list()  #it will create an empty list object
print(mylist2)

mylist3=[]    #it will also create an empty list object
print(mylist3)

print(mylist1[0]) #normal indexing 0 to size-1
print(mylist1[-10]) #reverse indexing starts from -1
print(mylist1[9]) #indexing 0 to size-1
print(mylist1[-1]) #reverse indexing starts from -1
'''
'''
print("List items:")
for item in mylist1:
    print(item,end=" ")

#list slicing

print("\nslicing")
print("mylist1[1:4]=>",mylist1[1:4])
print("mylist1[:4]=>",mylist1[:4])
print("mylist1[4:]=>",mylist1[4:])
print("mylist1[::-1]=>",mylist1[::-1])
'''
mylist1.append(15)
mylist1.append(45)
mylist1.append(150)
print("After append")
print(mylist1)
mylist1.insert(3,35)
mylist1.insert(5,55)
mylist1.insert(7,55)
mylist1.insert(9,55)
print("After insert")
print(mylist1)
print("frequency of 55 in list:",mylist1.count(55))

print("first occurence index of 55:",mylist1.index(55)) #5
print("second occurence index of 55:",mylist1.index(55,6))
mylist1.pop(0)  #will remove 0th index value if index 0 exists
#mylist1.remove(500)
mylist1.remove(55) #will remove 55 from list if exists
print("Updated list:",mylist1)
#mylist1.clear()
#print(mylist1)
mylist1.reverse()
print("Reverse List:")
print(mylist1)
#mylist1.sort() # will sort in ascending order,default nature
mylist1.sort(reverse=True) # will sort in descending order
print("Sorted List:")
print(mylist1)
#mylist1.append([5,8,20])
mylist1.extend([5,8,20])
print("updated list:")
print(mylist1)

#nesting of list(list with list)
mylist = ["CDAC", [1, 2, 3, 4, 5], [6, 7, 8, 9]]
print(mylist[0]) #"CDAC"
print(mylist[1]) #[1, 2, 3, 4, 5]
print(mylist[2])

print(mylist[1][3]) #4







