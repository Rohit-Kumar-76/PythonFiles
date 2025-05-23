'''
import  mymodule
mymodule.myfunction1(10)

mymodule.myfunction2(20,30)

mymodule.myfunction1(30)
'''
'''
#importing specific member of any module
from mymodule import myfunction1
myfunction1(50)
from  mymodule import myfunction2
myfunction2(40,50)
'''
#importing all members of any module
'''
from mymodule import  *
myfunction2(60,50)
myfunction1(70)
'''
from mymodule import myfunction2
#myfunction2(40,50)
import  mymodule
from  mymodule2 import myfunction2

myfunction2(50,60)
mymodule.myfunction2(40,50)

#module name aliasing
import mymodule as mylib
mylib.myfunction1(60)
mylib.myfunction2(60,30)

import  sys
print(sys.argv)












