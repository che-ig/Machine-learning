from __future__ import annotations

from abc import ABC, abstractmethod


class State(ABC):
    """
        Интерфейс состояний. Все состояния должны реализовать абстрактные методы
    """
    @abstractmethod
    def insert_quarter(self):
        pass

    @abstractmethod
    def eject_quarter(self):
        pass

    @abstractmethod
    def turn_crank(self):
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

    def insert_quarter(self):
        print('Вы уже ввели моненту. Вторую ввести нельзя')

    def eject_quarter(self):
        print('Заберите свою монетку.')
        self._machine.set_count(self._machine.get_no_quarter_state())

    def turn_crank(self):
        print('Подождите')
        self._machine.set_count(self._machine.get_sold_state())

    def give(self):
        print('Жевачка не выдана (она выдается в состояни sold)')


class NoQuarter(State):
    """
        Состояние отсутствия монетки в автомате
    """
    def __init__(self, machine: GumMachine):
        self._machine = machine

    def insert_quarter(self):
        print('Вы ввели монетку')
        self._machine.set_count(self._machine.get_has_quarter_state())

    def eject_quarter(self):
        print('Сначала вставьте монетку')

    def turn_crank(self):
        print('Сначала вставьте монетку, а потом дергайте за рычаг')

    def give(self):
        print('Жевачка выдается только за монетку')


class Sold(State):
    """
        Состояние когда жевачка уже продана и вскоре будет выдана покупателю
    """
    def __init__(self, machine: GumMachine):
        self._machine = machine

    def insert_quarter(self):
        print('Подождите выдачи жевачки')

    def eject_quarter(self):
        print('На этом этапе возврат невозможен')

    def turn_crank(self):
        print('Вы уже дернули за рычаг')

    def give(self):
        self._machine.release_gum()
        if self._machine.get_count() > 0:
            self._machine.set_count(self._machine.get_no_quarter_state())
        else:
            self._machine.set_count(self._machine.get_sold_out_state())


class SoldOUt(State):
    """
        Состояние пустого автомата.
    """
    def __init__(self, machine: GumMachine):
        self._machine = machine

    def insert_quarter(self):
        print('Все жевачки проданы')

    def eject_quarter(self):
        print('Вы не вставили монетку')

    def turn_crank(self):
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

    # Геттеры для получения объектов конкретных состояний.
    # Чтобы обслабить связь между объектами состояний создаем геттеры.
    # Имея геттеры в контексте нам не приходится в каждом конкретном состоянии
    # обращаться к классам др. состояний. Все обращения происходят через контекст,
    # который передается в конструкторы каждого из состояний.

    def get_no_quarter_state(self):
        return self._noQuarterState

    def get_has_quarter_state(self):
        return self._hasQuarterState

    def get_sold_state(self):
        return self._soldState

    def get_sold_out_state(self):
        return self._soldOutState

    def set_count(self, state: State):
        """
            Метод смены состояния объекта
        """
        self._state = state

    def insert_quarter(self):
        self._state.insert_quarter()

    def eject_quarter(self):
        self._state.eject_quarter()

    def turn_crank(self):
        self._state.turn_crank()
        self._state.give()

    def release_gum(self):
        if self._count > 0:
            print('Выдана одна жевачка')
            self._count -= 1

    def get_count(self) -> int:
        return self._count


if __name__ == "__main__":
    machine = GumMachine(5)

    machine.turn_crank()
    machine.turn_crank()

    machine.insert_quarter()
    machine.turn_crank()
    machine.eject_quarter()

    machine.insert_quarter()
    machine.turn_crank()

    machine.insert_quarter()
    machine.turn_crank()

    machine.insert_quarter()
    machine.turn_crank()

    machine.insert_quarter()
    machine.turn_crank()

    machine.insert_quarter()
    machine.turn_crank()

    machine.insert_quarter()
    machine.turn_crank()
