from __future__ import annotations
from abc import ABC, abstractmethod

class IAbstractFactory(ABC):
    @abstractmethod
    def createProduct_A():
        pass

    @abstractmethod
    def createProduct_B():
        pass

class IProduct_A(ABC):
    @abstractmethod
    def do():
        pass
class IProduct_B(ABC):
    @abstractmethod
    def run():
        pass


class Product_A_1(IProduct_A):
    def do(self):
        return 'do from Product_A_1'

class Product_A_2(IProduct_A):
    def do(self):
        return 'do from Product_A_2'

class Product_B_1(IProduct_B):
    def run(self):
        return 'run from Product_B_1'

class Product_B_2(IProduct_B):
    def run(self):
        return 'run from Product_B_2'
class FactoryOne(IAbstractFactory):
    def createProduct_A(self):
        return Product_A_1()

    def createProduct_B(self):
        return Product_B_1()

class FactoryTwo(IAbstractFactory):
    def createProduct_A(self):
        return Product_A_2()
        
    def createProduct_B(self):
        return Product_B_2()

def client_code(factory):
    prod_A = factory.createProduct_A()
    prod_B = factory.createProduct_B()
    print(prod_A.do())
    print(prod_B.run())


if __name__ == '__main__':
    factoryType = input('Введите one или two ')

    if factoryType == 'one':
        factory = FactoryOne()
    else:
        factory  = FactoryTwo()
    
    client_code(factory)
        