from __future__ import annotations
from abc import ABC, abstractmethod

class Dialog(ABC):
    def work(self):
        btn = self.createButton()
        btn.render()

    @abstractmethod
    def createButton():
        pass

class IButton(ABC):

    @abstractmethod
    def render():
        pass

class WindowButton(IButton):
    def render(self):
        print('render windows button') 

class LinuxButton(IButton):
    def render(self):
        print('render lunux button')

class WindowDailog(Dialog):
    def createButton(self):
        return WindowButton()

class linuxDailog(Dialog):
    def createButton(self):
        return LinuxButton()

def client_code(creator):
    creator.work()
    
if __name__ == '__main__':
    typeButton = input('Ведите win или lunux ')
    if typeButton == 'win':
        dialog = WindowDailog()
    else:
        dialog = linuxDailog()


    # button = dialog.createButton()
    client_code(dialog)