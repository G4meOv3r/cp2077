from Core.Interface.Widget import Widget
from Gameplay.Widgets.Menu import Menu

class MainWindow(Widget):
    def __init__(
        self,
        x=0, y=0, 
        width=0, height=0,
        frame_width=None, frame_height=None, 
        shift_x=0, shift_y=0,
        parent=None,
    ):
        height, width = parent.getmaxyx()
        super().__init__(
            height=height, width=width,
        )

        Menu(x=0, y=0, width=30, height=self._height, parent=self)


    def _fill(self):
        pass

        
