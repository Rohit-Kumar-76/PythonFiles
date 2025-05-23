# question no 5.
mylist1=[10,20,30,40,50,60,70,80,90,100] #list with some initial data
mylist1=list(int(num) for num in input("enter space seprated list avlue:").split(" "))
print(mylist1)
if not mylist1:
    print('Empty list')
else:
    print('List is not Empty\n',mylist1)
