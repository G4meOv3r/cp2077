import curses
from typing import Counter
from Core.Interface.Widget import Widget
from Core.Interface.Colors import Colors

class Menu(Widget):
    def __init__(
        self,
        x=0, y=0, 
        width=0, height=0,
        frame_width=None, frame_height=None, 
        shift_x=0, shift_y=0,
        parent=None
    ):
        super().__init__(x, y, width, height, frame_width, frame_height, shift_x, shift_y, parent)
        self._color_pair = Colors().get(Colors.BLACK, Colors.WHITE)

    def _fill(self):
        msg = "   Инвентарь    "
        x = (self._width - len(msg)) // 2
        self._widget.addstr(0, x, msg, self._color_pair | curses.A_BOLD)