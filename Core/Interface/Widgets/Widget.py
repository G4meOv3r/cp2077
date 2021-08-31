import curses
from Core.Interface.Colors import Colors

class Widget:
    _focused = None

    def __init__(
        self,
        x=0, y=0, 
        width=0, height=0,
        parent=None
    ):
        # Геометрия
        self._x = x
        self._y = y
        self._width = width
        self._height = height

        # Дерево компонентов
        self._parent = parent
        if parent:
            parent.add_child(self)
            self._x += parent.x()
            self._y += parent.y()
        self._children = []

        # Поля управления рендером
        self._showed = False

        # Поля состояний
        self._focusable = True
        self._focused_child = -1

        # Цветовая пара
        self._color_pair = Colors().get(Colors.WHITE, Colors.BLACK)
        
        # Виджет
        self._widget = curses.newwin(self._height, self._width, self._y, self._x)

        # Подсказка по использованию
        self._hint = ""


    # Методы рендера
    def render(self) -> None:
        if not self._showed: return
        self._flush()
        self._fill()
        self._refresh()
        for child in self._children:
            child.render()
    def _flush(self) -> None:
        for y in range(self._height):
            for x in range(self._width):
                try:
                    self._widget.addch(y, x, ' ', self._color_pair)
                except:
                    pass
    def _fill(self) -> None:
        pass
    def _refresh(self) -> None:
        self._widget.refresh()


    # Методы управления рендером
    def show(self) -> None:
        self.showed(True)
        for child in self._children:
            child.show()
    def hide(self) -> None:
        self.showed(False)
        for child in self._children:
            child.hide()


    # Методы управления деревом компонентов
    def add_child(self, widget):
        self._children.append(widget)
    def remove_child(self, widget):
        self._children.pop(self._children.index(widget))
    def _focus_forward(self):
        for child_index in range(self._focused_child+1, len(self._children)):
            child = self._children[child_index]
            if child.focusable():
                self._focused_child = child_index
                child.focus()
                break
        else:
            if type(self._parent) != Widget:
                self._focused_child = -1
                self.focus()
            else:
                self._parent.focus_forward()


    # Методы вызова состояний
    def focus(self):
        Widget._focused.blur()
        Widget._focused = self
        self.on_focus()
    def blur(self):
        Widget._focused = None
        self.on_blur()


    # Методы доступа к ограниченным полям
    def x(self, _x = None):
        if _x != None:
            if _x + self._width > self.parent(): raise Exception("Widget out of bounds")
            delta = _x - self._x
            self._x += delta

            for child in self._children:
                child.x(child.x() + delta)
        else:
            return self._x
    def y(self, _y = None):
        if _y != None:
            if _y + self._height > self.parent(): raise Exception("Widget out of bounds")
            delta = _y - self._y
            self._y += delta

            for child in self._children:
                child.y(child.y() + delta)
        else:
            return self._y
    def width(self, _width = None):
        if _width != None:
            if self.x() + _width > self.parent().width(): raise Exception("Widget out of bounds")
            self._width = _width
        else:
            return self._width
    def height(self, _height = None):
        if _height != None:
            if self.y() + _height > self.parent().height(): raise Exception("Widget out of bounds")
            self._height = _height
        else:
            return self._height
    
    def parent(self):
        return self._parent
    def children(self):
        return self._children

    def showed(self, _showed = None):
        if _showed != None:
            self._showed = _showed
        else:
            return self._showed    
    def focused(self, _focused = None):
        if _focused != None:
            if _focused:
                self.focus()
            else:
                self.blur()
        else:
            return self._focused == self
    def focusable(self, _focusable = None):
        if _focusable != None:
            self._focusable = _focusable
        else:
            return self._focusable
    def focused_child(self, _focused_child = None):
        if _focused_child != None:
            self._focused_child = _focused_child
        else:
            return self._focused_child


    # Сигналы для переопределения 
    def on_focus(self):
        pass
    def on_blur(self):
        pass


    @classmethod
    def focus_forward(cls):
        widget = Widget._focused
        children = widget.children()
        for child_index in range(len(children)):
            child = children[child_index]
            if child.focusable():
                widget.focused_child(child_index)
                child.focus()
                break
        else:
            widget.parent()._focus_forward()