from __future__ import annotations


class SubSystemA():
    def do_open(self) -> str:
        return "method do_open from SubSystemA"

    def do_close(self) -> str:
        return "method do_close from SubSystemA"


class SubSystemB():
    def start(self) -> str:
        return "method start from SubSystemB"

    def finish(self) -> str:
        return "method finish from SubSystemB"


class Facade:
    """
        Фасад предоставляем простой интерфейс для работы со сложной подсистемой.
        Таким образом снижается взаимосвязь между клиентом и подсистемой.
        Фасад делегирует запрос клиента к соответствующим объектам подсистемы.
    """
    def __init__(self, system_a: SubSystemA, system_b: SubSystemB) -> None:
        self._stysem_a = system_a or SubSystemA()
        self._stysem_b = system_b or SubSystemB()

    def operation(self):
        print(self._stysem_a.do_open(),
              self._stysem_a.do_close(),

              self._stysem_b.start(),
              self._stysem_b.finish(), sep='\n')


def client_code(facade: Facade) -> None:
    """
        Клиентский код работает с урощенным интерфийсом, предоставляемый фасадом
        и может не подозревать о всей сложности подсистемы.
    """
    facade.operation()


if __name__ == "__main__":
    client_code(Facade(SubSystemA(), SubSystemB()))
