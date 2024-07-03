from abc import ABC, abstractmethod


class IBeverage(ABC):
    """
    Интерфейс базового класса
    """

    @abstractmethod
    def cost(self) -> float:
        pass


class ICondiment(IBeverage):
    """
    Интерфейс базового декоратора
    """

    @abstractmethod
    def description() -> str:
        pass


class Espresso(IBeverage):
    """
    Конкретный класс. Кофе эспрессщ
    """

    def __init__(self, cost):
        self._cost = cost

    def cost(self):
        return self._cost

    def description(self) -> str:
        return "Espresso"


class DarkRoast(IBeverage):
    """
    Конкретный класс. Черный кофе.
    """

    def __init__(self, cost: float):
        self._cost = cost

    def cost(self):
        return self._cost

    def description(self) -> str:
        return "Black Coffee"


class Milk(ICondiment):
    """
    Декоратор добавляет молоко в напиток
    """

    def __init__(self, beverage: IBeverage, cost: float):
        self._beverage = beverage
        self._cost = cost

    def cost(self):
        return self._cost + self._beverage.cost()

    def description(self):
        return f"{self._beverage.description()} with Milk"


class Whip(ICondiment):
    """
    Декоратор добавляет взбитую пенку
    """

    def __init__(self, beverage: IBeverage, cost: float):
        self._beverage = beverage
        self._cost = cost

    def cost(self):
        return self._cost + self._beverage.cost()

    def description(self):
        return f"{self._beverage.description()} with Whip"


if __name__ == "__main__":
    espresso = Espresso(10)
    espresso = Milk(espresso, 5)
    espresso = Whip(espresso, 3)

    cost_esspresso = espresso.cost()
    description_esspresso = espresso.description()
    print(cost_esspresso, description_esspresso)
