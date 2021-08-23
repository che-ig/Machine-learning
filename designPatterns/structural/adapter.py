class Target:
    def query(self) -> str:
        return "query from Target"

class Adaptee:
    def specialQuery(self) -> str:
        return "the method specialQuery from Adaptee"
class Adapter:
    def __init__(self, adaptee: Adaptee) -> None:
        self._adaptee = adaptee

    def query(self) -> str:
        return self._adaptee.specialQuery()

def client_code(target):
    return target.query()

if __name__ == "__main__":
    adapted = Adapter(Adaptee())
    print(client_code(adapted))