from abc import ABC, abstractmethod

class CaffeineBeverage(ABC):
    """
    Абстрактный Класс определяет шаблонный метод, содержащий скелет некоторого
    алгоритма, состоящего из вызовов (обычно) абстрактных примитивных операций.

    Конкретные подклассы должны реализовать эти операции, но оставить сам
    шаблонный метод без изменений.
    """
    def prepareRecipe(self):
        """
            Шаблонный метод определяет последовательность
            выполняемых операций.
         """
        self.boilWater()
        self.brew()
        self.addCondimets()
        self.pourInCup()

    # Метод обязан быть реализован субклассом
    @abstractmethod
    def addCondimets(self):
        pass

    # Метод обязан быть реализован субклассом
    @abstractmethod
    def brew(self):
        pass

    """ Эти методы являются методами по умолчанию 
        и не нуждаются в переопределении. Но если субклассам
        требется переопределение, то они могут это сделать.
    """
    def boilWater(self):
        print('Кипятим воду')

    def pourInCup(self):
        print('Разливаем напиток')

class Tea(CaffeineBeverage):
    """
        Конкретные классы должны реализовать все абстрактные операции базового
        класса.
    """
    def brew(self):
        print("Заваривам чай")

    def addCondimets(self):
        print("Добавим сахар")
class Coffee(CaffeineBeverage):
    def brew(self):
        print("Варим кофе")

    def addCondimets(self):
        print("Добавим молоко")

if __name__ == "__main__":
    tea = Tea()
    res = tea.prepareRecipe()