from functools import reduce

from Core.Console.Colors import Colors
from Core.Console.Effects import Effects

class ConsoleMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Console(metaclass=ConsoleMeta):
    def __init__(self):
        pass

    def message(self, message, *args, **kwargs):
        print(message)

    def dialog(self, *args, **kwargs):
        pass