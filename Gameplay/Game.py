from Core.Interface.Interface import Interface
from Gameplay.Widgets.MainWindow import MainWindow
from Gameplay.Input.BaseController import BaseController

class Game:
    def __init__(self):
        self.controller = BaseController()
    
    def start(self):
        self.controller.on()
        Interface(MainWindow).start()