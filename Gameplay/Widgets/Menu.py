import curses

from Core.Interface.Widgets.Widget import Widget
from Core.Interface.Colors import Colors

class Menu(Widget):
    def __init__(
        self,
        x=0, y=0, 
        width=0, height=0,
        parent=None
    ):
        super().__init__(x, y, width, height, parent)
        self._color_pair = Colors().get(Colors.BLACK, Colors.WHITE)

    def _fill(self):
        msg = "Инвентарь"
        x = (self._width - len(msg)) // 2
        if self._focused == self:   
            self._widget.addstr(0, x, msg, self._color_pair | curses.A_BOLD | curses.A_UNDERLINE)
        else:
            self._widget.addstr(0, x, msg, self._color_pair | curses.A_BOLD)