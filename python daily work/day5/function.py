def add(x,y):
    z=x+y
    return z

def sub():
    n=20
    b=45
    return b-n
#without return with parameter
def mul(x,y):
    mulity=x*y
    print("mul=",mulity)

if  __name__=="__main__":
    result=add(20,34)
    print("sum=",result)
    print("sum=",add(30,67))
    num1=24
    num2=56
    #without return
    print("sum=",add(num1,num2))
    #with return value without parameter
    print("sub=", sub())
    mul(4,6)




