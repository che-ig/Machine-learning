from __future__ import annotations

from abc import ABC, abstractmethod


class IComponent(ABC):
    """
    Базовый класс Компонент объявляет общие операции как для простых, так и для
    сложных объектов структуры.
    """

    @property
    def parent(self) -> IComponent:
        return self._parent

    @parent.setter
    def parent(self, parent: IComponent):
        self._parent = parent

    # Методы присущие контейнерам элементов

    def add(self):
        pass

    def remove(self):
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self):
        pass


class Leaf(IComponent):
    def __init__(self, cost: float):
        self._cost = cost

    def operation(self):
        return self._cost


class Composete(IComponent):
    def __init__(self):
        self._children: list[IComponent] = []

    def add(self, component: IComponent) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: IComponent) -> None:
        self._children.remove(object)
        component.parent = None

    def operation(self):
        cost = 0
        for item in self._children:
            cost += item.operation()
        return cost

    def is_composite(self) -> bool:
        return True


if __name__ == "__main__":
    leaf_1 = Leaf(10)
    leaf_2 = Leaf(20)
    leaf_3 = Leaf(30)
    leaf_4 = Leaf(40)
    leaf_5 = Leaf(50)

    composite = Composete()
    composite.add(leaf_1)
    composite.add(leaf_2)

    composite_2 = Composete()
    composite_2.add(leaf_3)
    composite_2.add(leaf_4)

    composite_3 = Composete()
    composite_3.add(leaf_5)
    composite_3.add(composite)
    composite_3.add(composite_2)

    total_cost = composite_3.operation()
    print(total_cost)
