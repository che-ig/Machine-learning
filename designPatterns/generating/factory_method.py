from __future__ import annotations
from abc import ABC, abstractmethod

class Dialog(ABC):
    '''
        Базовый класс создателя
    '''
    def work(self):
        btn = self.createButton()
        btn.render()

    '''
        Фабричный метод. 
        ОБЯЗАН бфть переопредеоенным субклассами
    '''
    @abstractmethod
    def createButton():
        pass

class IButton(ABC):
    '''
        Интерфейс продукта. В нашем случае  - кнопки интерфейса
    '''
    @abstractmethod
    def render():
        pass

class WindowButton(IButton):
    '''
        Конкретный продукт. 
        Субкласс конкретной кнопки под windows
    '''
    def render(self):
        print('render windows button') 

class LinuxButton(IButton):
    '''
        Конкретный продукт. 
        Субкласс конкретной кнопки под linux
    '''
    def render(self):
        print('render lunux button')

class WindowDailog(Dialog):
    '''
        Конкретный фабричный метод. 
        Создает конкретную кнопку под windows
    '''
    def createButton(self):
        return WindowButton()

class linuxDailog(Dialog):
    '''
        Конкретный фабричный метод. 
        Создает конкретную кнопку под linux
    '''
    def createButton(self):
        return LinuxButton()

def client_code(creator):
    '''
        Испльзем метод базового класса, не беспокоясь о создании
        конкретных конкретных кнопок под разные ОС.
    '''
    creator.work()
    
if __name__ == '__main__':
    typeButton = input('Ведите win или lunux ')
    '''
        Создаем конкретные фабрими для требуемых операционных систем
    '''
    if typeButton == 'win':
        dialog = WindowDailog()
    else:
        dialog = linuxDailog()

    # Созданную фабрику передаем в клиентский код
    client_code(dialog)