from __future__ import annotations
from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def insertQuarter(self):
        pass

    @abstractmethod
    def ejectQuarter(self):
        pass

    @abstractmethod
    def turnCrank(self):
        pass

    @abstractmethod
    def give(self):
        pass
class HasQuarter(State):
    def insertQuarter(self):
        pass

    def ejectQuarter(self):
        pass

    def turnCrank(self):
        pass

    def give(self):
        pass

class NoQuarter(State):
    def insertQuarter(self):
        pass

    def ejectQuarter(self):
        pass

    def turnCrank(self):
        pass

    def give(self):
        pass

class Sold(State):
    def insertQuarter(self):
        pass

    def ejectQuarter(self):
        pass

    def turnCrank(self):
        pass

    def give(self):
        pass

class SoldOUt(State):
    def insertQuarter(self):
        pass

    def ejectQuarter(self):
        pass

    def turnCrank(self):
        pass

    def give(self):
        pass

class GumMachine:
    def __init__(self, count: int):
        self._count = count

if __name__ == "__main__":
    machine = GumMachine(20)