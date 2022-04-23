"""Модуль, реализующий паттерн итеротор."""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import List


class PizzaItem:
    """Кусок питцы."""
    def __init__(self: PizzaItem, number: int) -> None:
        """Задаем номер куска пиццы."""
        self.number = number

    def __str__(self: PizzaItem) -> str:
        """Выводим номер куска пиццы."""
        return f"кусочек пиццы под номером: {self.number}"


class PizzaSliceIterator(Iterator):
    """Класс итератор."""
    def __init__(self: PizzaSliceIterator,
                 pizza: List[PizzaItem],
                 reverse: bool = False) -> None:
        """Инициализируем итератор."""
        self._pizza = pizza
        self._index: int = -1 if reverse else 0
        self._reverse = reverse

    def __next__(self: PizzaSliceIterator) -> PizzaItem:
        """Метод обхода коллекции."""
        """Этот метод обязан быть реализован т.к мы отнаслеловались от Iterator"""
        try:
            pizza_item = self._pizza[self._index]
            self._index += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return pizza_item


class PizzaAggregate(Iterable):
    def __init__(self: PizzaAggregate, amount_slices: int = 10) -> None:
        self._slices = [PizzaItem(it + 1) for it in range(amount_slices)]
        print(f"Приготовили пиццу и порезали " f"на {amount_slices} кусочков")

    def amount_slices(self: PizzaAggregate) -> int:
        """Выводим количество кусков питццы."""
        return len(self._slices)

    def get_reverse_iterator(self: PizzaAggregate) -> PizzaSliceIterator:
        """Метод для обратного прохода по коллекции."""
        return PizzaSliceIterator(self._slices, True)

    def __iter__(self: PizzaAggregate) -> PizzaSliceIterator:
        """Метод возвращает объект типа Iterator."""
        """Данный метод обязан быть реализован т.к мы отнаследовались
            от Iterable. Также метод ОБЯЗАН возвращать объект типа Iterator."""
        return PizzaSliceIterator(self._slices)


if __name__ == "__main__":
    pizza = PizzaAggregate(5)
    for item in pizza:
        print("Это " + str(item))
    print("*" * 8 + "Обход в обратную сторону" + "*" * 8)
    iterator = pizza.get_reverse_iterator()
    for item in iterator:
        print("Это " + str(item))
