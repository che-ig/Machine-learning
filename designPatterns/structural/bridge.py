from __future__ import annotations

from abc import ABC, abstractmethod


class IImplementation(ABC):
    """
        Реализация устанавливает интерфейс для всех классов реализации. Он не должен
        соответствовать интерфейсу Абстракции. На практике оба интерфейса могут быть
        совершенно разными. Как правило, интерфейс Реализации предоставляет только
        примитивные операции, в то время как Абстракция определяет операции более
        высокого уровня, основанные на этих примитивах.
    """
    @abstractmethod
    def operation_implementation(self):
        pass


"""
    Каждая Конкретная Реализация соответствует определённой платформе и реализует
    интерфейс Реализации с использованием API этой платформы.
"""


class ConcreateImplementationA(IImplementation):
    def operation_implementation(self):
        return "operation_implementation from ConcreateImplementation_A"


class ConcreateImplementationB(IImplementation):
    def operation_implementation(self):
        return "operation_implementation from ConcreateImplementation_B"


class Abstraction:
    """
        Абстракция устанавливает интерфейс для «управляющей» части двух иерархий
        классов. Она содержит ссылку на объект из иерархии Реализации и делегирует
        ему всю настоящую работу.
    """
    def __init__(self, implementation: IImplementation):
        self._implementation = implementation

    def operation(self):
        print(f"{self.__class__.__name__} {self._implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):
    """
        Можно расширить Абстракцию без изменения классов Реализации.
    """
    def operation(self):
        print(f"{self.__class__.__name__} {self._implementation.operation_implementation()}")


def client_code(abstraction: Abstraction):
    """
        За исключением этапа инициализации, когда объект Абстракции связывается с
        определённым объектом Реализации, клиентский код должен зависеть только от
        класса Абстракции. Таким образом, клиентский код может поддерживать любую
        комбинацию абстракции и реализации.
    """
    abstraction.operation()


if __name__ == "__main__":
    implementation = ConcreateImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    implementation = ConcreateImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)
