from __future__ import annotations

from abc import ABC, abstractmethod


class IAbstractFactory(ABC):
    @abstractmethod
    def create_product_a():
        pass

    @abstractmethod
    def create_product_b():
        pass


class IProductA(ABC):
    @abstractmethod
    def do():
        pass


class IProductB(ABC):
    @abstractmethod
    def run():
        pass


class ProductA1(IProductA):
    def do(self):
        return 'do from ProductA1'


class ProductA2(IProductA):
    def do(self):
        return 'do from ProductA2'


class ProductB1(IProductB):
    def run(self):
        return 'run from ProductB1'


class ProductB2(IProductB):
    def run(self):
        return 'run from ProductB2'


class FactoryOne(IAbstractFactory):
    def create_product_a(self):
        return ProductA1()

    def create_product_b(self):
        return ProductB1()


class FactoryTwo(IAbstractFactory):
    def create_product_a(self):
        return ProductA2()

    def create_product_b(self):
        return ProductB2()


def client_code(factory):
    prod_a = factory.create_product_a()
    prod_b = factory.create_product_b()
    print(prod_a.do())
    print(prod_b.run())


if __name__ == '__main__':
    factory_type = input('Введите one или two ')

    if factory_type == 'one':
        factory = FactoryOne()
    else:
        factory = FactoryTwo()

    client_code(factory)
