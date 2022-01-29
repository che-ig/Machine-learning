"""Паттерн цепочка обязанностей."""

from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum


class TypeRequest(Enum):
    """Перечисление возможных запросов."""

    WORK = "work"
    PERSONNAL = "personal"
    COMMON = "common"


class IHandler(ABC):
    """Интерфейс обработчика цепочки обязанностей."""

    @abstractmethod
    def handle(self: IHandler, request: Request) -> None:
        """Метод обработки запроса."""
        pass


class Request():
    """Класс запроса."""

    """Т.е это и есть запрос который пойдет по цепочке обязанностей в надежде,
    что его кто-нибудь обработает."""

    def __init__(self: Request, name: str, type_request: TypeRequest) -> None:
        """Инициализация обьекта запроса."""
        self.name = name
        self._type_request = type_request

    @property
    def type_requst(self: Request) -> None:
        """Геттер для получения типа запроса."""
        return self._type_request

    @type_requst.setter
    def type_request(self: Request, type_request: TypeRequest) -> None:
        """Сеттер для установления типа запроса."""
        self._type_request = type_request


class AbstractHandler(IHandler):
    """Абстрактный класс обработчика запроса."""

    """Поведение цепочки по умолчанию может быть реализовано внутри базового класса
        обработчика."""

    def __init__(self: AbstractHandler, handler: AbstractHandler = None) -> None:
        """Иницаализация объекта обработчика запроса."""
        self._next_handler = handler

    @property
    def handler(self: AbstractHandler) -> IHandler:
        """Получаем следующий обработчик для запроса."""
        return self._next_handler

    @handler.setter
    def handler(self: AbstractHandler, handler: IHandler) -> None:
        """Устанавливаем следующий обработчик для запроса."""
        self._next_handler = handler

    @abstractmethod
    def check_request(self: AbstractHandler) -> None:
        """Метод проверяет подходит ли переданный объект для обработки текущим обработчиком И ОБРАБАТЫВАЕТ ЕГО."""
        pass

    def handle(self:  AbstractHandler, request: Request) -> None:
        """Метод обработки запроса."""
        """Если запрос не прошел проверку, то передаем его следующему обработчику в цепочке обязанностей."""

        result = self.check_request(request)
        # Если запрос не был обработан и есть куда передавать запрос, то передаем.
        if not result and self._next_handler:
            self._next_handler.handle(request)

# Типовые классы различных типов получателей запроса, т.е те кто в принципе может
# получить запрос на обработку. Обрабатывает запрос сам (если зпрос относится к его обязанностям)
# либо отдает дальше по цепочке.


class ReceiverWork(AbstractHandler):
    """Класс для обработки запроса типа - WORK."""

    def __init__(self: ReceiverWork, handler: AbstractHandler = None) -> None:
        """Метод инициализации объекта ReceiverWork."""
        self._next_handler = handler

    def check_request(self: ReceiverWork, request: Request) -> bool:
        """Метод для проверки и обработки запроса типа - WORK."""
        check = request.type_requst == TypeRequest.WORK
        if check:
            print(f"Приступаем к обработке запроса типа {TypeRequest.WORK}")
        else:
            print("Запрос перается следующему обработчику")
        return check


class ReceiverPersonal(AbstractHandler):
    """Класс для обработки запроса типа - PERSONNAL."""

    def __init__(self: ReceiverPersonal, handler: AbstractHandler = None) -> None:
        """Метод инициализации объекта PERSONNAL."""
        self._next_handler = handler

    def check_request(self: ReceiverPersonal, request: Request) -> bool:
        """Метод для проверки и обработки запроса типа - PERSONNAL."""
        check = request.type_requst == TypeRequest.PERSONNAL
        if check:
            print(f"Приступаем к обработке запроса типа {TypeRequest.PERSONNAL}")
        else:
            print("Запрос перается следующему обработчику")
        return check


class ReceiverCommon(AbstractHandler):
    """Класс для обработки запроса типа - COMMON."""

    def __init__(self: ReceiverCommon, handler: AbstractHandler = None) -> None:
        """Метод инициализации объекта COMMON."""
        self._next_handler = handler

    def check_request(self: ReceiverCommon, request: Request) -> bool:
        """Метод для проверки и обработки запроса типа - COMMON."""
        check = request.type_requst == TypeRequest.COMMON
        if check:
            print(f"Приступаем к обработке запроса типа {TypeRequest.COMMON}")
        else:
            print("Запрос перается следующему обработчику")
        return check


def test_chain(receiver: AbstractHandler, request: Request) -> None:
    """Тестовая функция для отладки."""
    print(f"Обработка запроса {request.type_requst}")
    receiver.handle(request)


if __name__ == "__main__":
    work = ReceiverWork()
    person = ReceiverPersonal(work)
    common = ReceiverCommon()
    common.handler = person

    request_common = Request('common', TypeRequest.COMMON)
    request_worker = Request('worker', TypeRequest.WORK)
    request_personal = Request('personal', TypeRequest.PERSONNAL)

    test_chain(work, request_common)
    test_chain(common, request_personal)
