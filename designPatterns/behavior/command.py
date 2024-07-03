"""Модуль, реализующий паттерн - Команда."""

from __future__ import annotations

from abc import ABC, abstractmethod


class ICommand(ABC):
    """Интерфейс Команды объявляет метод для выполнения команд."""

    @abstractmethod
    def execute(self: ICommand) -> None:
        """Метод для работы со стронними классами."""
        """Метод который будет выполнять основную работу по взаимодействию
        со сторонними классами."""

        pass


class TV:
    """Класс получатель (телевизор)."""

    """Функционал данного класса будет испльзоваться в команде"""

    def on(self: TV) -> None:
        """Метод включения телевизора."""
        print("Включение телевизора")

    def off(self: TV) -> None:
        """Метод выключения телевизора."""
        print("Выключение телевизора")


class VacuumCleaner:
    """Класс получатель (пылесос)."""

    """Функционал данного класса будет испльзоваться в команде"""

    def wash(self: VacuumCleaner) -> None:
        """Метод запускает мытье пола."""
        print("Моем пол")

    def clean(self: VacuumCleaner) -> None:
        """Метод запускает чистку пола."""
        print("Чистим пол")


class TvOnCommand(ICommand):
    """Команда, отвечающая ТОЛЬКО за включение телевизора."""

    def __init__(self: TvOnCommand, receiver: TV) -> None:
        """Инициализируем команду."""
        """Передаем объект, методы которого будут испльзоваться в методе execute"""
        self._receiver = receiver

    def execute(self: TvOnCommand) -> None:
        """Метод для работы с TV."""
        self._receiver.on()


class WashAndCleanCommand(ICommand):
    """Команда, отвечающая ТОЛЬКО за мытье и чистку пола при помощи пылесоса."""

    def __init__(self: WashAndCleanCommand, receiver: VacuumCleaner) -> None:
        """Инициализируем команду."""
        """Передаем объект, методы которого будут испльзоваться в методе execute"""
        self._receiver = receiver

    def execute(self: WashAndCleanCommand) -> None:
        """Метод для работы с VacuumCleaner."""
        self._receiver.wash()
        self._receiver.clean()


class Invoker:
    """Класс инициатор."""

    """Формирует команды"""

    tv = TV()
    vacuum = VacuumCleaner()

    tv_on = TvOnCommand(tv)
    vacuum_cleaner = WashAndCleanCommand(vacuum)

    def turn_on_tv(self: Invoker) -> None:
        """Метод для включения телевизора."""
        self.tv_on.execute()

    def working_vacuum_cleaner(self: Invoker) -> None:
        """Метод для включения пылесоса."""
        self.vacuum_cleaner.execute()


if __name__ == "__main__":
    invoker = Invoker()
    invoker.turn_on_tv()
    invoker.working_vacuum_cleaner()
