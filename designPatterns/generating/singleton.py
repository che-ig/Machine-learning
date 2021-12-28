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
    def some_business_logic(self: Singleton) -> None:
        """Наконец, любой одиночка должен содержать некоторую бизнес-логику."""
        """Которая может быть выполнена на его экземпляре."""

        # ...


if __name__ == "__main__":
    # Клиентский код.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
