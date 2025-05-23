from abc import   ABC,ABCMeta ,abstractmethod

class Animal(ABC):
    __metaclass__=ABCMeta
    @abstractmethod
    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        print("meow meow meow")

class Dog(Animal):
    def talk(self):
        print("bhon bhon bhon")
#animal=Animal()  #not valid,bcz it's abstract
animal=Cat()
animal.talk()
animal=Dog()
animal.talk()

