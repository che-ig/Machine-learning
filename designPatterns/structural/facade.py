from __future__ import annotations

class subSystem_A():
    def do_open(self) -> str:
        return "method do_open from subSystem_A"

    def do_close(self) -> str:
        return "method do_close from subSystem_A"

class subSystem_B():
    def start(self) -> str:
        return "method start from subSystem_B"

    def finish(self) -> str:
        return "method finish from subSystem_B"
class Facade:
    """ 
        Фасад предоставляем простой интерфейс для работы со сложной подсистемой.
        Таким образом снижается взаимосвязь между клиентом и подсистемой.
        Фасад делегирует запрос клиента к соответствующим объектам подсистемы.
    """
    def __init__(self, system_a: subSystem_A, system_b: subSystem_B) -> None:
        self._stysem_a = system_a or subSystem_A() 
        self._stysem_b = system_b or subSystem_B()

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
    client_code(Facade(subSystem_A(), subSystem_B()))