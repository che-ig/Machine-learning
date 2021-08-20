from __future__ import annotations
from abc import ABC, abstractmethod

class ICommand(ABC):
    """
        Интерфейс Команды объявляет метод для выполнения команд.
    """
    @abstractmethod
    def execute(self):
        pass

class TV:
    """ 
        Класс получатель (телевизор).
        Класс чьи методы будут испльзоваться в команде
    """
    def on(self):
        print('Включение телевизора')

    def off(self):
        print('Выключение телевизора')

class VacuumCleaner:
    """ 
        Класс получатель (пылесос).
        Класс чьи методы будут испльзоваться в команде
    """
    def wash(self):
        print('Моем пол')
    
    def clean(self):
        print('Чистим пол')

class tvOnCommand(ICommand):
    """ 
        Конкретная команда, отвечающая ТОЛЬКО за включение телевизора
    """
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.on()

class washAndCleanCommand(ICommand):
    """ 
        Конкретная команда, отвечающая ТОЛЬКО за мытье и чистку пола при
        помощи пылесоса
    """
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.wash()
        self._receiver.clean()

class Invoker():
    """ 
        Класс инициатор. Формирует команды
    """
    tv = TV()
    vacuum = VacuumCleaner()

    tvOn = tvOnCommand(tv)
    vacuumCleaner = washAndCleanCommand(vacuum)

    def turnOnTV(self):
        self.tvOn.execute()
    
    def workingVacuumCleaner(self):
        self.vacuumCleaner.execute()


if __name__ == '__main__':
    invoker = Invoker()
    invoker.turnOnTV()
    invoker.workingVacuumCleaner()