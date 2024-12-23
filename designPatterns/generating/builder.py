from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum


class Material(Enum):
    WOOD = "wood"
    BRICK = "brick"
    BLOCK = "block"
    UNKNOWN = "unknown"


class IBuilder(ABC):
    """
    Интерфейс строителя объявляет методы для создания частей
    объекта или продуктов.
    """

    @abstractmethod
    def add_swimming_pool(self) -> None:
        pass

    @abstractmethod
    def add_door(self) -> None:
        pass

    @abstractmethod
    def add_window(self) -> None:
        pass

    @abstractmethod
    def add_garage(self) -> None:
        pass

    @abstractmethod
    def get_result(self) -> None:
        pass


class House:
    """
    Паттерн строитель имеет смысл использовать только тогда, когда
    ваш продукт имеет сложную систему конфигурации.

    Конкретные строители могут производить несвязанные продукты т.е
    результаты строительства могут не всегда следовать одному и тому же
    интерфейсу (в этом их отличие от др. порождающий паттернов)
    """

    def __init__(self) -> None:
        self.material_house = None
        self.material_garage = Material.UNKNOWN
        self.doors: int = 1
        self.windows: int = 1
        self.garage: bool = False
        self.swimming_pool: bool = False

    def __str__(self) -> str:
        info: str = (
            f"Материал гаража {self.material_garage.value} \n"
            f"Количество дверей {self.doors} \n"
            f"Количество окон {self.windows} \n"
            f"Есть ли гараж {self.garage} \n"
            f"Есть ли бассеин {self.swimming_pool} \n\n"
        )

        return info


"""
    Классы конкретных строителей следуют интерфейсу строителя и предоставляют
    собственные реализации шагов построения объекта.
"""


class WoodBuilder(IBuilder):
    def __init__(self) -> None:
        self._house = House()
        self._house.material_house = Material.WOOD

    def add_window(self) -> None:
        # В деревянном доме не может быть больше одного окна
        pass

    def add_door(self) -> None:
        # В деревянном доме не может быть больше одной двери
        pass

    def add_garage(self) -> None:
        self._house.garage = True
        self._house.material_garage = Material.BRICK

    def add_swimming_pool(self) -> None:
        # В деревянном доме не может быть бассеина
        pass

    def get_result(self):
        return self._house


class BrickBuilder(IBuilder):
    def __init__(self) -> None:
        self._house = House()
        self._house.material_house = Material.BRICK

    def add_window(self) -> None:
        self._house.windows += 1

    def add_door(self) -> None:
        self._house.doors += 1

    def add_garage(self) -> None:
        self._house.garage = True
        self._house.material_garage = Material.BRICK

    def add_swimming_pool(self) -> None:
        self._house.swimming_pool = True

    def get_result(self):
        return self._house


class Director:
    """
    Директор отвечает за порядок следования шагов простроения объекта.
    Полезно для построения объекта специфической структуры или важен порядок шагов созданя продукта
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder: IBuilder) -> None:
        """
        Директор работает с любым экземпляром строителя.
        Клиентский код может выбрать строителя для построения объекта.
        """
        self._builder = builder

    def create_max_house(self) -> None:
        self._builder.add_window()
        self._builder.add_door()
        self._builder.add_garage()
        self._builder.add_swimming_pool()

    def create_base_house(self) -> None:
        self._builder.add_window()
        self._builder.add_door()


if __name__ == "__main__":
    director = Director()
    for nbuilder in (WoodBuilder, BrickBuilder):
        builder = nbuilder()
        director.builder = builder
        director.create_max_house()
        house = builder.get_result()
        print(house)
