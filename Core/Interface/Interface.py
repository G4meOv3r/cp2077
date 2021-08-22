import curses
from Core.Snippets.Singletone import SingletonMeta

class Interface(metaclass=SingletonMeta):
    def __init__(self, main_cls):
        self._terminated = False

        self._stdscr = curses.initscr()
        self._main_cls = main_cls

    def start(self) -> None:
        try:
            self._stdscr.keypad(True)
            curses.noecho()
            curses.cbreak()
            curses.curs_set(0)
            curses.start_color()
            self._mainloop()
        except Exception as e:
            self._stdscr.keypad(False)
            curses.echo()
            curses.nocbreak()
            curses.curs_set(1)
            curses.endwin()
            print(repr(e))

    def _mainloop(self) -> None:
        self._main = self._main_cls(parent=self._stdscr)
        self._main.show()
        while not self._terminated:
            self._main.render()
            pressed_key = self._stdscr.getkey()

    def terminate(self) -> None:
        self._terminated = True

        

