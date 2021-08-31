from Core.Interface.Widgets.Main import Main
from Gameplay.Widgets.Menu import Menu
from Gameplay.Widgets.Footer import Footer

class MainWindow(Main):
    def __init__(
        self,
        parent=None,
    ):
        super().__init__(parent)

        Menu(x=0, y=0, width=25, height=self._height, parent=self)
        Footer(x=0, y=self._height-1, parent=self)


    def _fill(self):
        pass

        
