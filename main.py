from abc import ABC, abstractmethod
import platform


class Window(ABC):
    @abstractmethod
    def draw(self):
        pass

class WindowsWindow(Window):
    def draw(self):
        pass #render a window in windows style


class MacWindow(Window):
    def draw(self):
        pass #render a window in Mac style


class LinuxWindow(Window):
    def draw(self):
        pass #render a window in Linux style

class Button(ABC):
    @abstractmethod
    def draw(self):
        pass

class WindowsButton(Button):
    def draw(self):
        pass #render a button in Windows style

class MacButton(Button):
    def draw(self):
        pass #render a button in Mac style

class LinuxButton(Button):
    def draw(self):
        pass #render a button in Linux style


class AbestractFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_window(self):
        pass

class windowsFactory(AbestractFactory):
    def create_button(self):
        return WindowsButton()

    def create_window(self):
        return WindowsWindow()
    
class MacFactory(AbestractFactory):
    def create_button(self):
        return MacButton()
    
    def create_window(self):
        return MacWindow()
    
class LinuxFactory(AbestractFactory):
    def create_button(self):
        return LinuxButton()
    
    def create_window(self):
        return LinuxWindow()
    

class AplicationUI:
    def __init__(self, factory:AbestractFactory):
        self.__factory = factory


    def create_ui(self):
        window = self.__factory.create_window()
        button = self.__factory.create_button()
        window.draw()
        button.draw()

def main():
    platform_name = platform.system()
    if platform_name == 'Linux':
        factory = LinuxFactory()

    elif platform_name == "MacOS":
        factory = MacFactory()
    else:
        factory = windowsFactory()
    
    application = AplicationUI(factory)
    application.create_ui()
