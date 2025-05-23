class Product:
    def __init__(self,pid,name,ptype,price):
        self.__pid=pid
        self.__name=name
        self.__ptype=ptype
        self.price=price
    def __str__(self):
        return "{:<10}{:<15}{:<10}{:<10}".format(self.__pid,self.__name,self.__ptype,self.__price)

class Shop():
    def addProduct(self):
        list=[self]
        for i in range(3):
            list={
            x = input("Enter product Id:")
            y = input("Enter product Name:")
            z = input("Enter product Type:")
            k = input("Enter product Price:")
            print("Enter product ",i+1,"details:")
            }

            products.append(p)
        return products
    def viewProduct(self,pid,name,ptype,price):
        products=[]
        for i in range(3):
            print(products[self,pid,name,ptype,price])



shop=Shop()
shop.addProduct()

shop.viewProduct(x,y,z,k)
print(products)


