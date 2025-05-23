'''
#imporitng of  all meber of a module
import modulespython  # importing modules in this file
modulespython.myfunction1(10) # accessing function with module name
modulespython.myfunction2(10,20)
modulespython.myfunction1(30)


# for specfic member access of any module

from modulespython import myfunction1
myfunction1(12)
from modulespython import myfunction2
myfunction2(12,23)


# access all member access of any module

from modulespython import *
myfunction2(13,45)
myfunction1(34)

'''
import mymodule
from mymodule import myfunction2
from modulespython import myfunction2
mymodule.myfunction2(28,34)
myfunction2(20,34)

# module name aliasing
import mymodule as mylib # mylib is nickname of mymodule
mylib.myfunction2(12,34)

#import sys
print(sys.argv)