from __future__ import annotations

from abc import ABC, abstractmethod


class Dialog(ABC):
    '''Базовый класс создателя.'''
    def work(self):
        btn = self.create_button()
        btn.render()

    @abstractmethod
    def create_button():
        """Фабричный метод."""

        """ОБЯЗАН быть переопределенным субклассами"""
        pass


class IButton(ABC):
    """Интерфейс продукта. В нашем случае  - кнопки интерфейса."""
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
    def create_button(self) -> IButton:
        return WindowButton()


class LinuxDailog(Dialog):
    '''
        Конкретный фабричный метод.
        Создает конкретную кнопку под linux
    '''
    def create_button(self) -> IButton:
        return LinuxButton()


def client_code(creator):
    '''
        Испльзем метод базового класса, не беспокоясь о создании
        конкретных конкретных кнопок под разные ОС.
    '''
    creator.work()


if __name__ == '__main__':
    type_button = input('Ведите win или lunux ')
    '''
        Создаем конкретные фабрими для требуемых операционных систем
    '''
    if type_button == 'win':
        dialog = WindowDailog()
    else:
        dialog = LinuxDailog()

    # Созданную фабрику передаем в клиентский код
    client_code(dialog)
