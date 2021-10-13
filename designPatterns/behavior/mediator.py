from __future__ import annotations
from enum import Enum
from abc import ABC, abstractmethod

class Events(Enum):
    CLICK = "click"
    DOUBLECLICK ="doubleclick"
    HOVER = "hover"
class IMediator(ABC):
    """ 
        Интерфейс посредника (медиатора) определяем метод по средствам которого компоненты
        будут оповещать посредника о своих событиях.
        Посредник может реагировать на события и передавать исполение др. компонентам.
    """
    @abstractmethod
    def notify(self, sender: object, event: Events):
        pass

class ConcreateMediator(IMediator):
    def __init__(self, comp_a: Component_A, comp_b: Component_B):
        self._component_a = comp_a
        self._component_a.mediator = self
        self._component_b = comp_b
        self._component_b.mediator = self

    def notify(self, sender: object, event: Events):
        if type(sender) is Component_A:
            if event == Events.CLICK:
                print("кликнули по Component_A")
                self._component_b.operation_b()

class BaseComponent():
    """ 
        Базовый компонент обеспечивает минимальную функциональность и хранит экземпляр
        медиатора во внетреннем свойстве компонента.
    """
    def __init__(self, mediator: IMediator = None):
        self._mediator = mediator

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: IMediator):
        self._mediator = mediator
""" 
    Конкретные компоненты реализуют произвольную функциональность. Они никак не связаны между
    собой. Они так же не зависят ни от каких конкретных классов посредников, а зависят только
    от интерфейса посредника.
"""
class Component_A(BaseComponent):
    def active_a(self):
        print("Component_A does active_a")
        self.mediator.notify(self, Events.CLICK)

    def active_b(self):
        print("Component_A does active_b")
        self.mediator.notify(self, Events.HOVER)

class Component_B(BaseComponent):
    def operation_a(self):
        print("Component_A does operation_a")
        self.mediator.notify(self, Events.HOVER)

    def operation_b(self):
        print("Component_A does operation_b")

if __name__ == "__main__":
    comp_a = Component_A()
    comp_b = Component_B()
    mediator = ConcreateMediator(comp_a, comp_b)

    comp_a.active_a()