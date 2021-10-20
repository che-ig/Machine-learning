from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum


class TypeRequest(Enum):
    WORK = "work"
    PERSONNAL = "personal"
    COMMON = "common"


class IHandler(ABC):
    """
        Интерфейс обработчика цепочки обязанностей.
    """
    @abstractmethod
    def handle(self, request: Request):
        pass


class Request():
    """
        Класс запроса.
        Т.е это и есть запрос который пойдет по цепочке обязанностей в надежде,
        что его кто-нибудь обработает.
    """
    def __init__(self, name: str, type_request: TypeRequest):
        self.name = name
        self._type_request = type_request

    @property
    def type_requst(self):
        return self._type_request

    @type_requst.setter
    def type_request(self, type_request: TypeRequest):
        self._type_request = type_request


class AbstractHandler(IHandler):
    """
        Поведение цепочки по умолчанию может быть реализовано внутри базового класса
        обработчика.
    """
    def __init__(self, handler: AbstractHandler = None):
        self._next_handler = handler

    @property
    def handler(self):
        """
            Получаем следующий обработчик для запроса
        """
        return self._next_handler

    @handler.setter
    def handler(self, handler: IHandler):
        """
            Устанавливаем следующий обработчик для запроса
        """
        self._next_handler = handler

    @abstractmethod
    def check_request(self):
        pass

    def handle(self, request: Request):
        """
            Метод обработки запроса. Если запрос не прошел проверку, то передаем его
            следующему обработчику в цепочке обязанностей.
        """
        result = self.check_request(request)
        if not result and self._next_handler:
            self._next_handler.handle(request)


"""
    Типовые классы различных типов получателей запроса, т.е те кто в принципе может
    получить запрос на обработку. Обрабатывает запрос сам (если зпрос относится к его обязанностям)
    либо отдает дальше по цепочке.
"""


class ReceiverWork(AbstractHandler):
    def __init__(self, handler: AbstractHandler = None):
        self._next_handler = handler

    def check_request(self, request: Request) -> bool:
        check = request.type_requst == TypeRequest.WORK
        if check:
            print(f"Приступаем к обработке запроса типа {TypeRequest.WORK}")
        else:
            print("Запрос перается следующему обработчику")
        return check


class ReceiverPersonal(AbstractHandler):
    def __init__(self, handler: AbstractHandler = None):
        self._next_handler = handler

    def check_request(self, request: Request) -> bool:
        check = request.type_requst == TypeRequest.PERSONNAL
        if check:
            print(f"Приступаем к обработке запроса типа {TypeRequest.PERSONNAL}")
        else:
            print("Запрос перается следующему обработчику")
        return check


class ReceiverCommon(AbstractHandler):
    def __init__(self, handler: AbstractHandler = None):
        self._next_handler = handler

    def check_request(self, request: Request) -> bool:
        check = request.type_requst == TypeRequest.COMMON
        if check:
            print(f"Приступаем к обработке запроса типа {TypeRequest.COMMON}")
        else:
            print("Запрос перается следующему обработчику")
        return check


def test_chain(receiver: AbstractHandler, request: Request):
    """
        Тестовая функция для отладки
    """
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
