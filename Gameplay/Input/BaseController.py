from Core.Events.Events import Events
from Core.Events.EventsController import EventsController
from Core.Interface.Widgets.Widget import Widget

class BaseController:
    def __init__(self):
        self._subscribers = []

    def on(self):
        self._subscribers.append(EventsController().subscribe(Events.KEY_TAB_PRESSED, self.onTab))

    def onTab(self):
        Widget.focus_forward()
