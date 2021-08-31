import curses
from time import sleep
from Core.Snippets.Singletone import SingletonMeta
from Core.Input.InputController import InputController

class Interface(metaclass=SingletonMeta):
    def __init__(self, main_cls):
        self._terminated = False

        self._stdscr = curses.initscr()
        self._main_cls = main_cls
        self._main = None

    # Методы управления
    def start(self) -> None:
        try:
            self._stdscr.keypad(True)
            curses.noecho()
            curses.cbreak()
            curses.curs_set(False)
            curses.start_color()
            self._mainloop()
        except Exception as e:
            self._stdscr.keypad(False)
            curses.echo()
            curses.nocbreak()
            curses.curs_set(True)
            curses.endwin()
            print(repr(e))
    def terminate(self) -> None:
        self._terminated = True

    
    # Главный цикл
    def _mainloop(self) -> None:
        self._main = self._main_cls(self._stdscr)
        self._main.show()
        while not self._terminated:
            self._main.render()
            InputController().input(self._stdscr.getkey())

    def debug(self, msg):
        self._stdscr.addstr(0, 0, msg, curses.color_pair(1))
        sleep(0.1)


    # Методы доступа к ограниченным полям
    def main(self):
        return self._main
