import curses
from Core.Snippets.Singletone import SingletonMeta

class Colors(metaclass=SingletonMeta):
    BLACK = 0
    WHITE = 1

    def __init__(self):
        curses.init_color(0, 0, 0, 0)
        curses.init_color(1, 1000, 1000, 1000)

        self._count = 1
        self._pairs = {}
    
    def get(self, foreground, background):
        try:
            with_foreground = self._pairs[foreground]
            try:
                pair_number = with_foreground[background]
            except KeyError:
                curses.init_pair(self._count, foreground, background)
                pair_number = self._count
                self._count += 1
                with_foreground[background] = pair_number
        except KeyError:
            curses.init_pair(self._count, foreground, background)
            pair_number = self._count
            self._count += 1
            self._pairs[foreground] = { background: pair_number }

        return curses.color_pair(pair_number)
        

