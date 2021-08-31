from Core.Interface.Widgets.Widget import Widget

class Main(Widget):
    def __init__(self, parent):
        height, width = parent.getmaxyx()
        super().__init__(0, 0, width, height)
        
        self._parent = parent
        Widget._focused = self
