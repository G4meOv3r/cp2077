class ConsoleMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Console(metaclass=ConsoleMeta):
    color_palette = {
            "black"     : "30",
            "red"       : "31",
            "green"     : "32",
            "yellow"    : "33",
            "blue"      : "34",
            "purple"    : "35",
            "cian"      : "36",
            "white"     : "37"
        }
        background_palette = {
            "black"     : "40",
            "red"       : "41",
            "green"     : "42",
            "yellow"    : "43",
            "blue"      : "44",
            "purple"    : "45",
            "cian"      : "46",
            "white"     : "47",
        }
        effect_palette = {
            "default"   : "40",
            "bold"      : "41",
            "thin"      : "42",
            "italic"    : "43",
            "underline" : "44",
            "blink"     : "45",
            "fast_blink": "46",
            "swap"      : "47",
        }

    def __init__():
        pass

    def message(self, *args, **kwargs): 
        color, background, effect, message, end = kwargs
        print()


    def dialog(self, *args, **kwargs):
        pass

