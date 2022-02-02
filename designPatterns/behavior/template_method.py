"""Модуль, реализующий паттерн - Шаблонный метод."""

from abc import ABC, abstractmethod


class CaffeineBeverage(ABC):
    """
    Абстрактный Класс определяет шаблонный метод, содержащий скелет некоторого
    алгоритма, состоящего из вызовов (обычно) абстрактных примитивных операций.

    Конкретные подклассы должны реализовать эти операции, но оставить сам
    шаблонный метод без изменений.
    """
    def prepare_recipe(self):
        """
            Шаблонный метод определяет последовательность
            выполняемых операций.
         """
        self.boil_water()
        self.brew()
        self.add_condimets()
        self.pour_in_cup()

    # Метод обязан быть реализован субклассом
    @abstractmethod
    def add_condimets(self):
        pass

    # Метод обязан быть реализован субклассом
    @abstractmethod
    def brew(self):
        pass

    # Эти методы являются методами по умолчанию
    # и не нуждаются в переопределении. Но если субклассам
    # требется переопределение, то они могут это сделать.

    def boil_water(self):
        print('Кипятим воду')

    def pour_in_cup(self):
        print('Разливаем напиток')


class Tea(CaffeineBeverage):
    """
        Конкретные классы должны реализовать все абстрактные операции базового
        класса.
    """
    def brew(self):
        print("Заваривам чай")

    def add_condimets(self):
        print("Добавим сахар")


class Coffee(CaffeineBeverage):
    def brew(self):
        print("Варим кофе")

    def add_condimets(self):
        print("Добавим молоко")


if __name__ == "__main__":
    tea = Tea()
    res = tea.prepare_recipe()
