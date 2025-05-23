class Product:
    def __init__(self,pid,name,ptype,price):
        self.__pid=pid
        self.__name=name
        self.__ptype=ptype
        self.price=price
    def __str__(self):
        return "{:<10}{:<15}{:<10}{:<10}"\
                .format(self.__pid,self.__name,self.__ptype,self.__price)

class Shop:
    def addProduct(self):
        products=[]
        for i in range(3):
            print("Enter product ",i+1,"details:")
            p=Product(
                      input("Enter product Id:"),
                      input("Enter product Name:"),
                      input("Enter product Type:"),
                      input("Enter product Price:"),
                     )
            products.append(p)
        return products

shop=Shop()
products=shop.addProduct()
print(products)

