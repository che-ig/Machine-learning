"""Паттерн проектирования синголтон."""

from __future__ import annotations


class SingletonMeta(type):
    """В Python класс Одиночка можно реализовать по-разному."""

    """ Возможные способы
        включают себя базовый класс, декоратор, метакласс. Мы воспользуемся
        метаклассом, поскольку он лучше всего подходит для этой цели.
    """
    _instances = {}

    def __call__(cls: SingletonMeta, *args, **kwargs):
        """Данная реализация не учитывает возможное изменение передаваемых аргументов в `__init__`."""
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """Класс одиночка с использованием метакласса."""

    def some_business_logic(self: Singleton) -> None:
        """Наконец, любой одиночка должен содержать некоторую бизнес-логику."""
        """Которая может быть выполнена на его экземпляре."""

        # ...


class MySingleton():
    """Класс одиночка без использования метакласов."""

    _instance = None

    def __new__(cls: MySingleton, *args, **kwargs) -> MySingleton:
        """Создаем экземпляр класса."""
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self: MySingleton, age: int) -> None:
        """Инициализация экземпляра класса."""
        if not getattr(MySingleton._instance, 'age', None):
            self.age = age


if __name__ == "__main__":
    # Клиентский код.

    s1 = Singleton()
    s2 = Singleton()

    my_singleton_1 = MySingleton(25)
    my_singleton_2 = MySingleton(35)
    print(my_singleton_1.age, my_singleton_2.age)

    if id(my_singleton_1) == id(my_singleton_2):
        print("My singleton works!")

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
