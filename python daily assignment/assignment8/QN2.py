class product(object):
    def __init__(self,pid,pn,pt,pp):
        self.__pid=pid
        self.__pn=pn
        self.__pt=pt
        self.__pp=pp
    def __str__(self):(self):
        return "{:<10}{:<15}{:<10}{:<10}"\
            .format(self.__pid,self.__pn,self.__pt,self.__pp)
class shop:

    def addproduct(self):



