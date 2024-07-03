from abc import ABC, abstractmethod


class ISubject(ABC):
    """
    Интерфейс Субъекта объявляет общие операции как для Реального Субъекта, так
    и для Заместителя. Клиент думает, что работает с реальным объектом, но на самом
    деле с proxy. Разницу не видно т.к оба объекта реализуют идентичный интерфейс.
    """

    @abstractmethod
    def request(self):
        pass


class RealSubject(ISubject):
    """
    Реальный объект. Содержит интересующие клиента методы.
    """

    def request(self):
        print("Вызвали метод request реальный объекта")


class Proxy(ISubject):
    """
    Прокси должен иметь одинаковый набор методов что и реальный объект
    """

    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Проверяем доспуп клиента к реальному объекту")
        return True

    def log_access(self):
        print("Логируем обращение клиента к реальному объекту")


def client_code(subject: ISubject):
    """
    Клиентский код должен работать со всеми объектами (как с реальными, так и
    заместителями) через интерфейс Субъекта, чтобы поддерживать как реальные
    субъекты, так и заместителей.
    """
    subject.request()


if __name__ == "__main__":
    real_subject = RealSubject()
    client_code(real_subject)
    print("\n")
    proxy_subject = Proxy(real_subject)
    client_code(proxy_subject)
