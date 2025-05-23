#call by value
def myfun(x,y):
    x=x+10
    y=y+30
    print(x," , ",y) #30, 60

#function calling
a=20
b=30
myfun(a,b)
print(a," , ",b) #20  30

#call by refrence/Pass by object reference
'''
list=["Patna","Gaya","Madhubani","Noida"]
print(list)
list.append("Dharbhanga")
print(list)
list=["Lucknow","Agra"]
print(list)
'''
'''
def add_list(mylist):
    #list=["Mumbai"]
    mylist.append("Mumbai")
    #print(mylist)

mylist=["Delhi","Patna","Lucknow"]
print(mylist)
add_list(mylist)
print(mylist)
'''

#required/positional argument
def print_values(x,y,z):
    print(x,",",y,",",z)


#print_values(20,50) #invalid,bcz all three parameters are mandatory
print_values(30,40,50)

#default argumnet/optional argument
def message(id,fname,surname="singh",salary=25600):
    print("Welcome:",fname," ",surname)
    print("ID:",id,"\tSalary:",salary)

message(100,"admin","astric",24500)
message(101,"Vishal","Mahto")
message(102,"Vishal")

                     #named/keyword
message(103,"Vishal",salary=35600)





