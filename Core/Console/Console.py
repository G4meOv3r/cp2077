class ConsoleMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Console(metaclass=ConsoleMeta):
    def __init__():
        pass

    def message(*args, **kwargs): 
        pass

    def dialog(*args, **kwargs):
        pass

