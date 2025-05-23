# question no 2.
#by function calling
lt=[1,2,3,4]
def mullist(mylist):
    result=1
    for x in mylist:
        result = result * x
    return result
print(mullist(lt))