from Core.Interface.Widgets.Widget import Widget

from Core.Events.Events import Events
from Core.Events.EventsController import EventsController


class Footer(Widget):
    def __init__(self, x=0, y=0, parent=None):
        super().__init__(x, y, parent.width(), parent.height(), parent)

        self.focusable(False)
        EventsController().subscribe(Events.KEY_H_PRESSED, self.toggle_showed)
    
    def _fill(self) -> None:
        msg_back = "[SHIFT+TAB] Назад"
        msg_forward = "[TAB] Вперед"
        msg_avaliable = "[UP/DOWN] Выбор ответа [ENTER] Отправить"
        spaces = " " * ((self._width - len(msg_back) - len(msg_avaliable) - len(msg_forward)) // 2)
        msg = f"{msg_back}{spaces}{msg_avaliable}{spaces}{msg_forward}"
        self._widget.addstr(0, 0, msg, self._color_pair)

    def toggle_showed(self):
        if self.showed():
            self.hide()
        else:
            self.show()
