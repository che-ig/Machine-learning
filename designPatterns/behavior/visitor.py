"""Модуль реализует паттерн - Посетитель."""

from __future__ import annotations

from abc import ABC, abstractmethod


class IVistor(ABC):
    """
        Интерфейс посетителя (Visitor).
        Объявляет набор методов, соответстующих классам компонентов.
        Сигнатура метода посещения позволяет посетителю
        понять конкретный класс компонента, с которым он имеет дело.
    """
    @abstractmethod
    def visit_for_concrete_component_a(self, component: ConcreteComponentA):
        pass

    @abstractmethod
    def visit_for_concrete_component_b(self, component: ConcreteComponentB):
        pass


class IComponent(ABC):
    """
        Интерфейс компонента.
        Объявляет метод accept, принимающий объект типа IVistor.
    """
    @abstractmethod
    def accept(self, visitor: IVistor):
        pass


"""
    Каждый конкретный компонент обязан реализовать метод accept так, чтобы внутри
    этого метода был вызов метода посетителя, соответстующего классу компонента.
"""


class ConcreteComponentA(IComponent):
    def __init__(self, weight: int):
        self._weight = weight

    def accept(self, visitor: IVistor):
        """
            Конкретный компонент должен знать какой метод посетиля необходимо вызвать,
            чтобы он подходил под текущий тип компонента.
        """
        visitor.visit_for_concrete_component_a(self)

    def get_weight(self):
        return self._weight

    def special_method_of_concreate_component_a_1(self):
        return "result from special_method_a_1"

    def special_method_of_concreate_component_a_2(self):
        return "result from special_method_a_2"


class ConcreteComponentB(IComponent):
    def __init__(self, length: int, mass: int):
        self._length = length
        self._mass = mass

    def accept(self, visitor: IVistor):
        visitor.visit_for_concrete_component_b(self)

    def get_length(self):
        return self._length

    def get_mass(self):
        return self._mass

    def special_method_of_concreate_component_b_1(self):
        return "result from special_method_b_1"

    def special_method_of_concreate_component_b_2(self):
        return "result from special_method_b_2"


# Конкретные посетители реализуют для каждого типа компонента свою реализацию поведения.


class ConcreteVisitorCalculateMass(IVistor):
    def visit_for_concrete_component_a(self, component: ConcreteComponentA):
        result = component.get_weight()
        print(f"Объект веслит {result * 0.45} фунта")

    def visit_for_concrete_component_b(self, component: ConcreteComponentB):
        result = component.get_mass()
        print(f"Объект веслит {result / 1000} тонн")


class ConcreteVisitorLength(IVistor):
    def visit_for_concrete_component_a(self, component: ConcreteComponentA):
        pass

    def visit_for_concrete_component_b(self, component: ConcreteComponentB):
        result = component.get_length()
        print(f"Объект имеет длину {result / 10} дециметров")


if __name__ == "__main__":
    visitors = [ConcreteVisitorCalculateMass(), ConcreteVisitorLength()]
    componetns = [ConcreteComponentA(200), ConcreteComponentB(250, 300)]

    for vis in visitors:
        for comp in componetns:
            comp.accept(vis)

