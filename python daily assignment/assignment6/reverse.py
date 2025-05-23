# with function

def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1
num=input("Enter a string")
x=reverse_string(num)
print(x)
#print(len(x))

# normal approach
name=input("Enter a name:")

if(len(name)%4==0):
    print(name[::-1])
else:
    print(name)