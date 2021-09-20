from __future__ import annotations
from abc import ABC, abstractmethod


class State(ABC):
    """ 
        Интерфейс состояний. Все состояния должны реализовать абстрактные методы
    """
    @abstractmethod
    def insertQuarter(self):
        pass

    @abstractmethod
    def ejectQuarter(self):
        pass

    @abstractmethod
    def turnCrank(self):
        pass

    @abstractmethod
    def give(self):
        pass
class HasQuarter(State):
    """ 
        Состояние когда клиент ввел моентку в автомат
    """
    def __init__(self, machine: GumMachine):
        self._machine = machine

    def insertQuarter(self):
        print('Вы уже ввели моненту. Вторую ввести нельзя')

    def ejectQuarter(self):
        print('Заберите свою монетку.')
        self._machine.setState(self._machine.getNoQuarterState())
    
    def turnCrank(self):
        print('Подождите')
        self._machine.setState(self._machine.getSoldState())

    def give(self):
        print('Жевачка не выдана (она выдается в состояни sold)')

class NoQuarter(State):
    """ 
        Состояние отсутствия монетки в автомате
    """
    def __init__(self, machine: GumMachine):
        self._machine = machine

    def insertQuarter(self):
        print('Вы ввели монетку')
        self._machine.setState(self._machine.getHasQuarterState())

    def ejectQuarter(self):
        print('Сначала вставьте монетку')

    def turnCrank(self):
        print('Сначала вставьте монетку, а потом дергайте за рычаг')

    def give(self):
        print('Жевачка выдается только за монетку')

class Sold(State):
    """ 
        Состояние когда жевачка уже продана и вскоре будет выдана покупателю
    """
    def __init__(self, machine: GumMachine):
        self._machine = machine

    def insertQuarter(self):
        print('Подождите выдачи жевачки')

    def ejectQuarter(self):
        print('На этом этапе возврат невозможен')

    def turnCrank(self):
        print('Вы уже дернули за рычаг')

    def give(self):
        self._machine.releaseGum()
        if self._machine.getCount() > 0:
            self._machine.setState(self._machine.getNoQuarterState())
        else:
            self._machine.setState(self._machine.getSoldOutState())

class SoldOUt(State):
    """ 
        Состояние пустого автомата.
    """
    def __init__(self, machine: GumMachine):
        self._machine = machine

    def insertQuarter(self):
        print('Все жевачки проданы')

    def ejectQuarter(self):
        print('Вы не вставили монетку')

    def turnCrank(self):
        print('В автомате нет жевачки')

    def give(self):
        print('Жевачка не выдана т.к автомат пуст')

class GumMachine:
    """ 
        Класс аппарата с жевачкой. Это класс контекста, который 
        делегирует вызовы клиента объектам состояний.
    """
    def __init__(self, count: int):
        self._count = count
        self._noQuarterState = NoQuarter(self)
        self._hasQuarterState = HasQuarter(self)
        self._soldState = Sold(self)
        self._soldOutState = SoldOUt(self)
        self._state = self._noQuarterState
        if not count:
            self._state = self._soldOutState

    """
        Геттеры для получения объектов конкретных состояний.
        Чтобы обслабить связь между объектами состояний создаем геттеры.
        Имея геттеры в контексте нам не приходится в каждом конкретном состоянии
        обращаться к классам др. состояний. Все обращения происходят через контекст,
        который передается в конструкторы каждого из состояний.
    """
    def getNoQuarterState(self):
        return self._noQuarterState

    def getHasQuarterState(self):
        return self._hasQuarterState

    def getSoldState(self):
        return self._soldState

    def getSoldOutState(self):
        return self._soldOutState
    
    """ 
        Метод смены состояния объекта
    """
    def setState(self, state: State):
        self._state = state
    
    def insertQuarter(self):
        self._state.insertQuarter()

    def ejectQuarter(self):
        self._state.ejectQuarter()

    def turnCrank(self):
        self._state.turnCrank()
        self._state.give()

    def releaseGum(self):
        if self._count > 0:
            print('Выдана одна жевачка')
            self._count -=1

    def getCount(self) -> int:
        return self._count        

if __name__ == "__main__":
    machine = GumMachine(5)

    machine.turnCrank()
    machine.turnCrank()

    machine.insertQuarter()
    machine.turnCrank()
    machine.ejectQuarter()

    machine.insertQuarter()
    machine.turnCrank()

    machine.insertQuarter()
    machine.turnCrank()

    machine.insertQuarter()
    machine.turnCrank()

    machine.insertQuarter()
    machine.turnCrank()

    machine.insertQuarter()
    machine.turnCrank()

    machine.insertQuarter() 
    machine.turnCrank()