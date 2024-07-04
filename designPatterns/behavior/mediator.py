"""Модуль, реализующий паттерн - Посредник"""

from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum


class Events(Enum):
    CLICK = "click"
    DOUBLECLICK = "doubleclick"
    HOVER = "hover"


class IMediator(ABC):
    """Интерфейс посредника (медиатора)."""

    """Определяем метод по средствам которого компоненты будут оповещать посредника
    о своих событиях. Посредник может реагировать на события и передавать
    исполение др. компонентам."""

    @abstractmethod
    def notify(self: IMediator, sender: object, event: Events) -> None:
        pass


class ConcreateMediator(IMediator):
    def __init__(self: ConcreateMediator, comp_a: ComponentA, comp_b: ComponentB) -> None:
        self._component_a = comp_a
        self._component_a.mediator = self
        self._component_b = comp_b
        self._component_b.mediator = self

    def notify(self: ConcreateMediator, sender: object, event: Events) -> None:
        if type(sender) is ComponentA:
            if event == Events.CLICK:
                print("кликнули по ComponentA")
                self._component_b.operation_b()


class BaseComponent:
    """Базовый класс любого компонента, участвующего в паттерне посредник."""

    """ Базовый компонент обеспечивает минимальную функциональность и хранит экземпляр
        медиатора во внутреннем свойстве компонента."""

    def __init__(self: BaseComponent, mediator: IMediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self: BaseComponent):
        """Метод для получения объекта медиатора."""
        return self._mediator

    @mediator.setter
    def mediator(self: BaseComponent, mediator: IMediator) -> None:
        """Метод для установки медиатора."""
        self._mediator = mediator


# Конкретные компоненты реализуют произвольную функциональность. Они никак не связаны между
# собой. Они так же не зависят ни от каких конкретных классов посредников, а зависят только
# от интерфейса посредника.


class ComponentA(BaseComponent):
    """Комопонент-модель."""

    def action_a(self):
        """Некоторое действие _а компонента А"""
        print("ComponentA does action_a")
        self.mediator.notify(self, Events.CLICK)

    def action_b(self):
        """Некоторое действие _b компонента А"""
        print("ComponentA does action_b")
        self.mediator.notify(self, Events.HOVER)


class ComponentB(BaseComponent):
    """Компонент-модель."""

    def operation_a(self):
        """Некоторое действие _а компонента B"""
        print("ComponentB does operation_a")
        self.mediator.notify(self, Events.HOVER)

    def operation_b(self):
        """Некоторое действие _b компонента B"""
        print("ComponentB does operation_b")


if __name__ == "__main__":
    comp_a = ComponentA()
    comp_b = ComponentB()
    mediator = ConcreateMediator(comp_a, comp_b)

    comp_a.action_a()
