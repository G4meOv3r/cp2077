from Core.Interface.Colors import Colors
import curses

class Widget:
    def __init__(
        self,
        x=0, y=0, 
        width=0, height=0,
        frame_width=None, frame_height=None, 
        shift_x=0, shift_y=0,
        parent=None
    ):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._frame_width = frame_width if frame_width else self._width
        self._frame_height = frame_height if frame_height else self._height
        self._shift_x = shift_x
        self._shift_y = shift_y
        self._children = []
        self._parent = parent
        self._show = False

        self._color_pair = Colors().get(Colors.WHITE, Colors.BLACK)
        self._widget = curses.newwin(self._height, self._width, self._y, self._x)
        
        if parent: parent.add_child(self)

    def render(self) -> None:
        if not self._show: return
        self._flush()
        self._fill()
        self._refresh()
        for child in self._children:
            child.render()

    def _flush(self) -> None:
        for y in range(self._height):
            for x in range(self._width):
                try:
                    self._widget.addch(y, x, '*', self._color_pair)
                except:
                    pass

    def _fill(self) -> None:
        pass

    def _refresh(self) -> None:
        self._widget.refresh()

    def show(self) -> None:
        self._show = True
        for child in self._children:
            child.show()
    
    def hide(self) -> None:
        self._show = False
        for child in self._children:
            child.hide()

    def add_child(self, widget):
        self._children.append(widget)
