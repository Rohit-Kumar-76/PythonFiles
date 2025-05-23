print("fun(1)")
#sorted() function
mylist1=['r','e','h','a','q']
ml=sorted(mylist1) # it arrange the value in asending order
print(ml)
print("\n")
print("fun(2)")
#abs() function
#x = abs(3+5j)
x = abs(-7.25)  # abs() function return the absulute value of the value or remove the negative sing
print(x)
print("\n")
print("fun(3)")
# all() function
# all() fucntion is use to cheak all variable are true or false
mylist = [True, True, True]
mylist = [1, 1, 1] # in list
mytuple = (0, True, False)# in tuple
x = all(mytuple)
print(x)
x = all(mylist)
print(x)

myset = {0, 1, 0}# in a set
x = all(myset)
print(x)
#all() fucntion
mydict = {0 : "Apple", 1 : "Orange"}# in dictionary
x = all(mydict)
print(x)
print("\n")
print("fun(4)")
#any() function
# this will give true if any value of list is true
x=any(mylist)# in list
print(x)
mytuple = (0, 1, False)
x = any(mytuple)# in tuple
print(x)

myset = {0, 1, 0}# in set
x = any(myset)
print(x)
print("\n")
print("fun(5)")
 # bin() function
 # is will give binary value of numbers
x = bin(36) # number to binary
print(x)
#hex() function
# it will convert not to hexa decimal n
x = hex(255)# number to hexa decimal
print(x)
print("\n")
print("fun(6)")
# oct() function
# it will convert number to octal form
x=oct(12)
print(x)# it will produce 0o prefix
print("\n")
print("fun(7)")
#chr() function
#it is string unicode of alphabets ,digit
x = chr(97)# this is string of 'a'
print(x)
x = chr(67)# it will give upper case "A"
print(x)
print("\n")
print("fun(8)")
#ord() function
# it will return unicode
x = ord("h")# it will give a unicode of 'h'
print(x)
x = ord("A")# it will give unicode of "A"
print(x)
print("\n")
print("fun(9)")
#divmod() function
# it will give divisor or remender of argument1 and argument2
x = divmod(10, 3)# it will give (3 ,1), 3 is divisor and 1 is remainder
print(x)
#div() function